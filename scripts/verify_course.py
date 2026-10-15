"""Kurs kitabı doğrulaması. Yalnızca standart kütüphane.

Kullanım:
  python scripts/verify_course.py
  python scripts/verify_course.py --page hafta01-gun01.html
  python scripts/verify_course.py --strict
"""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTEXT = ROOT / "context.md"
COURSE_JS = ROOT / "assets" / "js" / "course.js"

PAGE_RANGES: dict[str, range] = {
    "hafta01-gun01.html": range(1, 9),
    "hafta01-gun02.html": range(9, 12),
    "hafta01-gun03.html": range(12, 17),
    "hafta01-gun04.html": range(17, 22),
    "hafta01-gun05.html": range(22, 29),
    "hafta02-gun01.html": range(29, 34),
    "hafta02-gun02.html": range(34, 40),
    "hafta02-gun03.html": range(40, 43),
    "hafta02-gun04.html": range(43, 47),
    "hafta02-gun05.html": range(47, 50),
    "hafta03-gun01.html": range(50, 56),
    "hafta03-gun02.html": range(56, 59),
    "hafta03-gun03.html": range(59, 62),
    "hafta03-gun04.html": range(62, 65),
    "hafta03-gun05.html": range(65, 69),
    "hafta04-gun01.html": range(69, 72),
    "hafta04-gun02.html": range(72, 76),
    "hafta04-gun03.html": range(76, 81),
    "hafta04-gun04.html": range(81, 86),
    "hafta04-gun05.html": range(86, 92),
    "hafta05-gun01.html": range(92, 96),
    "hafta05-gun02.html": range(96, 99),
    "hafta05-gun03.html": range(99, 103),
    "hafta05-gun04.html": range(103, 106),
    "hafta05-gun05.html": range(106, 109),
    "hafta06-gun01.html": range(109, 116),
    "hafta06-gun02.html": range(116, 120),
    "hafta06-gun03.html": range(120, 124),
    "hafta06-gun04.html": range(124, 128),
    "hafta06-gun05.html": range(128, 133),
}

LAB_PAGES: dict[str, tuple[str, ...]] = {
    "hafta01-gun01.html": ("lab-n8n-demo", "lab-chaining"),
    "hafta01-gun03.html": ("lab-8-llm", "lab-ollama", "lab-llm-judge"),
    "hafta01-gun05.html": ("lab-checklist-loop",),
    "hafta02-gun02.html": ("lab-3-orkestrasyon",),
    "hafta03-gun01.html": ("lab-debate-crew",),
    "hafta03-gun02.html": ("lab-financial-researcher",),
    "hafta03-gun04.html": ("lab-docker-coding-agent",),
    "hafta04-gun02.html": ("lab-first-langgraph",),
    "hafta04-gun03.html": ("lab-playwright-mcp",),
    "hafta04-gun04.html": ("lab-deep-agent-fs-todo", "lab-skill-pptx"),
    "hafta05-gun01.html": ("lab-adk-first-agent", "lab-a2a-demo"),
    "hafta05-gun02.html": ("lab-strands-first-agent", "lab-pydantic-ai-first-agent"),
    "hafta05-gun03.html": ("lab-ms-agent-framework", "lab-agno-first-agent"),
    "hafta05-gun04.html": ("lab-mastra-first-agent",),
    "hafta06-gun01.html": ("lab-fetch-playwright-filesystem",),
    "hafta06-gun02.html": ("lab-fastmcp-server",),
    "hafta06-gun03.html": ("lab-qdrant-rag",),
}

VERIFY_NOTE_PAGES = {
    "hafta03-gun05.html",
    "hafta05-gun05.html",
    "hafta06-gun01.html",
    "hafta06-gun04.html",
    "hafta06-gun05.html",
}

PROJECT_PAGES: dict[str, tuple[str, ...]] = {
    "hafta01-gun05.html": ("proje-1",),
    "hafta02-gun02.html": ("proje-2",),
    "hafta02-gun05.html": ("proje-3",),
    "hafta03-gun03.html": ("proje-4",),
    "hafta03-gun05.html": ("proje-5",),
    "hafta04-gun05.html": ("proje-6",),
    "hafta05-gun05.html": ("proje-7", "proje-agent-loop"),
    "hafta06-gun05.html": ("proje-8",),
}

STEPS = (
    "step-need",
    "step-model",
    "step-code",
    "step-extend",
    "step-fail",
    "step-observe",
    "step-task",
    "step-why",
)

VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "source", "track", "wbr",
}

BALANCE_TAGS = {
    "div", "section", "table", "thead", "tbody", "tr", "td", "th",
    "pre", "code", "span", "a", "ul", "ol", "li", "article", "main",
    "nav", "header",
}

FORBIDDEN = re.compile(
    r"TODO|TBD|FIXME|lorem|devamı gelecek|burada .{0,40} olacak",
    re.IGNORECASE,
)


class Node:
    def __init__(self, tag: str, attrs: dict[str, str]):
        self.tag = tag
        self.attrs = attrs
        self.children: list[Node] = []
        self.text = ""

    @property
    def classes(self) -> set[str]:
        return set(self.attrs.get("class", "").split())

    @property
    def id(self) -> str:
        return self.attrs.get("id", "")


class Builder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {})
        self.stack = [self.root]
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = Node(tag, {k: (v or "") for k, v in attrs})
        self.stack[-1].children.append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = Node(tag, {k: (v or "") for k, v in attrs})
        self.stack[-1].children.append(node)

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID_TAGS:
            return
        if len(self.stack) == 1 or self.stack[-1].tag != tag:
            self.errors.append(f"kapanış uyuşmuyor: </{tag}> (açık: {self.stack[-1].tag})")
            for i in range(len(self.stack) - 1, 0, -1):
                if self.stack[i].tag == tag:
                    del self.stack[i:]
                    return
            return
        self.stack.pop()

    def handle_data(self, data: str) -> None:
        self.stack[-1].text += data


def walk(node: Node):
    yield node
    for child in node.children:
        yield from walk(child)


def text_of(node: Node) -> str:
    parts = [node.text]
    for child in node.children:
        parts.append(text_of(child))
    return "".join(parts)


def has_class(node: Node, name: str) -> bool:
    return any(name in n.classes for n in walk(node))


def by_id(root: Node, element_id: str) -> Node | None:
    for node in walk(root):
        if node.id == element_id:
            return node
    return None


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def escape_pre_bodies(html: str) -> str:
    def repl(match: re.Match[str]) -> str:
        open_tag, inner, close = match.group(1), match.group(2), match.group(3)
        inner = inner.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f"{open_tag}{inner}{close}"

    return re.sub(r"(<pre\b[^>]*>)(.*?)(</pre>)", repl, html, flags=re.S | re.I)


def parse(html: str) -> tuple[Node, list[str]]:
    builder = Builder()
    builder.feed(escape_pre_bodies(html))
    builder.close()
    if len(builder.stack) > 1:
        open_tags = [n.tag for n in builder.stack[1:]]
        builder.errors.append(f"kapanmamış etiketler: {open_tags}")
    return builder.root, builder.errors


def course_pages() -> list[str]:
    text = COURSE_JS.read_text(encoding="utf-8")
    return re.findall(r'file:\s*"([^"]+)"', text)


def lesson_catalog() -> dict[int, tuple[str, str]]:
    text = CONTEXT.read_text(encoding="utf-8")
    found: dict[int, tuple[str, str]] = {}
    for match in re.finditer(r"^\| (\d+) \| (.+?) \| ([^|]+?) \|", text, re.M):
        number = int(match.group(1))
        if 1 <= number <= 132 and number not in found:
            found[number] = (norm(match.group(2)), norm(match.group(3)))
    return found


def lesson_titles() -> dict[int, str]:
    return {number: title for number, (title, _duration) in lesson_catalog().items()}


def data_rows(table: Node) -> int:
    bodies = [n for n in table.children if n.tag == "tbody"]
    if bodies:
        return sum(1 for n in bodies[0].children if n.tag == "tr")
    return sum(1 for n in table.children if n.tag == "tr")


class Report:
    def __init__(self) -> None:
        self.pass_n = 0
        self.warn_n = 0
        self.fail_n = 0
        self.lines: list[str] = []

    def add(self, level: str, check: str, detail: str) -> None:
        if level == "PASS":
            self.pass_n += 1
        elif level == "WARN":
            self.warn_n += 1
        else:
            self.fail_n += 1
            level = "FAIL"
        self.lines.append(f"{level}  {check}: {detail}")


def check_file(name: str, pages: list[str], titles: dict[int, str], report: Report, full: bool) -> None:
    path = ROOT / name
    if not path.exists():
        report.add("FAIL", "2-envanter", f"{name} yok")
        return
    raw = path.read_text(encoding="utf-8")
    root, balance_errors = parse(raw)
    ids = {n.id for n in walk(root) if n.id}
    is_day = name in PAGE_RANGES
    is_book = name == "tam-kitap-baski.html"

    if 'charset="UTF-8"' not in raw and "charset='UTF-8'" not in raw:
        report.add("FAIL", "3-iskelet", f"{name}: charset UTF-8 yok")
    if 'lang="tr"' not in raw:
        report.add("FAIL", "3-iskelet", f"{name}: lang=tr yok")
    if "assets/css/course.css" not in raw:
        report.add("FAIL", "3-iskelet", f"{name}: course.css yok")
    if "assets/js/course.js" not in raw:
        report.add("FAIL", "3-iskelet", f"{name}: course.js yok")
    if not is_book and "page-jump-select" not in ids:
        report.add("FAIL", "3-iskelet", f"{name}: page-jump-select yok")
    if name not in {"index.html", "tam-kitap-baski.html"} and not has_class(root, "page-footer-nav"):
        report.add("FAIL", "3-iskelet", f"{name}: page-footer-nav yok")
    if not is_book and not has_class(root, "chapter-header"):
        report.add("FAIL", "3-iskelet", f"{name}: chapter-header yok")

    if is_day:
        expected = list(PAGE_RANGES[name])
        cards = [n for n in walk(root) if "lesson-card" in n.classes]
        found_numbers = []
        for card in cards:
            match = re.fullmatch(r"ders-(\d+)", card.id)
            if not match:
                report.add("FAIL", "4-ders-id", f"{name}: lesson-card id='{card.id}' ders-N değil")
                continue
            number = int(match.group(1))
            found_numbers.append(number)
            title_nodes = [n for n in walk(card) if "lesson-title-en" in n.classes]
            if not title_nodes:
                report.add("FAIL", "5-baslik", f"{name}: ders {number} İngilizce başlık yok")
            else:
                actual = norm(text_of(title_nodes[0]))
                wanted = titles.get(number, "")
                if actual != wanted:
                    report.add("FAIL", "5-baslik", f"{name}: ders {number} başlık uyuşmuyor: {actual!r} != {wanted!r}")
            for step in STEPS:
                boxes = [n for n in card.children if step in n.classes]
                boxes += [n for child in card.children for n in walk(child) if step in n.classes and n not in boxes]
                boxes = [n for n in walk(card) if step in n.classes]
                if len(boxes) != 1:
                    report.add("FAIL", "6-adim", f"{name}: ders {number} {step} sayısı {len(boxes)}")
                    continue
                if len(norm(text_of(boxes[0]))) < 80:
                    report.add("FAIL", "6-adim", f"{name}: ders {number} {step} 80 karakterden kısa")
                if step == "step-code" and not (has_class(boxes[0], "diagram-box") or any(n.tag == "pre" for n in walk(boxes[0]))):
                    report.add("FAIL", "6-adim", f"{name}: ders {number} step-code içinde pre veya diagram yok")
                if step == "step-observe" and not has_class(boxes[0], "trace-box"):
                    report.add("FAIL", "6-adim", f"{name}: ders {number} step-observe içinde trace-box yok")
            if found_numbers.count(number) > 1:
                report.add("FAIL", "4-ders-id", f"{name}: ders {number} birden fazla")
        if found_numbers != expected:
            report.add("FAIL", "4-ders-id", f"{name}: dersler {found_numbers} beklenen {expected}")
        else:
            report.add("PASS", "4-ders-id", f"{name}: ders {expected[0]}-{expected[-1]}")

        if not has_class(root, "badge-source"):
            report.add("FAIL", "7-rozet", f"{name}: badge-source yok")
        if not has_class(root, "badge-design"):
            report.add("FAIL", "7-rozet", f"{name}: badge-design yok")
        if not has_class(root, "callout-verify"):
            report.add("FAIL", "7-rozet", f"{name}: callout-verify yok")
        for lab_id in LAB_PAGES.get(name, ()):
            if lab_id not in ids:
                report.add("FAIL", "7-rozet", f"{name}: #{lab_id} yok")
        if name in LAB_PAGES and not has_class(root, "badge-lab"):
            report.add("FAIL", "7-rozet", f"{name}: badge-lab yok")
        if name in VERIFY_NOTE_PAGES and not has_class(root, "badge-verify"):
            report.add("FAIL", "7-rozet", f"{name}: badge-verify yok")
        for project_id in PROJECT_PAGES.get(name, ()):
            section = by_id(root, project_id)
            if section is None:
                report.add("FAIL", "7-rozet", f"{name}: #{project_id} yok")
                continue
            if not has_class(section, "badge-project") and "badge-project" not in raw:
                report.add("FAIL", "7-rozet", f"{name}: #{project_id} badge-project yok")
            tables = [n for n in walk(section) if n.tag == "table"]
            if not any(data_rows(table) >= 10 for table in tables):
                report.add("FAIL", "7-rozet", f"{name}: #{project_id} teslim tablosu 10 satırdan kısa")

        size = path.stat().st_size
        if size < 25000:
            report.add("FAIL", "11-boyut", f"{name}: {size} bayt (< 25000)")
        elif size < 45000:
            report.add("WARN", "11-boyut", f"{name}: {size} bayt (< 45000)")
        else:
            report.add("PASS", "11-boyut", f"{name}: {size} bayt")

    if name == "mod07-guvenilirlik-ve-mezuniyet.html":
        size = path.stat().st_size
        if size < 40000:
            report.add("FAIL", "11-boyut", f"{name}: {size} bayt (< 40000)")
        else:
            report.add("PASS", "11-boyut", f"{name}: {size} bayt")

    cleaned = re.sub(r'placeholder="[^"]*"', "", raw)
    for match in FORBIDDEN.finditer(cleaned):
        report.add("FAIL", "9-yasak", f"{name}: '{match.group(0)}'")
    if re.search(r"<pre\b[^>]*>\s*</pre>", raw, flags=re.S | re.I):
        report.add("FAIL", "9-yasak", f"{name}: boş pre")
    if re.search(r"<pre\b[^>]*>\s*<code>\s*</code>\s*</pre>", raw, flags=re.S | re.I):
        report.add("FAIL", "9-yasak", f"{name}: boş code")

    for error in balance_errors:
        if any(tag in error for tag in BALANCE_TAGS) or "kapan" in error:
            report.add("FAIL", "10-denge", f"{name}: {error}")

    check_links(name, raw, ids, pages, report)
    if name == "index.html":
        check_index_rows(raw, report, full)
    check_footer(name, root, pages, report)

    if not any(line.startswith("FAIL") and name in line for line in report.lines[-1:]):
        pass


def check_links(name: str, raw: str, ids: set[str], pages: list[str], report: Report) -> None:
    known = set(pages)
    missing: set[str] = set()
    seen_targets: set[str] = set()
    for href in re.findall(r'href="([^"]+)"', raw):
        if href.startswith(("http://", "https://", "mailto:", "javascript:")):
            continue
        file_part, _, fragment = href.partition("#")
        if not file_part:
            if fragment and fragment not in ids:
                report.add("FAIL", "8-link", f"{name}: #{fragment} bu sayfada yok")
            continue
        target = ROOT / file_part
        if file_part not in known and not target.exists():
            report.add("FAIL", "8-link", f"{name}: bilinmeyen hedef {href}")
            continue
        if not target.exists():
            missing.add(file_part)
            continue
        if fragment and file_part not in seen_targets:
            seen_targets.add(file_part)
        if fragment:
            target_html = target.read_text(encoding="utf-8")
            if f'id="{fragment}"' not in target_html and f"id='{fragment}'" not in target_html:
                report.add("FAIL", "8-link", f"{name}: {href} hedefinde id yok")
    if missing:
        report.add("WARN", "8-link", f"{name}: henüz yok ({len(missing)}): {', '.join(sorted(missing))}")


def check_index_rows(raw: str, report: Report, full: bool) -> None:
    rows = re.findall(
        r'<tr class="curriculum-row"><td>(\d+)</td><td><a href="([^"]+)">',
        raw,
    )
    if len(rows) != 132:
        report.add("FAIL", "8-link", f"index.html: curriculum-row sayısı {len(rows)}")
        return
    bad = []
    for number, href in rows:
        file_part = PAGE_RANGES and next(
            (page for page, span in PAGE_RANGES.items() if int(number) in span),
            "",
        )
        wanted = f"{file_part}#ders-{number}"
        if href != wanted:
            bad.append(f"{number}->{href}")
    if bad:
        report.add("FAIL", "8-link", f"index.html derin bağlantı: {bad[:5]}")
    else:
        report.add("PASS", "8-link", "index.html 132 ders bağlantısı doğru")
    if not full:
        return


def check_footer(name: str, root: Node, pages: list[str], report: Report) -> None:
    if name not in pages:
        return
    navs = [n for n in walk(root) if "page-footer-nav" in n.classes]
    if not navs:
        return
    hrefs = []
    for node in walk(navs[0]):
        if node.tag == "a" and node.attrs.get("href"):
            hrefs.append(node.attrs["href"].split("#", 1)[0])
    index = pages.index(name)
    expected = []
    if index > 0:
        expected.append(pages[index - 1])
    if index < len(pages) - 1:
        expected.append(pages[index + 1])
    for href in hrefs:
        if href not in expected:
            report.add("FAIL", "12-gezinti", f"{name}: footer {href} komşu değil ({expected})")


def check_inventory(pages: list[str], only: str | None, report: Report) -> None:
    if len(pages) != 34:
        report.add("FAIL", "2-envanter", f"COURSE_PAGES {len(pages)} kayıt (34 olmalı)")
    else:
        report.add("PASS", "2-envanter", "COURSE_PAGES 34 kayıt")
    targets = [only] if only else pages
    missing = [name for name in targets if not (ROOT / name).exists()]
    if missing:
        report.add("FAIL", "2-envanter", f"eksik dosya: {missing}")
    elif not only:
        report.add("PASS", "2-envanter", "34 dosyanın tamamı var")


def check_lessons_global(report: Report) -> None:
    found: dict[int, str] = {}
    for name in PAGE_RANGES:
        path = ROOT / name
        if not path.exists():
            continue
        for match in re.finditer(r'id="ders-(\d+)"', path.read_text(encoding="utf-8")):
            number = int(match.group(1))
            if number in found:
                report.add("FAIL", "4-ders-id", f"ders {number} hem {found[number]} hem {name}")
            found[number] = name
    if len(found) == 132 and set(found) == set(range(1, 133)):
        report.add("PASS", "4-ders-id", "1-132 her ders bir kez")
    else:
        missing = [n for n in range(1, 133) if n not in found]
        report.add("FAIL", "4-ders-id", f"eksik dersler: {missing[:20]}")


def check_print_book(pages: list[str], report: Report) -> None:
    path = ROOT / "tam-kitap-baski.html"
    if not path.exists():
        report.add("WARN", "13-kitap", "tam-kitap-baski.html yok")
        return
    newest_source = max((ROOT / name).stat().st_mtime for name in pages if name != "tam-kitap-baski.html" and (ROOT / name).exists())
    if path.stat().st_mtime < newest_source:
        report.add("WARN", "13-kitap", "tam-kitap kaynaklardan eski; yeniden derle")
    text = path.read_text(encoding="utf-8")
    lesson_ids = set(re.findall(r'id="ders-(\d+)"', text))
    parts = re.findall(r'id="part-[^"]+"', text)
    if len(lesson_ids) != 132:
        report.add("FAIL", "13-kitap", f"kitapta {len(lesson_ids)} ders id")
    if len(parts) != 33:
        report.add("FAIL", "13-kitap", f"kitapta {len(parts)} bölüm (33 olmalı)")
    if len(lesson_ids) == 132 and len(parts) == 33 and path.stat().st_mtime >= newest_source:
        report.add("PASS", "13-kitap", "tam kitap güncel, 132 ders, 33 bölüm")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--page", help="Tek dosya, ör. hafta01-gun01.html")
    parser.add_argument("--strict", action="store_true", help="Uyarıları da hata say")
    args = parser.parse_args()

    report = Report()
    if not CONTEXT.exists():
        report.add("FAIL", "1-kok", f"context.md yok: {ROOT}")
        print("\n".join(report.lines))
        return 1
    report.add("PASS", "1-kok", str(ROOT))

    pages = course_pages()
    titles = lesson_titles()
    if len(titles) != 132:
        report.add("FAIL", "5-baslik", f"context.md ders başlığı {len(titles)} (132 olmalı)")
    else:
        report.add("PASS", "5-baslik", "context.md 132 başlık okundu")

    check_inventory(pages, args.page, report)
    targets = [args.page] if args.page else [name for name in pages if (ROOT / name).exists()]
    for name in targets:
        check_file(name, pages, titles, report, full=not args.page)
    if not args.page:
        check_lessons_global(report)
        check_print_book(pages, report)

    print("\n".join(report.lines))
    print(f"\nPASS {report.pass_n} / WARN {report.warn_n} / FAIL {report.fail_n}")
    if report.fail_n or (args.strict and report.warn_n):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

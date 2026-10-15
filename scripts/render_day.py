"""Gün sayfası oluşturucu. İçerik scripts/content/*.json dosyasından gelir.

  python scripts/render_day.py scripts/content/hafta01-gun01.json
  python scripts/render_day.py scripts/content
"""

from __future__ import annotations

import json
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_course import (  # noqa: E402
    LAB_PAGES,
    PAGE_RANGES,
    PROJECT_PAGES,
    VERIFY_NOTE_PAGES,
    course_pages,
    lesson_catalog,
)

ROOT = Path(__file__).resolve().parent.parent

STEPS = (
    ("step-need", "1", "İhtiyaç"),
    ("step-model", "2", "Zihinsel model"),
    ("step-code", "3", "Minimum örnek"),
    ("step-extend", "4", "Genişletme"),
    ("step-fail", "5", "Başarısızlık örneği"),
    ("step-observe", "6", "Gözlem"),
    ("step-task", "7", "Bağımsız görev"),
    ("step-why", "8", "Gerekçe"),
)


def p(text: str) -> str:
    return f"<p>{escape(text.strip())}</p>"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def render(day: dict) -> str:
    filename = day["file"]
    require(filename in PAGE_RANGES, f"bilinmeyen gün dosyası: {filename}")
    catalog = lesson_catalog()
    pages = course_pages()
    index = pages.index(filename)
    prev_file = pages[index - 1]
    next_file = pages[index + 1]
    expected = list(PAGE_RANGES[filename])
    lessons = day["lessons"]
    numbers = [lesson["n"] for lesson in lessons]
    require(numbers == expected, f"{filename}: dersler {numbers}, beklenen {expected}")

    lab_ids = [lab["id"] for lab in day.get("labs", [])]
    require(tuple(lab_ids) == LAB_PAGES.get(filename, ()), f"{filename}: lablar {lab_ids}")
    project_ids = [project["id"] for project in day.get("projects", [])]
    require(tuple(project_ids) == PROJECT_PAGES.get(filename, ()), f"{filename}: projeler {project_ids}")
    if filename in VERIFY_NOTE_PAGES:
        require(len(day.get("verify_note", "").strip()) >= 80, f"{filename}: verify_note zorunlu")

    lesson_html = []
    map_rows = []
    for lesson in lessons:
        title_en, duration = catalog[lesson["n"]]
        require(len(lesson["title_tr"].strip()) >= 12, f"ders {lesson['n']} title_tr kısa")
        for key in ("need", "model", "extend", "fail", "task", "why", "observe", "trace"):
            require(len(lesson[key].strip()) >= 80, f"ders {lesson['n']} {key} kısa")
        has_code = bool(lesson.get("code", "").strip())
        has_diagram = bool(lesson.get("diagram", "").strip())
        require(has_code or has_diagram, f"ders {lesson['n']} kod veya diyagram yok")
        lesson_html.append(render_lesson(lesson, title_en, duration))
        map_rows.append(
            "<tr>"
            f"<td>{lesson['n']}</td>"
            f"<td><a href=\"#ders-{lesson['n']}\">{escape(title_en)}</a></td>"
            f"<td>{escape(duration)}</td>"
            f"<td>{escape(lesson['title_tr'])}</td>"
            "</tr>"
        )

    labs = "\n".join(render_lab(lab) for lab in day.get("labs", []))
    projects = "\n".join(render_project(project) for project in day.get("projects", []))
    verify = ""
    if day.get("verify_note"):
        verify = (
            '<div class="callout callout-verify"><div class="callout-title">'
            '<span class="badge badge-verify">[Doğrulama notu]</span></div>'
            f"{p(day['verify_note'])}</div>"
        )
    checks = "\n".join(f"<li>{escape(item)}</li>" for item in day["checklist"])
    require(len(day["checklist"]) >= 6, f"{filename}: kontrol listesi 6 maddeden kısa")
    nodes = "\n".join(
        f'<div class="flow-node {escape(node.get("kind", ""))}">{escape(node["label"])}</div>'
        for node in day["flow"]
    )

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{escape(day["title"])} | Agentic AI Engineering</title>
  <link rel="stylesheet" href="assets/css/course.css" />
</head>
<body>
  <header class="top-navbar no-print">
    <div class="navbar-inner">
      <a href="index.html" class="brand-link"><span class="brand-badge">{escape(day["badge"])}</span><span>{escape(day["title"])}</span></a>
      <div class="nav-controls">
        <select id="page-jump-select" class="nav-select" aria-label="Sayfa Seçin"></select>
        <a href="tam-kitap-baski.html" class="btn btn-primary">Tam Kitap (PDF)</a>
        <button type="button" class="btn btn-print" onclick="printCurrentPage()">Bu Sayfayı PDF Yazdır</button>
      </div>
    </div>
  </header>
  <main class="book-container">
    <article class="book-page">
      <section class="chapter-header">
        <div class="chapter-meta"><span>{escape(day["meta"])}</span><span>Ders {expected[0]}–{expected[-1]}</span></div>
        <h1>{escape(day["title"])}</h1>
        {p(day["intro"])}
      </section>
      <div class="callout callout-verify">
        <div class="callout-title"><span class="badge badge-verify">[Doğrulama notu]</span> <span class="badge badge-design">[Öğretim tasarımı]</span></div>
        <p>Bu sayfadaki kod ve açıklamalar öğretim tasarımıdır. Kütüphane arayüzleri sürümle değişebilir; çalıştırmadan önce resmi dokümantasyonla karşılaştırın. Derslerin İngilizce başlıkları kurs sayfasından alınmıştır ve kaynak rozetiyle durur.</p>
      </div>
      {verify}
      <section id="gun-haritasi">
        <h2>Günün haritası</h2>
        <div class="table-wrap"><table>
          <thead><tr><th>Ders</th><th>Kaynaktaki başlık</th><th>Süre</th><th>Bugünkü odak</th></tr></thead>
          <tbody>
          {"".join(map_rows)}
          </tbody>
        </table></div>
      </section>
      <section id="zihinsel-model">
        <h2>Bugünün kavramı nereye oturur?</h2>
        {p(day["model_lead"])}
        <div class="diagram-box"><div class="flow-diagram">{nodes}</div>
        <div class="diagram-caption">{escape(day["flow_caption"])}</div></div>
      </section>
      {"".join(lesson_html)}
      {labs}
      {projects}
      <section id="gun-sonu">
        <h2>Gün sonu kontrol listesi</h2>
        <ul>
        {checks}
        </ul>
      </section>
      <nav class="page-footer-nav no-print">
        <a href="{prev_file}" class="btn btn-outline">← Önceki</a>
        <a href="{next_file}" class="btn btn-primary">Sonraki →</a>
      </nav>
    </article>
  </main>
  <script src="assets/js/course.js"></script>
</body>
</html>
"""


def render_lesson(lesson: dict, title_en: str, duration: str) -> str:
    code = ""
    if lesson.get("code", "").strip():
        code = (
            '<div class="code-block-wrapper"><div class="code-header"><span>'
            f"{escape(lesson.get('code_name', 'ornek.py'))}</span></div><pre><code>"
            f"{escape(lesson['code'].strip())}</code></pre></div>"
        )
    diagram = ""
    if lesson.get("diagram", "").strip():
        diagram = f'<div class="diagram-box"><div class="diagram-caption">{escape(lesson["diagram"])}</div></div>'
    return f"""
<section class="lesson-card" id="ders-{lesson["n"]}" data-ders="{lesson["n"]}">
  <div class="lesson-header">
    <span class="lesson-number">DERS {lesson["n"]}</span>
    <div class="lesson-title-group">
      <div class="lesson-title-tr">{escape(lesson["title_tr"])}</div>
      <p class="lesson-title-en">{escape(title_en)}</p>
    </div>
    <span class="badge badge-duration">{escape(duration)}</span>
    <span class="badge badge-source">[Kaynak]</span>
  </div>
  <div class="lesson-body"><div class="steps-grid">
    <div class="step-box step-need"><div class="step-header"><span class="step-num">1</span> İhtiyaç</div>{p(lesson["need"])}</div>
    <div class="step-box step-model"><div class="step-header"><span class="step-num">2</span> Zihinsel model</div>{p(lesson["model"])}</div>
    <div class="step-box step-code"><div class="step-header"><span class="step-num">3</span> Minimum örnek</div>{p(lesson.get("code_lead", "En küçük çalışan sürüm aşağıdadır."))}{code}{diagram}</div>
    <div class="step-box step-extend"><div class="step-header"><span class="step-num">4</span> Genişletme</div>{p(lesson["extend"])}</div>
    <div class="step-box step-fail"><div class="step-header"><span class="step-num">5</span> Başarısızlık örneği</div>{p(lesson["fail"])}</div>
    <div class="step-box step-observe"><div class="step-header"><span class="step-num">6</span> Gözlem</div>{p(lesson["observe"])}<div class="trace-box">{escape(lesson["trace"].strip())}</div></div>
    <div class="step-box step-task"><div class="step-header"><span class="step-num">7</span> Bağımsız görev</div>{p(lesson["task"])}</div>
    <div class="step-box step-why"><div class="step-header"><span class="step-num">8</span> Gerekçe</div>{p(lesson["why"])}</div>
  </div></div>
</section>
"""


def render_lab(lab: dict) -> str:
    steps = "\n".join(f"<li>{escape(step)}</li>" for step in lab["steps"])
    return f"""
<section class="callout callout-lab" id="{escape(lab["id"])}">
  <div class="callout-title"><span class="badge badge-lab">[Uygulama Laboratuvarı]</span> {escape(lab["title"])}</div>
  {p(lab["goal"])}
  <ol>{steps}</ol>
  <div class="trace-box">{escape(lab["proof"].strip())}</div>
</section>
"""


def render_project(project: dict) -> str:
    require(len(project["delivery"]) >= 10, f"{project['id']} teslim tablosu 10 satırdan kısa")
    rows = "\n".join(
        f"<tr><td>{escape(row['item'])}</td><td>{escape(row['content'])}</td></tr>"
        for row in project["delivery"]
    )
    return f"""
<section id="{escape(project["id"])}">
  <h2><span class="badge badge-project">[Proje]</span> {escape(project["title"])}</h2>
  {p(project["lead"])}
  <div class="table-wrap"><table>
    <thead><tr><th>Teslim</th><th>Bu projede ne göstereceksin</th></tr></thead>
    <tbody>
    {rows}
    </tbody>
  </table></div>
  {p(project["criterion"])}
</section>
"""


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) != 2:
        raise SystemExit("kullanim: python scripts/render_day.py <json-veya-klasor>")
    target = Path(sys.argv[1])
    files = sorted(target.glob("*.json")) if target.is_dir() else [target]
    for path in files:
        day = json.loads(path.read_text(encoding="utf-8"))
        html = render(day)
        out = ROOT / day["file"]
        out.write_text(html, encoding="utf-8", newline="\n")
        print(f"{day['file']} {out.stat().st_size} bayt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

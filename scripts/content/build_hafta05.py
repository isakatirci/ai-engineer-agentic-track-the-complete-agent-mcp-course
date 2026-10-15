# -*- coding: utf-8 -*-
"""Hafta 5 içerik üretici. Çalışınca scripts/content/hafta05-gun0N.json yazar."""

from __future__ import annotations

import json
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent
FORBIDDEN = re.compile(
    r"TODO|TBD|FIXME|lorem|devamı gelecek|burada .{0,40} olacak",
    re.IGNORECASE,
)

NARRATIVE = ("need", "model", "extend", "fail", "task", "why", "observe", "trace")
DELIVERY = (
    "Problem tanımı",
    "Mimari açıklama",
    "Çalıştırma talimatı",
    "Örnek yapılandırma",
    "Başarılı senaryo",
    "Başarısız senaryo",
    "Test seti",
    "Trace kanıtı",
    "Maliyet değerlendirmesi",
    "Bilinen sınırlamalar",
)


def lesson(n, title_tr, code_name, code_lead, code, **fields):
    data = {
        "n": n,
        "title_tr": title_tr,
        "code_name": code_name,
        "code_lead": code_lead,
        "code": code.strip("\n"),
    }
    data.update(fields)
    return data


def day(**kwargs):
    return kwargs


def check_text(label: str, text: str, minimum: int) -> None:
    body = text.strip()
    if len(body) < minimum:
        raise SystemExit(f"KISA {label}: {len(body)} < {minimum}")
    if FORBIDDEN.search(body):
        raise SystemExit(f"YASAK {label}: {FORBIDDEN.search(body).group(0)}")


def validate(page: dict) -> None:
    check_text(page["file"] + " intro", page["intro"], 200)
    check_text(page["file"] + " model_lead", page["model_lead"], 200)
    if len(page["checklist"]) < 6:
        raise SystemExit(page["file"] + " checklist")
    if page["file"] == "hafta05-gun05.html":
        note = page.get("verify_note", "")
        check_text(page["file"] + " verify_note", note, 80)
        for phrase in ("AutoGen Agent Creator", "Multi-Framework Agent Loop"):
            if phrase not in note:
                raise SystemExit(f"verify_note eksik ifade: {phrase}")
    elif page.get("verify_note"):
        raise SystemExit(page["file"] + " verify_note olmamalı")
    for item in page["lessons"]:
        check_text(f"{item['n']} title", item["title_tr"], 12)
        for key in NARRATIVE:
            check_text(f"{item['n']} {key}", item[key], 700)
        lines = item["code"].strip("\n").splitlines()
        if len(lines) < 25:
            raise SystemExit(f"{item['n']} code {len(lines)} satır")
        check_text(f"{item['n']} code", item["code"], 25)
    for lab in page.get("labs", []):
        if len(lab["steps"]) < 5:
            raise SystemExit(lab["id"] + " steps")
        check_text(lab["id"] + " proof", lab["proof"], 200)
    expected_projects = {
        "hafta05-gun05.html": ["proje-7", "proje-agent-loop"],
    }.get(page["file"], [])
    got = [project["id"] for project in page.get("projects", [])]
    if got != expected_projects:
        raise SystemExit(f"{page['file']} projeler {got}")
    for project in page.get("projects", []):
        names = [row["item"] for row in project["delivery"]]
        if names != list(DELIVERY):
            raise SystemExit(f"{project['id']} teslim adları {names}")
        for row in project["delivery"]:
            check_text(project["id"] + " " + row["item"], row["content"], 120)

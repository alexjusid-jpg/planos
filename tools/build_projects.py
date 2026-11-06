#!/usr/bin/env python3
"""Genera projects.json para la página de inicio (lista de proyectos + archivos de cada ZIP).

Uso:  python3 tools/build_projects.py
Para agregar un proyecto nuevo: sumar una entrada en PROJECTS y volver a correr el script.
"""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["he", "en", "es"]

PROJECTS = [
    {"id": "yoseftal_rev08", "main": True,
     "name": {"he": "יוספטל – מחלקת אשפוז", "en": "Yoseftal – Hospital ward", "es": "Yoseftal – Pabellón de internación"},
     "sub": {"he": "קריאת אחות · REV08", "en": "Nurse call · REV08", "es": "Llamada de enfermería · REV08"}},
    {"id": "migdalei", "main": True,
     "name": {"he": "מגדלי ים התיכון – דיור מוגן", "en": "Migdalei Yam HaTikhon – Assisted living", "es": "Migdalei Yam HaTijon – Departamentos tutelados"},
     "sub": {"he": "קריאת אחות", "en": "Nurse call", "es": "Llamada de enfermería"}},
    {"id": "nesher", "main": True,
     "name": {"he": "נשר – מרכז רפואי גריאטרי", "en": "Nesher – Geriatric medical center", "es": "Nesher – Centro médico geriátrico"},
     "sub": {"he": "קריאת אחות", "en": "Nurse call", "es": "Llamada de enfermería"}},
    {"id": "yoseftal_rev05", "main": False, "name": {"he": "יוספטל · REV05", "en": "Yoseftal · REV05", "es": "Yoseftal · REV05"}, "sub": {}},
    {"id": "yoseftal", "main": False, "name": {"he": "יוספטל · גרסה ראשונה", "en": "Yoseftal · first version", "es": "Yoseftal · primera versión"}, "sub": {}},
    {"id": "yoseftal_ex1", "main": False, "name": {"he": "יוספטל · דוגמה 1", "en": "Yoseftal · example 1", "es": "Yoseftal · ejemplo 1"}, "sub": {}},
    {"id": "yoseftal_ex2", "main": False, "name": {"he": "יוספטל · דוגמה 2", "en": "Yoseftal · example 2", "es": "Yoseftal · ejemplo 2"}, "sub": {}},
]

files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split("\n")
files = [f for f in files if f]
fset = set(files)
size = lambda f: os.path.getsize(os.path.join(ROOT, f)) if os.path.exists(os.path.join(ROOT, f)) else 0


def refs(html_path):
    """Archivos de otras carpetas que la página usa (../../carpeta/...)."""
    out = set()
    try:
        txt = open(os.path.join(ROOT, html_path), encoding="utf-8", errors="ignore").read()
    except OSError:
        return out
    base = os.path.dirname(html_path)
    for m in re.findall(r'["\'(](\.\./[^"\')?#]+)', txt):
        p = os.path.normpath(os.path.join(base, m))
        if p in fset:
            out.add(p)
    return out


out = []
for p in PROJECTS:
    pid = p["id"]
    mine = [f for f in files if f.startswith(pid + "/")]
    has_lang = all(any(f.startswith(f"{pid}/{l}/") for f in mine) for l in LANGS)
    entry = {k: p[k] for k in ("id", "main", "name", "sub")}
    cov = {"yoseftal_rev08": "Yoseftal", "migdalei": "Migdalei", "nesher": "Nesher"}.get(pid)
    if cov: entry["cover"] = f"covers/Plano de {cov}.pdf"
    entry["open"] = {l: (f"{pid}/{l}/" if has_lang else f"{pid}/") for l in LANGS}
    zips = {}
    for l in (LANGS if has_lang else ["all"]):
        others = [f"{pid}/{o}/" for o in LANGS if o != l] if has_lang else []
        sel = [f for f in mine if not any(f.startswith(o) for o in others)]
        extra = set()
        for f in sel:
            if f.endswith(".html"):
                extra |= refs(f)
        sel = sorted(set(sel) | extra)
        zips[l] = {"files": sel, "bytes": sum(size(f) for f in sel)}
    if not has_lang:
        zips = {l: zips["all"] for l in LANGS}
    entry["zip"] = zips
    out.append(entry)

json.dump(out, open(os.path.join(ROOT, "projects.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for e in out:
    print(e["id"], {l: round(z["bytes"] / 1e6, 1) for l, z in e["zip"].items()}, "MB")

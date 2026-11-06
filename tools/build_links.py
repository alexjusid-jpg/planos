#!/usr/bin/env python3
"""Genera "Mis links – Planos Máster" (uso interno de Alex): covers/Mis links Planos Master.html (+ PDF con build en playwright).
Uso: python3 tools/build_links.py
"""
import os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = "https://alexjusid-jpg.github.io/planos/"
DRIVE = "https://drive.google.com/drive/folders/11MzCqTsBpkAmVZZTIBMpuKlKnmzBclsg"

GROUPS = [
 ("Mis herramientas · הכלים שלי · My tools", "Solo para mí — no compartir", [
   ("🏠 Inicio – todos los proyectos", "דף הבית – כל הפרויקטים", S),
   ("📁 Google Drive – App Planos Máster", "גוגל דרייב", DRIVE),
   ("💻 Código (GitHub)", "קוד", "https://github.com/alexjusid-jpg/planos"),
   ("⚙️ Activar envío automático (instrucciones)", "הוראות", "https://github.com/alexjusid-jpg/planos/blob/main/tools/apps_script/INSTRUCCIONES.md")]),
 ("Formularios · טפסים · Forms", "Se pueden mandar a Orad", [
   ("📝 Solicitud de proyecto nuevo – עברית", "בקשת פרויקט חדש", S + "solicitud/?lang=he"),
   ("📝 New project request – English", "", S + "solicitud/?lang=en"),
   ("📝 Solicitud de proyecto nuevo – Español", "", S + "solicitud/?lang=es"),
   ("✏️ Actualización / cambio – Yoseftal", "עדכון מידע – יוספטל", S + "solicitud/?mode=update&p=Yoseftal&lang=he"),
   ("✏️ Actualización / cambio – Migdalei", "עדכון מידע – מגדלי ים התיכון", S + "solicitud/?mode=update&p=Migdalei&lang=he"),
   ("✏️ Actualización / cambio – Nesher", "עדכון מידע – נשר", S + "solicitud/?mode=update&p=Nesher&lang=he")]),
 ("Yoseftal · יוספטל", "Se puede compartir", [
   ("▶ 3D – עברית", "", S + "yoseftal_rev08/he/"), ("▶ 3D – English", "", S + "yoseftal_rev08/en/"), ("▶ 3D – Español", "", S + "yoseftal_rev08/es/"),
   ("📄 Plano de Yoseftal (PDF)", "", S + "covers/Plano%20de%20Yoseftal.pdf"),
   ("📊 Presentación EN", "", S + "yoseftal_rev08/assets/Yoseftal_SmartRoom_Presentation_REV08_EN.pptx"),
   ("📊 מצגת עברית", "", S + "yoseftal_rev08/assets/Yoseftal_SmartRoom_Presentation_REV08_HE.pptx")]),
 ("Migdalei Yam HaTikhon · מגדלי ים התיכון", "Se puede compartir", [
   ("▶ 3D – עברית", "", S + "migdalei/he/"), ("▶ 3D – English", "", S + "migdalei/en/"), ("▶ 3D – Español", "", S + "migdalei/es/"),
   ("📄 Plano de Migdalei (PDF)", "", S + "covers/Plano%20de%20Migdalei.pdf"),
   ("📊 Presentación EN", "", S + "migdalei/en/presentation_EN.pptx"), ("📊 מצגת עברית", "", S + "migdalei/he/presentation_HE.pptx"),
   ("📊 Presentación ES", "", S + "migdalei/es/presentacion_ES.pptx")]),
 ("Nesher · נשר", "En preparación", [
   ("▶ Planos – ES · EN · עב", "", S + "nesher/"), ("📄 Plano de Nesher (PDF)", "", S + "covers/Plano%20de%20Nesher.pdf")]),
]

rows = []
for title, note, links in GROUPS:
    items = "".join(f'<li><a href="{html.escape(u)}"><b>{html.escape(t)}</b>{f"<span>{html.escape(h)}</span>" if h else ""}<small>{html.escape(u)}</small></a></li>' for t, h, u in links)
    rows.append(f'<section><h2>{html.escape(title)}</h2><p class="n">{html.escape(note)}</p><ul>{items}</ul></section>')

page = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow"><title>Mis links · Planos Máster</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700&family=Heebo:wght@400;600;800&family=IBM+Plex+Mono:wght@500&display=swap">
<style>:root{{--ink:#1C2230;--muted:#667080;--line:#E3E6EA;--accent:#C9662A;--warm:#FAF7F3;color-scheme:light}}*{{box-sizing:border-box}}
body{{margin:0;background:#fff;color:var(--ink);font:15px/1.4 Heebo,system-ui,Arial,sans-serif}}
.p{{max-width:860px;margin:0 auto;padding:max(18px,env(safe-area-inset-top,0px)) 18px 40px}}
.top{{font:500 12px "IBM Plex Mono",monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);border-bottom:1px solid var(--line);padding-bottom:10px;display:flex;justify-content:space-between}}
h1{{font:700 clamp(30px,6vw,46px)/1.05 Fraunces,Georgia,serif;margin:18px 0 4px}}.sub{{color:var(--muted);margin:0 0 6px}}
.tip{{background:var(--warm);border:1px solid var(--line);border-radius:10px;padding:10px 14px;font-size:14px;margin:14px 0 4px}}
section{{margin-top:22px}}h2{{font:800 19px Heebo,sans-serif;margin:0;padding-bottom:4px;border-bottom:2px solid var(--ink)}}
.n{{font:500 11px "IBM Plex Mono",monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin:6px 0 8px}}
ul{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:8px}}
a{{display:block;text-decoration:none;color:var(--ink);border:1px solid var(--line);border-radius:10px;padding:10px 12px;min-height:58px;background:#fff}}
a:hover{{border-color:var(--accent)}}a b{{display:block;font-weight:600}}a span{{display:block;direction:rtl;text-align:right;color:#4A515B;font-size:14px}}
a small{{display:block;font:500 10px "IBM Plex Mono",monospace;color:var(--muted);word-break:break-all;margin-top:3px}}
footer{{margin-top:30px;border-top:1px solid var(--line);padding-top:10px;font:500 11px "IBM Plex Mono",monospace;color:var(--muted)}}
@media print{{@page{{size:A4;margin:10mm}}.p{{padding:0}}section{{break-inside:avoid}}}}</style></head><body><div class="p">
<div class="top"><span>Planos Máster · uso interno</span><span>Alex Jusid</span></div>
<h1>Mis links</h1><p class="sub">Todos los links de la app de planos en un solo lugar · כל הקישורים במקום אחד · All links in one place</p>
<div class="tip">📱 Para tenerlo como ícono en el iPhone: abrir el link en <b>Safari</b> → botón Compartir ⬆ → <b>Agregar a pantalla de inicio</b>.</div>
{''.join(rows)}
<footer>Actualizado 06.11.2026 · Planos Máster · Alex Jusid</footer></div></body></html>"""
os.makedirs(os.path.join(ROOT, "covers"), exist_ok=True)
open(os.path.join(ROOT, "covers", "Mis links Planos Master.html"), "w", encoding="utf-8").write(page)
print("ok")

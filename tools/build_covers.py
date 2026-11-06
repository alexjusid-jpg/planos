#!/usr/bin/env python3
"""Genera la portada de cada proyecto: "Plano de <Proyecto>.html" (archivo único, se abre sin internet,
con imagen, datos del proyecto, links y QR). Salida: covers/ (también se publica en GitHub Pages).

Uso: python3 tools/build_covers.py
"""
import base64, io, os, html
import qrcode, qrcode.image.svg
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://alexjusid-jpg.github.io/planos/"
AUTHOR = "Alex Jusid"
DIST = ("Orad Systems", "אורד מערכות")

PROJECTS = [
    {"key": "Yoseftal", "slug": "yoseftal_rev08", "img": "yoseftal_rev08/assets/renders/corridor.jpg",
     "en": "Yoseftal Medical Center", "he": "המרכז הרפואי יוספטל",
     "tag_en": "Hospital ward · Nurse call system", "tag_he": "מחלקת אשפוז · מערכת קריאת אחות",
     "date": "2026-11-06", "rev": "REV08",
     "open": {"he": "yoseftal_rev08/he/", "en": "yoseftal_rev08/en/", "es": "yoseftal_rev08/es/"},
     "pres": [("Presentation · EN", "yoseftal_rev08/assets/Yoseftal_SmartRoom_Presentation_REV08_EN.pptx"),
              ("מצגת · עברית", "yoseftal_rev08/assets/Yoseftal_SmartRoom_Presentation_REV08_HE.pptx")]},
    {"key": "Migdalei", "slug": "migdalei", "img": "migdalei/renders/r_lobby.jpg",
     "en": "Migdalei Yam HaTikhon", "he": "מגדלי ים התיכון",
     "tag_en": "Assisted living · Nurse call system", "tag_he": "דיור מוגן · מערכת קריאת אחות",
     "date": "2026-10-24", "rev": "",
     "open": {"he": "migdalei/he/", "en": "migdalei/en/", "es": "migdalei/es/"},
     "pres": [("Presentation · EN", "migdalei/en/presentation_EN.pptx"), ("מצגת · עברית", "migdalei/he/presentation_HE.pptx"),
              ("Presentación · ES", "migdalei/es/presentacion_ES.pptx")]},
    {"key": "Nesher", "slug": "nesher", "img": "nesher/assets/plan/L01.jpg",
     "en": "Nesher Geriatric Medical Center", "he": "מרכז רפואי גריאטרי נשר",
     "tag_en": "Geriatric center · Nurse call system", "tag_he": "מרכז גריאטרי · מערכת קריאת אחות",
     "date": "2026-11-02", "rev": "",
     "open": {"he": "nesher/", "en": "nesher/", "es": "nesher/"}, "pres": []},
]


def img64(path):
    im = Image.open(os.path.join(ROOT, path)).convert("RGB")
    im.thumbnail((1400, 900))
    b = io.BytesIO(); im.save(b, "JPEG", quality=72, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def qr_svg(url):
    q = qrcode.QRCode(border=1, box_size=10); q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m)
    rects = "".join(f'<rect x="{x}" y="{y}" width="1" height="1"/>' for y, row in enumerate(m) for x, v in enumerate(row) if v)
    return f'<svg viewBox="0 0 {n} {n}" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges" role="img" aria-label="QR"><rect width="{n}" height="{n}" fill="#fff"/><g fill="#1F2630">{rects}</g></svg>'


def fmt(d):
    y, m, dd = d.split("-")
    return f"{dd}.{m}.{y}"


TPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>Plano de {key} · {en} · {he}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Heebo:wght@400;500;700;800&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
:root{{--ink:#1C2230;--muted:#667080;--line:#E3E6EA;--paper:#FFFFFF;--warm:#FAF7F3;--accent:#C9662A;--navy:#27306B;
  --serif:"Fraunces",Georgia,serif;--sans:"Heebo",system-ui,Arial,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace;color-scheme:light}}
*{{box-sizing:border-box}}
html,body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 var(--sans)}}
.page{{max-width:1080px;margin:0 auto;padding:max(18px,env(safe-area-inset-top,0px)) max(18px,env(safe-area-inset-right,0px)) 40px max(18px,env(safe-area-inset-left,0px))}}
.top{{display:flex;justify-content:space-between;align-items:center;font:500 12px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--muted);padding-bottom:14px;border-bottom:1px solid var(--line)}}
.top b{{color:var(--accent);font-weight:500}}
.hero{{position:relative;margin-top:18px;border-radius:14px;overflow:hidden;aspect-ratio:16/8;background:var(--warm)}}
.hero img{{width:100%;height:100%;object-fit:cover;display:block}}
.hero::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,0) 45%,rgba(255,255,255,.92) 100%)}}
.badge{{position:absolute;top:14px;inset-inline-start:14px;z-index:2;background:#fff;border-radius:999px;padding:6px 14px;font:500 12px var(--mono);letter-spacing:.1em;text-transform:uppercase;box-shadow:0 2px 12px rgba(0,0,0,.12)}}
.badge i{{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--accent);margin-inline-end:8px;vertical-align:1px}}
.titles{{display:grid;grid-template-columns:1fr 1fr;gap:10px 40px;align-items:end;margin-top:-64px;position:relative;z-index:3;padding:0 6px}}
h1{{font:700 clamp(30px,5vw,54px)/1.02 var(--serif);margin:0;letter-spacing:-.01em}}
.he{{font:800 clamp(28px,4.6vw,50px)/1.08 var(--sans);margin:0;direction:rtl;text-align:right}}
.tag{{color:var(--muted);font-size:15px;margin-top:6px}}
.tag.r{{direction:rtl;text-align:right}}
.meta{{display:grid;grid-template-columns:repeat(3,1fr);margin:30px 0 0;border-top:2px solid var(--ink);border-bottom:1px solid var(--line)}}
.meta div{{padding:16px 14px}}.meta div+div{{border-inline-start:1px solid var(--line)}}
.meta dt{{font:500 11px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}}
.meta dt span{{display:block;font:500 12px var(--sans);letter-spacing:0;text-transform:none;direction:rtl}}
.meta dd{{margin:6px 0 0;font:700 21px/1.2 var(--serif)}}
.meta dd small{{display:block;font:500 14px var(--sans);color:var(--muted);direction:rtl}}
.excl{{display:inline-block;margin-top:6px;font:500 11px var(--mono);letter-spacing:.1em;color:#fff;background:var(--accent);padding:2px 8px;border-radius:3px;text-transform:uppercase}}
.go{{display:grid;grid-template-columns:1fr auto;gap:26px;margin-top:30px;align-items:start}}
h2{{font:500 12px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 10px}}
.btns{{display:flex;flex-wrap:wrap;gap:10px}}
a.b{{display:inline-flex;align-items:center;gap:10px;text-decoration:none;font:700 16px var(--sans);color:#fff;background:var(--ink);padding:14px 20px;border-radius:10px;min-height:52px}}
a.b.alt{{background:#fff;color:var(--ink);border:1.5px solid var(--ink)}}
a.b.pres{{background:var(--warm);color:var(--ink);border:1px solid var(--line);font-weight:600}}
a.b:hover{{transform:translateY(-1px)}}
.url{{font:500 13px var(--mono);color:var(--muted);margin-top:10px;word-break:break-all}}
.url a{{color:var(--navy)}}
.qr{{width:150px;text-align:center;font:500 11px var(--mono);color:var(--muted);letter-spacing:.08em}}
.qr svg{{width:150px;height:150px;display:block;border:1px solid var(--line);border-radius:10px;padding:8px;margin-bottom:6px}}
.sec{{margin-top:26px}}
footer{{margin-top:40px;padding-top:14px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px;font:500 12px var(--mono);color:var(--muted);letter-spacing:.06em}}
@media (max-width:720px){{.titles{{grid-template-columns:1fr;margin-top:-40px}}.he,.tag.r{{text-align:right}}.hero{{aspect-ratio:4/3}}
  .meta{{grid-template-columns:1fr}}.meta div+div{{border-inline-start:0;border-top:1px solid var(--line)}}.go{{grid-template-columns:1fr}}.qr{{width:auto;display:flex;gap:12px;align-items:center;text-align:start}}.qr svg{{width:110px;height:110px;margin:0}}a.b{{flex:1 1 100%;justify-content:center}}}}
@media print{{@page{{size:A4;margin:12mm}}.page{{padding:0;max-width:none}}.hero{{aspect-ratio:16/7.5}}.titles{{margin-top:-46px}}a.b{{padding:10px 16px;min-height:0;font-size:14px}}.meta dd{{font-size:18px}}.go{{margin-top:20px}}.sec{{margin-top:16px}}footer{{margin-top:22px}}}}
</style>
</head>
<body>
<div class="page">
  <div class="top"><span>Plano de {key}</span><span><b>Nurse call</b> · ACE BG · Advantecnia</span></div>
  <div class="hero"><span class="badge"><i></i>{badge}</span><img src="{img}" alt="{en}"></div>
  <div class="titles">
    <div><h1>{en}</h1><div class="tag">{tag_en}</div></div>
    <div><p class="he">{he}</p><div class="tag r">{tag_he}</div></div>
  </div>
  <dl class="meta">
    <div><dt>Prepared by<span>הוכן ע״י · Elaborado por</span></dt><dd>{author}<small>{author_he}</small></dd></div>
    <div><dt>Date<span>תאריך · Fecha</span></dt><dd>{date}</dd></div>
    <div><dt>Exclusive distribution<span>הפצה בלעדית · Distribución exclusiva</span></dt><dd>{dist}<small>{dist_he}</small></dd><span class="excl">Exclusive · בלעדי</span></div>
  </dl>
  <div class="go">
    <div>
      <h2>Open the 3D plans · פתיחת התוכניות · Abrir los planos</h2>
      <div class="btns">
        <a class="b" href="{u_he}">▶ פתיחה בעברית</a>
        <a class="b alt" href="{u_en}">Open in English</a>
        <a class="b alt" href="{u_es}">Abrir en español</a>
      </div>
      <div class="url">🔗 <a href="{u_main}">{u_main}</a></div>
      {pres}
    </div>
    <div class="qr">{qr}SCAN · סרקו · ESCANEAR</div>
  </div>
  <footer><span>© {year} {author} · {dist}</span><span>{key} · {rev_s}{date}</span></footer>
</div>
</body>
</html>
"""

os.makedirs(os.path.join(ROOT, "covers"), exist_ok=True)
for p in PROJECTS:
    u = {k: SITE + v for k, v in p["open"].items()}
    pres = ""
    if p["pres"]:
        pres = '<div class="sec"><h2>Presentation · מצגת · Presentación</h2><div class="btns">' + "".join(
            f'<a class="b pres" href="{SITE + f}">📊 {html.escape(t)}</a>' for t, f in p["pres"]) + "</div></div>"
    out = TPL.format(key=p["key"], en=html.escape(p["en"]), he=html.escape(p["he"]), tag_en=p["tag_en"], tag_he=p["tag_he"],
                     img=img64(p["img"]), badge=("3D · " + p["rev"]) if p["rev"] else "3D interactive",
                     author=AUTHOR, author_he="", date=fmt(p["date"]), dist=DIST[0], dist_he=DIST[1],
                     u_he=u["he"], u_en=u["en"], u_es=u["es"], u_main=u["he"], pres=pres, qr=qr_svg(u["he"]),
                     year=p["date"][:4], rev_s=(p["rev"] + " · ") if p["rev"] else "")
    fn = os.path.join(ROOT, "covers", f"Plano de {p['key']}.html")
    open(fn, "w", encoding="utf-8").write(out)
    print(fn, round(len(out) / 1024), "KB")

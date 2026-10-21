# Migdalei Yam a Tijon – Assisted living – ACE BG / Advantecnia nurse call

Rev. B · 15/10/2026 · Telab International · on architectural plan L5 (typical floor)

## Files
| File | What it is | How to open |
|---|---|---|
| `plans_2D_EN.pdf` | 12 A1 sheets (incl. photorealistic renders): typical floor (nurse call and wiring), devices with photos, client marks on plan L2, 1-bedroom apt., 2-bedroom apt., ground floor with nurse desk, riser diagram, bill of materials and 3D views | Any PDF reader; print on A1 |
| `presentation_EN.pptx` | 14-slide presentation | PowerPoint, Keynote, Google Slides |
| `walkthrough_EN.mp4` | Photorealistic walkthrough (360° real-light images) | Any player |
| 360° tour | https://alexjusid-jpg.github.io/planos/migdalei/tour360/?lang=en (walk the building with 360° photos) | Browser |
| `guided_tour_EN.mp4` | Photorealistic guided tour (real-light renders) | Any player |
| `drawing_CAD_EN.dxf` | CAD: typical floor and GF with layers per system; devices as blocks with ID / DESCRIPCION / ALTURA_M / CODIGO | AutoCAD → Save as → **DWG** |
| `model_BIM_EN.ifc` | IFC4 BIM: GF + 8 floors with walls, windows, furniture, devices and cables | **Revit**: Open → IFC → save as **RVT** |
| `viewer_3d_EN.html` | 3D viewer with **🚶 Walk**, **Go to…** and **📄 Documents** (view and download every file) | Online: https://alexjusid-jpg.github.io/planos/migdalei/en/ |

## The building
- 8 identical floors with 4 apartments: x01 and x02 one-bedroom (2 bathrooms), x03 and x04 two-bedroom (2 bathrooms). 32 apartments.
- Ground floor: reception with the **nurse desk** and Grandstream Android phone (PoE straight to the switch; alarm red, presence green, doctor blue, voice orange); rack with Buslogic Premium server and D-Link DES-1210-28P PoE switch; 2 public toilets. *Proposed GF layout: to be adjusted with the architect's plan.*

## Devices
- Tablet at the door of each apartment (iPad / Android): 32.
- Voice call panel with buttons ACE82182451 in the living room and each bedroom (pear next to the bed): 80.
- Pull-cords ACE40320303W at the toilet and shower of every bathroom: 138 (includes the 10 public toilets).
- Corridor light ACE41020309 above each public toilet: 10.
- One LCom ACE71610003 per apartment and per public toilet; 2 BoxCom ACE70810000 on the ceiling and a D-Link DES-1210-28P PoE switch (24 ports) in each floor rack; Buslogic Premium server on GF.

## Wiring (all Cat6 / Cat7 and PoE)
Green: Cat6 radial from each device to the LCom · Orange: chain LCom → LCom → ceiling BoxCom · Red: switch → riser → GF server.
Preliminary quantities: validate with Advantecnia and on site.

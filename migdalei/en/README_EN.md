# Migdalei Yam a Tijon – Assisted living – ACE BG / Advantecnia nurse call

Preliminary design Rev. A · 12/10/2026 · Telab International

## Contents
| File | What it is | How to open |
|---|---|---|
| `plans_2D_EN.pdf` | 7 A1 sheets: typical floor equipment and wiring (1:60), type A and type B apartments with heights, GF + 6 floors vertical diagram, topology and bill of materials, 3D views | Any PDF reader; print on A1 |
| `drawing_CAD_EN.dxf` | CAD drawing of the typical floor with layers per system; cables as 3D polylines; devices as blocks with ID / DESCRIPCION / ALTURA_M / CODIGO attributes | AutoCAD, BricsCAD, DraftSight. For **DWG**: open in AutoCAD → Save as → DWG |
| `model_BIM_EN.ifc` | IFC4 BIM model of the building: GF + 6 floors with walls, doors, windows, furniture, devices and cables | **Revit**: File → Open → IFC, then save as **RVT** |
| `viewer_3d_EN.html` | 3D viewer: equipment / wiring, tour, views, **Walk mode** and **Go to…** each device | Double-click (needs internet). Online version: https://claude.ai/artifact/4L9gAG1KqRfpgipCaP8ry9 |
| `walkthrough_EN.mp4` | Walkthrough video with English captions | Any player |
| `presentation_EN.pptx` | 11-slide presentation | PowerPoint, Keynote, Google Slides |
| `renders/` | 3D images | Any image viewer |
| `fuentes/` | Scripts that generate everything from `model.json` | Python 3 + Node |

## How to walk in the 3D viewer
1. **🚶 Walk** button: you stand in the corridor at eye height.
2. Computer: arrows or W / S to move forward and back, A / D to step sideways, ← → or Q / E to turn, drag the mouse to look around.
3. Phone or tablet: on-screen ▲ ▼ ⟲ ⟳ buttons, and drag with your finger to look around.
4. Walls can't be crossed: go in through the doors.
5. **Go to…**: pick a device (e.g. D1-TAB) and you stand in front of it, with its card and ACE code.

## Building
- Ground floor: reception with the nurse desk (phone ACE52190200) and the main rack with server ACE51010103.
- Floors 1 to 6: 6 apartments per floor, 3 type A and 3 type B mixed (36 in total). Comms room next to the lift.
- Type A: living room with open kitchen, main bedroom with en-suite (shower + toilet), bedroom 2, guest bathroom with shower, hall and storage.
- Type B: living room with open kitchen, one bedroom and one bathroom with shower.
- Residential furniture (not hospital).

## Devices per apartment
Android tablet in the living room (call and voice) · voice call ACE82182451 in the main bedroom · pull-cords ACE40320303W at toilet and shower (1.85 m) · presence / cancel next to the door (optional) · LCom ACE71610003 in the hall ceiling. No corridor light.

## Wiring (all Cat6 / Cat7 and PoE)
- **Green**: Cat6 radial from each device to the apartment LCom.
- **Orange**: LCom → LCom → LCom → Buscomm ACE70810000 (2 Buscomm per floor).
- **Red**: Buscomm → floor PoE switch ACEUCM6302 → riser → GF server.
- Calls reach the nurse desk as voice or as an alarm.

## How to modify
1. Edit `fuentes/model_mig.py` (layout, furniture, devices) and run `python3 model_mig.py`.
2. Plans: `python3 plan_mig.py`. CAD / BIM: `python3 export_mig.py`. Viewer: `python3 build_viewer_mig.py`.
3. English and Hebrew texts: `fuentes/i18n/*.py` → regenerate `i18n_mig.json`.

## To verify
Preliminary quantities: validate with Advantecnia and on site.

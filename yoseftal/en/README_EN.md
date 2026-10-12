# Inpatient ward – Nurse call system ACE BG / Advantecnia

Preliminary design Rev. A · 12/10/2026 · Telab International

## Contents
| File | What it is | How to open it |
|---|---|---|
| `plans_2D_EN.pdf` | 7 A1 sheets: equipment plan and wiring plan (1:50), typical room with elevations, toilets and nurse station, topology + bill of materials, 3D views | Any PDF reader; print on A1 to keep the scale |
| `drawing_CAD_EN.dxf` | CAD drawing with layers per system; cables are 3D polylines at real height; devices are blocks with ID / DESCRIPTION / HEIGHT / ACE CODE attributes | AutoCAD, BricsCAD, DraftSight. For **DWG**: open in AutoCAD → Save As → DWG |
| `model_BIM_EN.ifc` | IFC4 BIM model: walls, doors, windows, furniture, sanitary ware, Advantecnia devices and cable segments | **Revit**: File → Open → IFC (or Insert → Link IFC), then save as **RVT** |
| `viewer_3d_EN.html` | Interactive 3D viewer: equipment / wiring modes, walkthrough, corridor-light simulation, device card on click | Double-click (needs internet for the 3D library) |
| `walkthrough_EN.mp4` | Walkthrough video with English captions | Any video player |
| `presentation_EN.pptx` | 11-slide presentation | PowerPoint, Keynote, Google Slides |
| `renders/` | High-resolution 3D images | Any image viewer |

## Layout
- Entrance at the east end of the corridor. Doors from the entrance: P1 Room 1 · P2 Room 2 · P3 Office · P4 Room 3 · P5 Room 4. In every room the door comes first and the 3 beds follow, heads against the side wall.
- Toilet block opposite Room 1: the accessible WC (toilet + shower) next to the block entrance, then the patient WC, then the staff WC.
- Nurse station opposite the office, with its own door; desk against the corridor wall (window): PC / phone on the wall side, the nurse faces the corridor and the TV. Comms rack at the far end of the corridor.

## Wiring
- **Radial in each room**: every device (bed call, presence, corridor light, pull-cord) has its own cable to the room's 24-pin board (ECV169).
- **Chain**: each 24-pin board connects to the next with KNX bus 2x2x0.8 mm LH EIBBUS; the last board connects to the SmartHub (Raspberry Pi).
- **Cat6 / Cat7 only** from SmartHub → switch → server, and to the nurse PC or desk phone and the TV. No room has a Cat6/Cat7 connection.
- **PoE**: boards and call devices are powered over PoE. 230 V only at the rack (switch, server, SmartHub), PC / phone and TV.
- Colours: green = bus and radial call cabling · red = Cat6/Cat7 · blue = 230 V.

## ACE BG accessories
Bed call ACE41220316 · toilet/shower pull-cord ACE40320303 · presence/cancel ACE80081001 · corridor indicator light ACE41020309 · desk phone ACE52190200 · PC/monitor ACE52040208 · server ACE51010103 · switch ACEUCM6302 · ceiling converter board (24-pin ECV169).

## To verify
Confirm with Advantecnia the maximum number of boards per bus line and the total bus length. Quantities are preliminary.

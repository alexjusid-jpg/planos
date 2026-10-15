# Migdalei Yam a Tijon – Vivienda tutelada – Llamada de enfermería ACE BG / Advantecnia

Rev. B · 15/10/2026 · Telab International · sobre el plano de arquitectura L5 (piso tipo)

## Archivos
| Archivo | Qué es | Cómo se abre |
|---|---|---|
| `planos_2D_ES.pdf` | 9 láminas A1: piso tipo (llamada y cableado), depto. 1 habitación, depto. 2 habitaciones, planta baja con desk de enfermería, esquema vertical, lista de materiales y vistas 3D | Cualquier lector PDF; imprimir en A1 |
| `presentacion_ES.pptx` | Presentación de 11 diapositivas | PowerPoint, Keynote, Google Slides |
| `recorrido_ES.mp4` | Video del recorrido con leyendas | Cualquier reproductor |
| `plano_CAD_ES.dxf` | CAD: piso tipo y PB con capas por sistema; equipos como bloques con ID / DESCRIPCION / ALTURA_M / CODIGO | AutoCAD → Guardar como → **DWG** |
| `modelo_BIM_ES.ifc` | BIM IFC4: PB + 8 pisos con muros, ventanas, muebles, equipos y cables | **Revit**: Abrir → IFC → guardar como **RVT** |
| `visor_3d_ES.html` | Visor 3D con **🚶 Caminar**, **Ir a…** y **📄 Documentos** (ver y bajar todos los archivos) | En línea: https://alexjusid-jpg.github.io/planos/migdalei/es/ |

## El edificio
- 8 pisos iguales con 4 departamentos: x01 y x02 de 1 habitación (2 baños), x03 y x04 de 2 habitaciones (2 baños). 32 departamentos.
- Planta baja: recepción con el **desk de enfermería** y teléfono de escritorio Android ACE52190200; oficina con el servidor ACE51010103; 2 baños públicos. *Distribución de PB propuesta: se ajusta con el plano del arquitecto.*

## Equipos
- Tablet en la puerta de cada departamento (iPad / Android): 32.
- Panel de llamada con voz y botones ACE82182451 en el salón y en cada dormitorio (con pera junto a la cama): 80.
- Tiradores ACE40320303W en el inodoro y en la ducha de todos los baños: 138 (incluye los 10 baños públicos).
- Luz de pasillo ACE41020309 sobre cada baño público: 10.
- LCom ACE71610003 por departamento y por baño público; 2 Buscomm + switch PoE por piso; servidor en PB.

## Cableado (todo Cat6 / Cat7 y PoE)
Verde: Cat6 radial de cada equipo al LCom · Naranja: cadena LCom → LCom → Buscomm del gabinete del piso · Rojo: switch → montante → servidor de PB.

## Cómo modificar
`model_mig2.py` (equipos y ubicaciones) → `python3 model_mig2.py` → `./build_lang_mig2.sh es|en|he` → `python3 build_viewer_mig2.py`.
Cantidades de anteproyecto: validar con Advantecnia y en obra.

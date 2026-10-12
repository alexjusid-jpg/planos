# Migdalei Yam a Tijon – Departamentos tutelados – Llamada de enfermería ACE BG / Advantecnia

Anteproyecto Rev. A · 12/10/2026 · Telab International

## Contenido
| Archivo | Qué es | Cómo se abre |
|---|---|---|
| `planos_2D_ES.pdf` | 7 láminas A1: piso tipo equipamiento y cableado (1:60), departamento tipo A y tipo B con alturas, esquema vertical PB + 6 pisos, topología y lista de materiales, vistas 3D | Cualquier lector PDF; imprimir en A1 |
| `plano_CAD_ES.dxf` | Plano CAD del piso tipo con capas por sistema; cables como polilíneas 3D; equipos como bloques con atributos ID / DESCRIPCION / ALTURA_M / CODIGO | AutoCAD, BricsCAD, DraftSight. Para **DWG**: abrir en AutoCAD → Guardar como → DWG |
| `modelo_BIM_ES.ifc` | Modelo BIM IFC4 del edificio: PB + 6 pisos con muros, puertas, ventanas, muebles, dispositivos y cables | **Revit**: Archivo → Abrir → IFC y guardar como **RVT** |
| `visor_3d_ES.html` | Visor 3D: equipamiento / cableado, recorrido, vistas, **modo Caminar** e **Ir a…** cada equipo | Doble clic (necesita internet). Versión en línea: https://claude.ai/artifact/4L9gAG1KqRfpgipCaP8ry9 |
| `recorrido_ES.mp4` | Video del recorrido con leyendas en español | Cualquier reproductor |
| `presentacion_ES.pptx` | Presentación de 11 diapositivas | PowerPoint, Keynote, Google Slides |
| `renders/` | Imágenes 3D | Cualquier visor |
| `fuentes/` | Scripts que generan todo desde `model.json` | Python 3 + Node |

## Cómo caminar en el visor 3D
1. Botón **🚶 Caminar**: quedás parado en el pasillo a la altura de los ojos.
2. Computadora: flechas o W / S para avanzar y retroceder, A / D para ir de costado, ← → o Q / E para girar, arrastrar el mouse para mirar.
3. Celular o tablet: botones ▲ ▼ ⟲ ⟳ en pantalla y arrastrar con el dedo para mirar.
4. Las paredes no se atraviesan: se entra por las puertas.
5. **Ir a…**: elegí un equipo (por ejemplo D1-TAB) y quedás parado frente a él con su ficha y código ACE.

## Edificio
- Planta baja: recepción con el puesto de enfermería (teléfono ACE52190200) y el gabinete principal con el servidor ACE51010103.
- Pisos 1 a 6: 6 departamentos por piso, 3 tipo A y 3 tipo B intercalados (36 en total). Sala de comunicaciones junto al ascensor.
- Tipo A: living con cocina abierta, dormitorio principal con baño en suite (ducha + inodoro), dormitorio 2, baño de visitas con ducha, hall y depósito.
- Tipo B: living con cocina abierta, un dormitorio y un baño con ducha.
- Mobiliario de vivienda (no hospitalario).

## Equipos por departamento
Tablet Android en el living (llamada y voz) · llamada con voz ACE82182451 en el dormitorio principal · tiradores ACE40320303W en inodoro y ducha (1,85 m) · presencia / cancelación junto a la puerta (opcional) · LCom ACE71610003 en el cielorraso del hall. Sin luz de pasillo.

## Cableado (todo Cat6 / Cat7 y PoE)
- **Verde**: Cat6 radial de cada equipo al LCom del departamento.
- **Naranja**: LCom → LCom → LCom → Buscomm ACE70810000 (2 Buscomm por piso).
- **Rojo**: Buscomm → switch PoE ACEUCM6302 del piso → montante → servidor de PB.
- La llamada llega por voz o como alarma al puesto de enfermería.

## Cómo modificar
1. Editar `fuentes/model_mig.py` (distribución, muebles, equipos) y ejecutar `python3 model_mig.py`.
2. Planos: `python3 plan_mig.py`. CAD / BIM: `python3 export_mig.py`. Visor: `python3 build_viewer_mig.py`.
3. Textos en inglés y hebreo: `fuentes/i18n/*.py` → regenerar `i18n_mig.json`.

## A verificar
Cantidades de anteproyecto: validar con Advantecnia y en obra.

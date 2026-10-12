# Pabellón de internación – Sistema de llamada de enfermería ACE BG / Advantecnia

Anteproyecto Rev. A · 12/10/2026 · Telab International

## Contenido
| Archivo | Qué es | Cómo se abre |
|---|---|---|
| `planos_2D_ES.pdf` | 7 láminas A1: planta de equipamiento y de cableado (1:50), habitación tipo con alzados, baños y estación de enfermería, topología + lista de materiales, vistas 3D | Cualquier lector PDF; imprimir en A1 para respetar la escala |
| `plano_CAD_ES.dxf` | Plano CAD con capas por sistema; cables como polilíneas 3D a su altura real; dispositivos como bloques con atributos ID / DESCRIPCIÓN / ALTURA / CÓDIGO ACE | AutoCAD, BricsCAD, DraftSight. Para **DWG**: abrir en AutoCAD → Guardar como → DWG |
| `modelo_BIM_ES.ifc` | Modelo BIM IFC4: muros, puertas, ventanas, mobiliario, sanitarios, dispositivos Advantecnia y tramos de cable | **Revit**: Archivo → Abrir → IFC (o Insertar → Vincular IFC) y guardar como **RVT** |
| `visor_3d_ES.html` | Visor 3D interactivo: modo equipamiento / cableado, recorrido, simulación de luces, ficha de cada equipo al hacer clic | Doble clic (necesita internet) |
| `walkthrough_ES.mp4` | Video recorrido con leyendas en español | Cualquier reproductor |
| `presentacion_ES.pptx` | Presentación de 11 diapositivas | PowerPoint, Keynote, Google Slides |
| `renders/` | Imágenes 3D en alta resolución | Cualquier visor de imágenes |

## Distribución
- Entrada por el extremo este del pasillo. Puertas desde la entrada: P1 Habitación 1 · P2 Habitación 2 · P3 Oficina · P4 Habitación 3 · P5 Habitación 4. En cada cuarto, desde la entrada, primero la puerta y después las 3 camas con la cabecera contra el muro lateral.
- Núcleo de baños frente a la Habitación 1: baño accesible (inodoro + ducha) junto al acceso del núcleo, luego baño de pacientes y al final baño del personal.
- Estación de enfermería frente a la oficina, con puerta propia; escritorio contra el muro del pasillo (ventana): PC / teléfono del lado de la pared, la enfermera mira al pasillo y a la TV. Gabinete de comunicaciones al otro extremo del pasillo.

## Cableado
- **Radial en cada cuarto**: cada dispositivo (llamada de cama, presencia, luz de pasillo, tirador) con su propio cable a la tarjeta de 24 pins (ECV169) del cuarto.
- **Cadena**: cada tarjeta de 24 pins se conecta a la siguiente con BUS KNX 2x2x0,8 mm LH EIBBUS; la última se conecta al SmartHub (Raspberry Pi).
- **Cat6 / Cat7 solo** del SmartHub al switch y al servidor, y a la PC o teléfono de enfermería y a la TV. Ningún cuarto tiene conexión Cat6/Cat7.
- **PoE**: tarjetas y dispositivos de llamada alimentados por PoE. 230 V solo en el gabinete (switch, servidor, SmartHub), PC / teléfono y TV.
- Colores: verde = bus y cableado radial de llamada · rojo = Cat6/Cat7 · azul = 230 V.

## Accesorios ACE BG
Llamada de cama ACE41220316 · tirador baño/ducha ACE40320303 · presencia/cancelación ACE80081001 · luz indicadora de pasillo ACE41020309 · teléfono de escritorio ACE52190200 · PC/monitor ACE52040208 · servidor ACE51010103 · switch ACEUCM6302 · tarjeta conversora en techo (24 pins ECV169).

## A verificar
Confirmar con Advantecnia el máximo de tarjetas por línea de bus y la longitud total del bus. Cantidades de anteproyecto.

# Nesher · Llamada de enfermería (ACE BG / Advantecnia)

- **URL pública:** https://alexjusid-jpg.github.io/planos/nesher/
- **Repositorio:** github.com/alexjusid-jpg/planos → carpeta `nesher/` (GitHub Pages, rama `main`). No hay contraseñas: la página es pública pero no indexada (noindex).
- **Chat original:** https://claude.ai/code/session_01BM25ckuPA3Nm3dsayCSS36

## Qué hay
| Archivo | Qué es |
|---|---|
| `index.html` | Visor interactivo 2D por planta (L00–L13), ES/EN/HE, modo revisión (✕ quitar punto), exportar CSV, resumen, documentos |
| `3d/es|en|he/` | Maqueta 3D de la planta típica L09 (12 cuartos, 32 camas, 11 baños): recorrido, caminar, cableado, simulación de llamadas, documentos |
| `assets/plan/Lxx.jpg` | Plano base de cada planta (aclarado) |
| `assets/eq/*.jpg` | Fotos reales de equipos ACE |
| `docs/Nesher_Plan2D_EN.pdf` | Planos 2D ACE estilo Yoseftal (17 hojas A3) |
| `docs/Nesher_BOQ_ACE_EN.xlsx` | BOQ ACE: hojas BOQ, Floors, Points (Y/N), Cables, Notes |
| `docs/GCN-ELC-Lxx-03_numbered.pdf` | Planos base del cliente con cada punto numerado (verde cama, azul baño) |

## Números
- Verde (cama / sillón): 1–535 · Azul (baño): 1–213, de la planta más baja a la más alta. B02 sin puntos. L02 vino duplicado: se usó una copia.
- Cuartos: L03 14, L04 14, L07 22, L08 20 (de los rótulos); resto estimado = camas ÷ 2,3.

## 3D
- Motor: el mismo de Yoseftal (three.js), con el modelo de Nesher generado desde los puntos del plano L09 (posiciones de camas y baños reales; muros y mobiliario aproximados).
- URL: https://alexjusid-jpg.github.io/planos/nesher/3d/es/ (también /en/ y /he/).

## Cómo modificar
1. **Quitar/agregar puntos:** en el Excel BOQ, hoja `Points`, columna `Confirmed` = N; todo el BOQ se recalcula. En el visor: Modo revisión → tocar punto → Exportar revisión (CSV) y mandarlo al chat.
2. **Cuartos por planta o plantas incluidas:** Excel, hoja `Floors`, celdas azules.
3. **Planos / visor:** pedir el cambio en el chat; se regeneran PDF, imágenes y `index.html` y se publica de nuevo en `nesher/`.

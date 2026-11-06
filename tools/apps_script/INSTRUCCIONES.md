# Activar el envío automático del formulario (una sola vez, ~5 minutos, desde la computadora)

Qué se logra: cuando alguien completa el formulario y toca **📤 שליחה**, todo (datos + archivos)
se guarda solo en Google Drive › App Planos Máster › "Proyecto <nombre> <fecha>", queda anotado en la
hoja "Solicitudes Planos Máster" y te llega un mail. Las actualizaciones van a "07 Actualizaciones".

1. En la computadora abrí **script.google.com** (con tu cuenta de Gmail) → **Nuevo proyecto**.
2. Borrá lo que aparece escrito y pegá todo el contenido de este archivo:
   https://raw.githubusercontent.com/alexjusid-jpg/planos/main/tools/apps_script/Code.gs
3. Arriba a la izquierda cambiá el nombre a **Planos Máster – formulario** → 💾 Guardar.
4. Botón azul **Implementar** (Deploy) → **Nueva implementación** → ⚙️ tipo: **Aplicación web**.
   - Ejecutar como: **Yo**
   - Quién tiene acceso: **Cualquier persona** (Anyone)
   → **Implementar**.
5. Google pide permiso: **Autorizar acceso** → elegí tu cuenta → "Google no verificó esta app" →
   **Configuración avanzada** → **Ir a Planos Máster (no seguro)** → **Permitir**.
   (Es tu propio script; el aviso es normal.)
6. Copiá la **URL de la aplicación web** (termina en `/exec`) y pegámela en el chat.
   Yo la pongo en el formulario y queda funcionando.

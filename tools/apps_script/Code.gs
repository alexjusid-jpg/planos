/**
 * Planos Máster – receptor del formulario (Google Apps Script).
 * Guarda automáticamente cada solicitud en Google Drive:
 *   App Planos Máster / Proyecto <nombre> <dd mm aaaa> / 01 Solicitud, 02 Planos, 03 BOQ, 04 Propuesta, 05 Presentacion, 06 3D y video
 * Las actualizaciones van a:  Proyecto <nombre> … / 07 Actualizaciones / <fecha hora>
 * Además: anota cada envío en la hoja "Solicitudes Planos Máster" y manda un mail al dueño de la cuenta.
 *
 * Instalación: ver INSTRUCCIONES.md (Implementar → Aplicación web → Ejecutar como: yo · Acceso: cualquier persona).
 */
const ROOT_ID = '11MzCqTsBpkAmVZZTIBMpuKlKnmzBclsg';   // carpeta "App Planos Máster"
const KEY = 'planos-master-2026';                        // la misma clave que usa el formulario
const SUBS = ['01 Solicitud', '02 Planos', '03 BOQ', '04 Propuesta', '05 Presentacion', '06 3D y video'];
const DEST = { plans: '02 Planos', boq: '03 BOQ', spec: '01 Solicitud/Mifrat tecnico', cabling: '01 Solicitud/Cableado',
               other: '01 Solicitud/Otros documentos', free: '01 Solicitud/Notas', ideas: '01 Solicitud/Ideas arquitecto' };

function doGet() { return out({ ok: true, service: 'Planos Master' }); }

function doPost(e) {
  try {
    const b = JSON.parse(e.postData.contents);
    if (b.key !== KEY) return out({ ok: false, error: 'key' });
    if (b.action === 'start') return out(start(b));
    if (b.action === 'file') return out(saveFile(b));
    if (b.action === 'finish') return out(finish(b));
    return out({ ok: false, error: 'action' });
  } catch (err) { return out({ ok: false, error: String(err) }); }
}

function out(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function child(parent, name) { const it = parent.getFoldersByName(name); return it.hasNext() ? it.next() : parent.createFolder(name); }
function path(base, p) { return p.split('/').reduce((f, n) => child(f, n), base); }
function clean(s) { return String(s || '').replace(/[\\\/:*?"<>|]+/g, '-').trim(); }
function stamp(fmt) { return Utilities.formatDate(new Date(), Session.getScriptTimeZone(), fmt); }

function findProject(root, name) {
  const want = ('proyecto ' + clean(name)).toLowerCase(); const it = root.getFolders();
  while (it.hasNext()) { const f = it.next(); if (f.getName().toLowerCase().indexOf(want) === 0) return f; }
  return null;
}

function start(b) {
  const root = DriveApp.getFolderById(ROOT_ID), m = b.meta || {};
  const name = clean(m.project || m.projectHe || m.client || 'nuevo');
  let proj = b.mode === 'update' ? findProject(root, name) : null;
  if (!proj) {
    const d = (m.requestDate || stamp('yyyy-MM-dd')).split('-').reverse().join(' ');
    proj = child(root, 'Proyecto ' + name + ' ' + d);
    SUBS.forEach(s => child(proj, s));
  }
  const base = b.mode === 'update' ? path(proj, '07 Actualizaciones/' + stamp('yyyy-MM-dd HH-mm')) : child(proj, '01 Solicitud');
  return { ok: true, folderId: base.getId(), projectId: proj.getId(), projectUrl: proj.getUrl(), mode: b.mode || 'new' };
}

function saveFile(b) {
  const base = DriveApp.getFolderById(b.folderId);
  const isUpdate = base.getParents().hasNext() && base.getParents().next().getName() === '07 Actualizaciones';
  let target = base;
  if (!isUpdate) { const proj = base.getParents().next(); target = path(proj, DEST[b.field] || '01 Solicitud/Otros documentos'); }
  else target = child(base, (DEST[b.field] || 'Otros').split('/').pop());
  const blob = Utilities.newBlob(Utilities.base64Decode(b.data), b.mime || 'application/octet-stream', clean(b.name));
  const f = target.createFile(blob);
  return { ok: true, id: f.getId() };
}

function finish(b) {
  const base = DriveApp.getFolderById(b.folderId);
  base.createFile('resumen.txt', b.summary || '', MimeType.PLAIN_TEXT);
  base.createFile('datos.json', JSON.stringify(b.meta || {}, null, 1), MimeType.PLAIN_TEXT);
  const m = b.meta || {};
  // registro en una hoja de cálculo
  const root = DriveApp.getFolderById(ROOT_ID); const it = root.getFilesByName('Solicitudes Planos Máster');
  const ss = it.hasNext() ? SpreadsheetApp.open(it.next()) : (function () { const s = SpreadsheetApp.create('Solicitudes Planos Máster'); DriveApp.getFileById(s.getId()).moveTo(root);
    s.getSheets()[0].appendRow(['Fecha', 'Tipo', 'Proyecto', 'Proyecto (HE)', 'Cliente', 'Distribuidor', 'Responsable', 'Archivos', 'Carpeta']); return s; })();
  ss.getSheets()[0].appendRow([new Date(), b.mode === 'update' ? 'Actualización' : 'Nueva', m.project, m.projectHe, m.client, m.distributor, m.requester, b.count || 0, base.getUrl()]);
  try { MailApp.sendEmail(Session.getEffectiveUser().getEmail(), (b.mode === 'update' ? 'Actualización: ' : 'Nueva solicitud: ') + (m.project || m.projectHe || m.client || ''),
    (b.summary || '') + '\n\nCarpeta: ' + base.getUrl()); } catch (err) {}
  return { ok: true, url: base.getUrl() };
}

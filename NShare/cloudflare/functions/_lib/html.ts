import type { FileEntry } from "./types";

function escapeHtml(text: string): string {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function linkify(text: string): string {
  const escaped = escapeHtml(text);
  const urlPattern = /(https?:\/\/[^\s<>"]+|www\.[^\s<>"]+)/gi;
  return escaped.replace(urlPattern, (match) => {
    const href = match.startsWith("http://") || match.startsWith("https://") ? match : `http://${match}`;
    return `<a href="${href}" target="_blank" rel="noopener noreferrer">${match}</a>`;
  });
}

function breadcrumb(path: string): string {
  const parts = path ? path.split("/") : [];
  let accumulated = "";
  const links = ['<a href="/">Home</a>'];

  for (const part of parts) {
    accumulated = accumulated ? `${accumulated}/${part}` : part;
    links.push(`<a href="/?path=${encodeURIComponent(accumulated)}">${escapeHtml(part)}</a>`);
  }

  return links.join(" / ");
}

interface IndexOptions {
  currentPath: string;
  items: FileEntry[];
  allowUpload: boolean;
  tokenRequired: boolean;
  noticeText: string;
  canEdit: boolean;
  adminRequired: boolean;
}

export function renderIndex({
  currentPath,
  items,
  allowUpload,
  tokenRequired,
  noticeText,
  canEdit,
  adminRequired,
}: IndexOptions): string {
  const rows = items
    .map((item) => {
      const icon = item.isDir ? "📁" : "📄";
      const href = item.isDir
        ? `/?path=${encodeURIComponent(item.path)}`
        : `/download?path=${encodeURIComponent(item.path)}`;
      const deleteButton = canEdit
        ? `<button class="btn-delete" data-path="${escapeHtml(item.path)}" data-name="${escapeHtml(item.name)}">🗑️</button>`
        : "";
      return `<tr><td>${icon}</td><td><a href="${href}">${escapeHtml(item.name)}</a></td><td>${escapeHtml(item.sizeDisplay)}</td>${canEdit ? `<td>${deleteButton}</td>` : ""}</tr>`;
    })
    .join("");

  const uploadButton = allowUpload ? '<a class="btn" href="/upload">Upload files</a>' : "";
  const loginButton = adminRequired && !canEdit ? '<a class="btn btn-secondary" href="/login">Admin login</a>' : "";
  const headerButtons = [loginButton, uploadButton].filter(Boolean).join("\n      ");
  const tokenMessage =
    tokenRequired && allowUpload
      ? '<p class="info">Authentication token required for uploads.</p>'
      : "";

  const adminMessage =
    adminRequired && !canEdit
      ? '<p class="info">Admin authentication required for uploads and edits. Use the admin login button above.</p>'
      : "";

  const noticeHtml = canEdit
    ? `
  <div class="notice-board">
    <div class="notice-header">
      <h2>Notice Board</h2>
      <button id="edit-notice-btn" class="btn btn-small">Edit</button>
    </div>
    <div id="notice-display" class="notice-content">${noticeText ? linkify(noticeText) : "<em>No notices</em>"}</div>
    <div id="notice-editor" class="notice-editor" style="display: none;">
      <textarea id="notice-textarea" rows="5">${escapeHtml(noticeText)}</textarea>
      <div class="notice-actions">
        <button id="save-notice-btn" class="btn">Save</button>
        <button id="cancel-notice-btn" class="btn btn-secondary">Cancel</button>
      </div>
    </div>
  </div>
`
    : `
  <div class="notice-board notice-readonly">
    <div class="notice-header">
      <h2>Notice Board</h2>
    </div>
    <div class="notice-content">${noticeText ? linkify(noticeText) : "<em>No notices yet</em>"}</div>
  </div>
`;

  const contentRows = rows || `<tr><td colspan="${canEdit ? 4 : 3}">No files</td></tr>`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>NShare</title>
  <link rel="stylesheet" href="/static/css/styles.css" />
  <script src="/static/js/app.js" defer></script>
</head>
<body>
  <header>
    <h1>NShare</h1>
    <div class="header-actions">
      ${headerButtons}
    </div>
  </header>
  <nav>${breadcrumb(currentPath)}</nav>
  ${tokenMessage}
  ${adminMessage}
  ${noticeHtml}
  <table>
    <thead>
      <tr><th></th><th>Name</th><th>Size</th>${canEdit ? "<th>Actions</th>" : ""}</tr>
    </thead>
    <tbody>
      ${contentRows}
    </tbody>
  </table>
</body>
</html>`;
}

export function renderUploadForm(currentPath: string): string {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Upload to NShare</title>
  <link rel="stylesheet" href="/static/css/styles.css" />
</head>
<body>
  <header>
    <h1>Upload files</h1>
  </header>
  <nav>${breadcrumb(currentPath)}</nav>
  <form method="post" enctype="multipart/form-data">
    <label>Select files
      <input type="file" name="files" multiple required />
    </label>
    <label>Target folder
      <input type="text" name="target" value="${escapeHtml(currentPath)}" />
    </label>
    <button type="submit">Upload</button>
  </form>
</body>
</html>`;
}

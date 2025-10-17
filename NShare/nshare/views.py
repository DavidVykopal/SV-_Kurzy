"""HTML rendering for NShare."""

from __future__ import annotations

import html
from pathlib import Path
from typing import Iterable

from .storage import FileMeta


def breadcrumb(path: Path) -> str:
    parts = ["<a href=\"/\">Home</a>"]
    accumulated = Path()
    for part in path.parts:
        accumulated /= part
        parts.append(
            f"<a href=\"/?path={html.escape(str(accumulated))}\">{html.escape(part)}</a>"
        )
    return " / ".join(parts)


def render_index(
    current_path: Path,
    items: Iterable[FileMeta],
    allow_upload: bool,
    token_required: bool,
    notice_text: str = "",
    can_edit_notice: bool = False,
) -> str:
    rows = []
    for item in items:
        icon = "📁" if item.is_dir else "📄"
        href = (
            f"/?path={html.escape(str(item.path))}"
            if item.is_dir
            else f"/download?path={html.escape(str(item.path))}"
        )

        # Add delete button only if can_edit_notice (means we're on write port)
        delete_btn = ""
        if can_edit_notice:
            delete_btn = f'<button class="btn-delete" data-path="{html.escape(str(item.path))}" data-name="{html.escape(item.name)}">🗑️</button>'

        rows.append(
            "<tr>"
            f"<td>{icon}</td>"
            f"<td><a href=\"{href}\">{html.escape(item.name)}</a></td>"
            f"<td>{item.size_display}</td>"
            f"<td>{delete_btn}</td>"
            "</tr>"
        )

    upload_button = (
        "<a class=\"btn\" href=\"/upload\">Upload files</a>" if allow_upload else ""
    )
    token_message = (
        "<p class=\"info\">Authentication token required for uploads.</p>"
        if token_required and allow_upload
        else ""
    )

    # Notice board HTML
    notice_html = ""
    if can_edit_notice:
        # Editable notice board for write port
        notice_html = f"""
  <div class="notice-board">
    <div class="notice-header">
      <h2>Notice Board</h2>
      <button id="edit-notice-btn" class="btn btn-small">Edit</button>
    </div>
    <div id="notice-display" class="notice-content">{html.escape(notice_text) if notice_text else '<em>No notices</em>'}</div>
    <div id="notice-editor" class="notice-editor" style="display: none;">
      <textarea id="notice-textarea" rows="5">{html.escape(notice_text)}</textarea>
      <div class="notice-actions">
        <button id="save-notice-btn" class="btn">Save</button>
        <button id="cancel-notice-btn" class="btn btn-secondary">Cancel</button>
      </div>
    </div>
  </div>
"""
    else:
        # Read-only notice board for read-only port - always show it
        notice_html = f"""
  <div class="notice-board notice-readonly">
    <div class="notice-header">
      <h2>Notice Board</h2>
    </div>
    <div class="notice-content">{html.escape(notice_text) if notice_text else '<em>No notices yet</em>'}</div>
  </div>
"""

    return f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset=\"utf-8\" />
  <title>NShare</title>
  <link rel=\"stylesheet\" href=\"/static/css/styles.css\" />
  <script src=\"/static/js/app.js\" defer></script>
</head>
<body>
  <header>
    <h1>NShare</h1>
    {upload_button}
  </header>
  <nav>{breadcrumb(current_path)}</nav>
  {token_message}
  {notice_html}
  <table>
    <thead>
      <tr><th></th><th>Name</th><th>Size</th>{'<th>Actions</th>' if can_edit_notice else ''}</tr>
    </thead>
    <tbody>
      {''.join(rows) if rows else f'<tr><td colspan={4 if can_edit_notice else 3}>No files</td></tr>'}
    </tbody>
  </table>
</body>
</html>
"""


def render_upload_form(current_path: Path) -> str:
    return f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset=\"utf-8\" />
  <title>Upload to NShare</title>
  <link rel=\"stylesheet\" href=\"/static/css/styles.css\" />
</head>
<body>
  <header>
    <h1>Upload files</h1>
  </header>
  <nav>{breadcrumb(current_path)}</nav>
  <form method=\"post\" enctype=\"multipart/form-data\">
    <label>Select files
      <input type=\"file\" name=\"files\" multiple required />
    </label>
    <label>Target folder
      <input type=\"text\" name=\"target\" value=\"{html.escape(str(current_path))}\" />
    </label>
    <button type=\"submit\">Upload</button>
  </form>
</body>
</html>
"""

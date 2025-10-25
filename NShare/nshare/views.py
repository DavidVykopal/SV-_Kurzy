"""HTML rendering for NShare."""

from __future__ import annotations

import html
import re
from pathlib import Path
from typing import Iterable

from .storage import FileMeta


def linkify_urls(text: str) -> str:
    """Convert URLs in text to clickable HTML links.

    Args:
        text: Plain text that may contain URLs

    Returns:
        HTML with URLs converted to <a> tags
    """
    if not text:
        return ""

    # First escape all HTML to prevent XSS
    escaped_text = html.escape(text)

    # URL regex pattern - matches http://, https://, and www. URLs
    url_pattern = re.compile(
        r'(https?://[^\s<>"]+|www\.[^\s<>"]+)',
        re.IGNORECASE
    )

    def replace_url(match):
        url = match.group(0)
        # Add http:// to www. URLs
        href = url if url.startswith(('http://', 'https://')) else f'http://{url}'
        return f'<a href="{href}" target="_blank" rel="noopener noreferrer">{url}</a>'

    return url_pattern.sub(replace_url, escaped_text)


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
    lan_ip: str = "",
    current_port: int = 0,
    student_port: int = 0,
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

    # Connection info HTML (only for teacher port)
    connection_info_html = ""
    if can_edit_notice and lan_ip and student_port:
        student_url = f"http://{lan_ip}:{student_port}"
        connection_info_html = f"""
  <div class="connection-info">
    <div class="info-header">
      <h3>📡 Share with Students</h3>
    </div>
    <div class="info-content">
      <p><strong>Student Access URL:</strong></p>
      <div class="url-box">
        <code id="student-url">{html.escape(student_url)}</code>
        <button class="btn btn-small btn-copy" data-copy-text="{html.escape(student_url)}">Copy</button>
      </div>
      <p class="info-note">Students can connect to this URL on the same network (read-only access)</p>
      <p class="info-note"><strong>Your Network IP:</strong> {html.escape(lan_ip)}</p>
    </div>
  </div>
"""

    # Notice board HTML
    notice_html = ""
    if can_edit_notice:
        # Editable notice board for write port
        # Convert URLs to clickable links in display
        notice_display = linkify_urls(notice_text) if notice_text else '<em>No notices</em>'
        notice_html = f"""
  <div class="notice-board">
    <div class="notice-header">
      <h2>Notice Board</h2>
      <button id="edit-notice-btn" class="btn btn-small">Edit</button>
    </div>
    <div id="notice-display" class="notice-content">{notice_display}</div>
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
        # Convert URLs to clickable links
        notice_display = linkify_urls(notice_text) if notice_text else '<em>No notices yet</em>'
        notice_html = f"""
  <div class="notice-board notice-readonly">
    <div class="notice-header">
      <h2>Notice Board</h2>
    </div>
    <div class="notice-content">{notice_display}</div>
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
  {connection_info_html}
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

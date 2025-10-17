# NShare Dual-Port Setup Guide

## Overview
Your NShare server now supports dual-port hosting with persistent storage:
- **Port 8000**: Full read-write access (for teachers)
- **Port 5555**: Read-only access (for students)
- **Data Directory**: `~/.nshare_data/files` - All uploaded files persist here
- **Notice Board**: `~/.nshare_data/notice_board.txt` - Messages persist between sessions

## Features

### Port 8000 (Teacher Access)
- Upload and download files
- Edit the notice board
- Delete files and folders with 🗑️ button
- Full file management

### Port 5555 (Student Access)
- Browse and download files only
- View the notice board (read-only)
- No upload capabilities

### Notice Board
- Displayed at the top of the file listing
- Teachers can edit via the "Edit" button on port 8000
- Students see the same message on port 5555 (read-only)
- Updates are synchronized in real-time

## Starting the Server

### Quick Start
```bash
./start_dual_port.sh
```

### Manual Start
```bash
cd /Users/davidvykopal/Documents/SVČ/NShare
python3 scripts/run_server.py --port 8000 --readonly-port 5555
```

### With Authentication Token
Edit `start_dual_port.sh` and uncomment the alternative command to add token authentication.

## Accessing the Server

### Teacher Access
- Local: http://localhost:8000
- Network: http://YOUR_IP:8000

### Student Access
- Local: http://localhost:5555
- Network: http://YOUR_IP:5555

The server will display your LAN IP address when it starts.

## Using the Notice Board

1. Open http://localhost:8000 in your browser
2. You'll see the notice board at the top
3. Click the "Edit" button
4. Type your message
5. Click "Save"
6. Students will see the message immediately on port 5555

## Deleting Files

On port 8000 (teacher access):
1. You'll see a trash icon (🗑️) next to each file/folder
2. Click the trash icon
3. Confirm the deletion
4. The file/folder will be immediately removed

**Note:** Students on port 5555 cannot delete files - they won't see the delete buttons.

## Python 3.13 Compatibility

All code has been updated to work with Python 3.13:
- Removed deprecated `cgi` module
- Replaced with `email.message.EmailMessage`
- Fixed authentication decorator

## Files Modified

- `nshare/server.py` - Dual-port support, notice board API, read-only logic
- `nshare/security.py` - Fixed decorator to handle callable tokens
- `nshare/views.py` - Added notice board HTML rendering
- `nshare/static/css/styles.css` - Notice board styling
- `nshare/static/js/app.js` - Notice board editing JavaScript
- `scripts/run_server.py` - Added `--readonly-port` CLI argument
- `start_dual_port.sh` - Startup script for dual-port mode

## Troubleshooting

### Port Already in Use
If you get "Address already in use" error:
```bash
lsof -ti:8000 -ti:5555 | xargs kill -9
```

### Module Not Found
Make sure you're running the script from the NShare directory or use the provided startup script.

## Persistent Storage

All your data is stored outside the codebase in `~/.nshare_data/`:

### Files Directory
- Location: `~/.nshare_data/files/`
- All uploaded files are stored here
- Files persist between server restarts
- You can directly add/remove files in this directory

### Notice Board
- Location: `~/.nshare_data/notice_board.txt`
- Plain text file storing the notice board message
- Automatically loaded when server starts
- Automatically saved when you edit via the web interface

### Managing Data

**View your data:**
```bash
ls -la ~/.nshare_data/files/
cat ~/.nshare_data/notice_board.txt
```

**Backup your data:**
```bash
tar -czf nshare-backup.tar.gz ~/.nshare_data/
```

**Clear all data:**
```bash
rm -rf ~/.nshare_data/
```

## Security Notes

- Both ports share the same authentication token (if configured)
- Read-only port prevents ALL write operations (uploads, edits, deletes)
- Notice board can only be edited from port 8000
- Data persists in your home directory, protected by your user permissions

Enjoy your dual-port file sharing system with persistent storage!

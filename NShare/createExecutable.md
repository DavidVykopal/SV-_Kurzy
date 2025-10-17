# createExecutable.md

## Prerequisites
- Python 3.13 (or compatible) installed.
- Virtual environment support (`python3 -m venv`).
- Internet access to download PyInstaller.

> **Note:** Building Windows executables must be performed on a Windows host (physical machine, VM, or CI). macOS cannot cross-compile.

## 1. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

## 2. Install PyInstaller
```bash
pip install --upgrade pip
pip install pyinstaller
```

## 3. Build macOS Executable (Apple Silicon)
```bash
pyinstaller --onefile \
  --add-data "nshare/static:nshare/static" \
  --add-data "nshare/templates:nshare/templates" \
  scripts/run_server.py
```
- Output binary: `dist/run_server`
- Build intermediates: `build/`

### Universal macOS binary (optional)
Requires a universal (arm64+x86_64) Python install. If available:
```bash
pyinstaller --onefile --target-arch universal2 \
  --add-data "nshare/static:nshare/static" \
  --add-data "nshare/templates:nshare/templates" \
  scripts/run_server.py
```
If you encounter `not a fat binary` errors, reinstall Python from python.org or use a universal framework build.

## 4. Build Windows Executable (on Windows)
```cmd
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install pyinstaller
pyinstaller --onefile ^
  --add-data "nshare/static;nshare/static" ^
  --add-data "nshare/templates;nshare/templates" ^
  scripts/run_server.py
```
- Output binary: `dist\run_server.exe`

## 5. Distribution Tips
- Copy `dist/run_server` (macOS) or `dist/run_server.exe` (Windows) to the target media (e.g., USB drive).
- Include `ngrok/` binary if remote tunnelling is required.
- Optionally bundle a `README-launch.txt` with run instructions.

## 6. Clean Up
```bash
rm -rf build dist run_server.spec
```
Run only if you want to remove build artifacts.

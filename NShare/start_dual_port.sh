#!/bin/bash
# Startup script for NShare with dual-port hosting
# Port 8000: Read-Write access (for teacher)
# Port 5555: Read-Only access (for students)

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Add the NShare directory to Python path
export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH"

echo "Starting NShare with dual-port configuration..."
echo "Port 8000: Read-Write (Teacher)"
echo "Port 5555: Read-Only (Students)"
echo ""

python3 "$SCRIPT_DIR/scripts/run_server.py" \
    --port 8000 \
    --readonly-port 5555 \
    --root "$SCRIPT_DIR/shared_files" \
    --verbose

# Alternative with authentication token:
# python3 ../scripts/run_server.py \
#     --port 8000 \
#     --readonly-port 5555 \
#     --root . \
#     --auth-token "your-secret-token" \
#     --verbose

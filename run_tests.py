import os
import subprocess
import sys

project_dir = os.path.dirname(os.path.abspath(__file__))
venv_python = os.path.join(project_dir, "venv", "Scripts", "python.exe")
if os.name != "nt" and os.path.exists(os.path.join(project_dir, "venv", "bin", "python")):
    venv_python = os.path.join(project_dir, "venv", "bin", "python")

if not os.path.exists(venv_python):
    sys.stderr.write("Virtual environment not found. Create it first with: python -m venv venv\n")
    sys.exit(1)

cmd = [venv_python, "-m", "pytest", "test_app.py"]
print("Running:", " ".join(cmd))
raise SystemExit(subprocess.call(cmd, cwd=project_dir))

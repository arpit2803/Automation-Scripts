application_title = "IPL Score"
main_python_file = "final_ipl.py"

import sys

from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

includes = ["os", "time", "win32api", "win32gui", "win32con", "sys", "struct", "requests", "bs4", "re"]

setup(
        name = application_title,
        version = "0.1",
        description = "simple file comparison",
        options = {"build_exe" : {"includes" : includes }},
        executables = [Executable(main_python_file, base = base)] )

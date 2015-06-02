application_title = "Comparison"
main_python_file = "file_comparison.py"

import sys

from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

includes = ["os", "time"]

setup(
        name = application_title,
        version = "0.1",
        description = "simple file comparison",
        options = {"build_exe" : {"includes" : includes }},
        executables = [Executable(main_python_file)] )

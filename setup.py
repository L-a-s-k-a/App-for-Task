import sys
from cx_Freeze import setup, Executable

# Базовая конфигурация для скрытия консоли (только для GUI-приложений)
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Только для графических приложений (tkinter, PyQt и т.д.)
    
# Определение исполняемого файла
executables = [
    Executable(
        script="CoV.py",
        base=base,      # "Win32GUI" для GUI, None для консольных приложений
        icon="icon.ico"
    )
]

# Настройка сборки
setup(
    name="CoV", 
    version="1.0",
    description="This app is designed to calculate individual homework variants",
    executables=executables
)
import sys
from pathlib import Path
from colorama import init, Fore
init(autoreset=True)

if len(sys.argv) < 2:
    print ("python hw03\hw_03.py . <доступ_до_директорії>")
    sys.exit(1)
second_el = sys.argv[1]
second_el_pathobj = Path(second_el)
if not second_el_pathobj.exists():
    print("Це розташування не існує")
    sys.exit(1)
if not second_el_pathobj.is_dir():
    print("Цієї директорії не існує")
    sys.exit(1) 

def function(path: Path, depth: int = 0):
    indent = " " * 4 * depth
    try:
        elements = sorted(path.iterdir(), key=lambda p: p.name)
    except PermissionError:
        print(f"{indent}У вас не має доступу до {path.name}")
        return
    for file in elements:
        if file.is_dir():
            print(Fore.BLUE + f"{indent}+ {file.name}/")
            function(file, depth + 1)
        else:
            print(Fore.GREEN + f"{indent}- {file.name}")
function(second_el_pathobj, 0)
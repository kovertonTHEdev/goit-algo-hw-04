from pathlib import Path
from cats_func import get_cats_info
BASE = Path(__file__).resolve().parent
cats_file = BASE / "cats_file.txt"

cats_info = get_cats_info(cats_file)
print(cats_info)

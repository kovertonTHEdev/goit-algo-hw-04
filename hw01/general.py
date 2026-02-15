from calculation_func import total_salary
from pathlib import Path

BASE = Path(__file__).resolve().parent
salaries_file = BASE / "salaries.txt"

total, average = total_salary(salaries_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

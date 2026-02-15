def total_salary (salaries_file): 
     try:
          with open(salaries_file, "r", encoding="UTF-8") as file:
               total = 0 # акумулятор
               count = 0 # акумулятор
               for line in file:
                    cleaned_line = line.strip() # прибирає пробіли 
                    parts = cleaned_line.split(",") # робить список імен + ЗП
                    if len(parts) == 2: 
                         salary_text = parts[1]
                         try: 
                              salary = int(salary_text)
                              total += salary # накопичення сум зарплат
                              count+=1 #накопичення акум
                         except ValueError:
                              continue
     except FileNotFoundError:
          return (0, 0)
     if count == 0:
          return (0, 0)
     if count > 0:
          average = total / count # cереднє вираховуємо
          return (total, average)
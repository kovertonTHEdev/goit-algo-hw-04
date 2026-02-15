def total_salary (salaries_file): 
     try:
          with open(salaries_file, "r", encoding="UTF-8") as file:
               total = 0
               count = 0 
               for line in file:
                    cleaned_line = line.strip() 
                    parts = cleaned_line.split(",") 
                    if len(parts) == 2: 
                         salary_text = parts[1]
                         try: 
                              salary = int(salary_text)
                              total += salary 
                              count+=1 
                         except ValueError:
                              continue
     except FileNotFoundError:
          return (0, 0)
     if count == 0:
          return (0, 0)
     if count > 0:
          average = total / count 
          return (total, average)
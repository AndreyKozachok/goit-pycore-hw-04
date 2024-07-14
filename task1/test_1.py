from pathlib import Path

def total_salary(path):
    average = 0
    total = 0
    num_developers = 0    
    with open(path, "r", encoding="utf-8") as file:
        
        for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total += salary
                        num_developers += 1
                    except ValueError:
                        print(
                            f"Помилка: Неправильний формат заробітної плати '{line.strip()}'"
                        )
        average = int(total / num_developers)
       
    print(f"Загальна сума заробітної плати {total}. Середня заробітна плата {average}.")
     

total_salary("task1/salary_file.txt")
   



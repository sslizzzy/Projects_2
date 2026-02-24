researcher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment_name = input("Введите название эксперимента: ")
experiment_conclusion = input("Введите вывод по эксперименту: ")

with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write("+--------------------------------------------------+\n")
    file.write("|       Электронный лабораторный журнал            |\n")
    file.write("+--------------------------------------------------+\n")
    file.write(f"| ФИО исследователя : {researcher_name:<30} |\n")
    file.write(f"| Дата             : {experiment_date:<30} |\n")
    file.write(f"| Эксперимент      : {experiment_name:<30} |\n")
    file.write("+--------------------------------------------------+\n")
    file.write("| Вывод:                                           |\n")
    file.write(f"| {experiment_conclusion:<48} |\n")
    file.write("+--------------------------------------------------+\n")

print("\nДанные успешно сохранены в файл journal.txt")
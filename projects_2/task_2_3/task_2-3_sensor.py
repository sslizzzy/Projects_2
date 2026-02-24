name_of_operator = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")

with open('sensor_log.txt', 'w', encoding='utf-8') as file:
     file.write(f"{name_of_operator}\t{pressure_value}\n")

print("\nДанные успешно сохранены в sensor_log.txt")
volume = float(input("Введите необходимый объем физиологического раствора (мл): "))
salt_mass = volume * 0.009
water_volume = volume

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем:\t{volume:.2f} мл\n")
    file.write(f"Масса соли:\t{salt_mass:.2f} г\n")
    file.write(f"Объем воды:\t{water_volume:.2f} мл\n")

print(f"\nРецепт успешно сохранен в файл recipe.txt")
print(f"Для приготовления {volume:.2f} мл 0.9% физиологического раствора необходимо:")
print(f"- Соль (NaCl): {salt_mass:.2f} г")
print(f"- Вода: {water_volume:.2f} мл")
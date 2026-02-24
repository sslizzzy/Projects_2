protein_g = float(input("Введите массу белков в продукте (г): "))
fat_g = float(input("Введите массу жиров в продукте (г): "))
carb_g = float(input("Введите массу углеводов в продукте (г): "))

total_calories = (protein_g * 4) + (fat_g * 9) + (carb_g * 4)

print(f"\nОбщая калорийность продукта: {total_calories:.1f} ккал")
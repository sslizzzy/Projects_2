seq_list = ["ATATACGCGTA", "CTTCGGNGGA"]

# Перебираем каждую последовательность в списке
for sequence in seq_list:
    print(f"\nПоследовательность: {sequence}")
    print("Построчный вывод:")
    
    # Перебираем каждый символ в последовательности
    for nucleotide in sequence:
        print(nucleotide)

# Завершающее сообщение
print("\nЦикл выполнен")
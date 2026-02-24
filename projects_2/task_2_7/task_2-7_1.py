files = ["seq1", "seq2", "seq3", "seq4"]
sample_date = "2026-02-25"

print("Обработка файлов:")
print("-" * 40)

for name in files:
    new_name = name + "_" + sample_date + ".fasta"
    print(f"{new_name}")

print("-" * 40)
print(f"Все файлы обработаны. Дата образцов: {sample_date}")
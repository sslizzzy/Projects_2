donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите группу крови реципиента (I, II, III, IV): ").strip().upper()
valid_groups = ["I", "II", "III", "IV"]

if donor not in valid_groups or recipient not in valid_groups:
    print("Ошибка: введена некорректная группа крови. Допустимые значения: I, II, III, IV")
else:
    if donor == "I" or donor == recipient:
        print(f"Переливание крови от донора с группой {donor} к реципиенту с группой {recipient} ВОЗМОЖНО")
        if donor == "I" and donor != recipient:
            print("   (Донор с I группой является универсальным донором)")
        elif donor == recipient:
            print("   (Группы крови совпадают)")
    else:
        print(f"Переливание крови от донора с группой {donor} к реципиенту с группой {recipient} НЕВОЗМОЖНО")
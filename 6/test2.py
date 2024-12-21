age_2021 = int(input("Введите ваш возраст на конец 2021 года: "))
for year in range(age_2021, 0, -1):
    print(f"В {2021 - age_2021 + year} году вам исполнилось {year} лет.")

num = int(input("Введите количество: "))
phrase = "На этом факультете есть "
if num % 10 == 1 and num % 100 != 11:
    phrase += f"{num} магистратура"
elif num % 10 in [2, 3, 4] and num % 100 not in [12, 13, 14]:
    phrase += f"{num} магистратуры"
elif num == 0 or num % 10 in [0, 5, 6, 7, 8, 9] or num % 100 in [11, 12, 13, 14]:
    phrase += f"{num} магистратур"
print(phrase)

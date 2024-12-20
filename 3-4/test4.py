n = int(input('Количество магистратур: '))
if n % 10 == 1 and n != 11:
    ending = 'магистратура'
elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
    ending = 'магистратуры'
else:
    ending = 'магистратур'
print(f'На этом факультете есть {n} {ending}')

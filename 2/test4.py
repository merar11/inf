past_president = input("Введите фамилию президента России на момент вашего рождения: ")
current_president = input("Введите фамилию нынешнего президента России: ")
if past_president.lower() == current_president.lower():
  print("Одинаковы")
else:
  print("Не одинаковы")

x = int(input("Enter not 0 num: "))
y = int(input("Enter not 0 num: "))
if x > 0 and y > 0:
    print("1")
else x > 0 and y < 0:
    print("3")
else x < 0 and y < 0:
    print("4")
else x < 0 and y > 0:
    print("2")
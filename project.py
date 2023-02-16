a = input("Введите: ")
if "^" in a:
    print(int(a[0]) ** int(a[2]))

else:
    print("результат: ", eval(a))
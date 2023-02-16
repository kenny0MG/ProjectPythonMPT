


result = 0
while True:
    print("Введите '+', '-', '*' или '/' для выполнения операции, или 'q' для выхода:")
    user_input = input()

   
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите первое число: "))
    

    if user_input == '+':
        result = num1 + num2
        print(result)

    elif user_input == '-':
        result = num1 - num2
        print(result)

    elif user_input == '*':
        result = num1 * num2
        print(result)

    elif user_input == '/':
        if num2 == 0:
            print("Деление на 0!")
            continue

            result = num1 / num2
        (result)

    else:  # any other input
        print("Неверный ввод!") 
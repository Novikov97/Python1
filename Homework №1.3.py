n = int(input("Введите целое положительное число "))
if n > 0:
    a = n + (n * 10 + n) + (n * 100 + n * 10 + n)
    print(a)
else:
    print("Вы ввели отрицательное число.")

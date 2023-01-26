receipt = int(input("Введите значение выручки фирмы "))
cost = int(input("Введите значение издержек фирмы "))

if receipt > cost:
    profit = receipt - cost
    rent = profit / receipt
    employee = int(input("Введите число сотрудников фирмы "))
    profit_employee = profit/employee
    print(f"Прибыль - выручка больше издержек."
          f"\nРентабельность выручки = {rent}."
          f"\nПрибыль фирмы в расчете на одного сотрудника {profit_employee}.")
else:
    print("Убыток - издержки больше выручки")

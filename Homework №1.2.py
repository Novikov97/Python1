sec = int(input("Введите время в секундах "))
#Считаем часы
hour = sec // 3600
#Считаем минуты
sec1 = sec % 3600
min = sec1 // 60
#Считаем секунды
sec2 = sec % 60
print(f"В {sec} сек - {hour}:{min}:{sec2}.")

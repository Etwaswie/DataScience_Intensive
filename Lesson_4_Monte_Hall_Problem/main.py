import math
import random
doors = [1, 0, 0] # 1 - машина, 0 - пусто
#print(doors)
right_choise = 0
wrong_choise = 0
for i in range(0, 1001):
    doors = [1, 0, 0]  # 1 - машина, 0 - пусто
    print("Есть 3 двери...")
    random.shuffle(doors)
    doors_copy = doors.copy()
    print(doors)

    choise = random.randrange(0, 3) # человек выбирает дверь
    print(f"Участник выбрал дверь номер {choise + 1}")

    doors[choise] = 'choisen'
    #print(doors)
    #print(doors_copy)

    opened = doors.index(0)
    doors[opened] = 'opened'
    print(f"Ведущий открывает дверь номер {opened + 1}, там оказывается пусто")
    #print(doors)
    #print(doors_copy)
    print(f"Ведущий предлагает сменить выбор на оставшуюся дверь, но участник не соглашается")

    if doors_copy[choise] == 1:
        print("Участник был прав и угадал нужную дверь")
        right_choise += 1
    else:
        print("К сожалению за выбранной дверью ничего не оказалось")
        wrong_choise += 1

print(f"Участники правильно угадали в {right_choise} случаях и ошиблись в {wrong_choise} случаях")
print(f"Правильный ответ был дан в {(right_choise/1001)*100}% случаев")

# 2 вариант
doors = [1, 0, 0] # 1 - машина, 0 - пусто
right_choise = 0
wrong_choise = 0
for i in range(0, 1001):
    doors = [1, 0, 0]  # 1 - машина, 0 - пусто
    print("Есть 3 двери...")
    random.shuffle(doors)
    doors_copy = doors.copy()
    #print(doors)

    choise = random.randrange(0, 3) # человек выбирает дверь
    print(f"Участник выбрал дверь номер {choise + 1}")

    doors[choise] = 'choisen'
    #print(doors)
    #print(doors_copy)

    opened = doors.index(0)
    doors[opened] = 'opened'
    print(f"Ведущий открывает дверь номер {opened + 1}, там оказывается пусто")
    #print(doors)
    #print(doors_copy)
    for _ in range(3):
        if doors[_] == 0 or doors[_] == 1:
            change_choise = doors.index(doors[_])
            #print(f"Оставшаяся - {change_choise}")

    print(f"Ведущий предлагает сменить выбор на дверь номер {change_choise + 1}, участник согласился")

    choise = change_choise
    if doors_copy[choise] == 1:
        print("Участник был прав и угадал нужную дверь")
        right_choise += 1
    else:
        print("К сожалению за выбранной дверью ничего не оказалось")
        wrong_choise += 1

print(f"Участники правильно угадали в {right_choise} случаях и ошиблись в {wrong_choise} случаях")
print(f"Правильный ответ был дан в {(right_choise/1001)*100}% случаев")
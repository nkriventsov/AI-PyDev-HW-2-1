# 8. (МОДУЛЬ 3) В проекте создать новый модуль bornday.py
# 9. Написать программу или модернизировать предыдущую используя условные операторы:
# - Спросить у пользователя год рождения А.С. Пушкина
# - Если пользователь ввел верный год спросить у него день рождения
# - Если день рождения введен верно вывести 'Верно'
# - Если день рождения введен неверно вывести 'Неверный день рождения'
# - Если неверно введен год, то сразу вывести 'Неверный год рождения', а день рождения не спрашивать
#___________________________________________________________________________________________

actual_birth_year = 1799
chosen_birth_year = int(input("Введите год рождения А.С. Пушкина: "))
actual_birth_date = "06/06"

if chosen_birth_year == actual_birth_year:
    chosen_birth_date = input('Введите дату рождения А.С. Пушкина в формате "дд/мм": ')
    if chosen_birth_date == actual_birth_date:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')
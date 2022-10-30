# 12. (МОДУЛЬ 5) В проекте создать новый модуль borndayforewer.py
# 13.Написать или модернизировать программу (МОДУЛЬ 3) используя условные операторы и цикл while:
# Просим пользователя ввести год рождения А.С. Пушкина до тех пор пока он не ввел правильный год,
# после этого спрашиваем день рождения до тех пор, пока он не ввел верный день.
# После верного ответа выводим в терминал 'Верно' и выходим из программы
#___________________________________________________________________________________________

actual_birth_year = 1799
chosen_birth_year = None
actual_birth_date = "06/06"
chosen_birth_date = None
while chosen_birth_year != actual_birth_year:
    if chosen_birth_year != None:
        print('Неверный год рождения')
    chosen_birth_year = int(input("Введите год рождения А.С. Пушкина: "))
else:
    while chosen_birth_date != actual_birth_date:
        if chosen_birth_date != None:
            print('Неверный день рождения')
        chosen_birth_date = input('Введите дату рождения А.С. Пушкина в формате "дд/мм": ')
    else:
        print('Верно')
print('Спасибо!')



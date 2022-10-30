# 14. (МОДУЛЬ 6) В проекте создать новый модуль victory.py
# 15. Используя любые средства написать программу викторина:
# Выбрать минимум 5 известных людей и узнать их год рождения.
# Программа должна по очереди спрашивать у пользователя год рождения знаменитости.
# После того как пользователь ввел все ответы, программа считает и выводит на экран:
# - количество правильных ответов
# - количество ошибок
# - процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ)
# - процент неправильных ответов
# После вывода информации программа спрашивает
#
# пользователя хочет ли он начать игру сначала, если да - то повторяем все сначала, если ответ нет - выходим из программы
#
# - В программе с помощью комментариев написать подсказки - правильные ответы для каждой знаменитости
#_______________________________________________________________________________________________________

pushkin_birth_year = 1799       # Д.р. А.С. Пушкин
akhmatova_birth_year = 1889     # Д.р. А.А. Ахматова
lermontov_birth_year = 1814     # Д.р. М.Ю. Лермонтов
blok_birth_year = 1880          # Д.р. А.А. Блок
nekrasov_birth_year = 1821      # Д.р. Н.А. Некрасов
total_questions = 5
new_play = "Да"

while new_play == "Да":
    correct_answers = 0
    wrong_answers = 0
    chosen_birth_year = int(input("Введите год рождения А.С. Пушкина: "))   # 1799
    if chosen_birth_year == pushkin_birth_year:
        correct_answers += 1
    else:
        wrong_answers += 1

    chosen_birth_year = int(input("Введите год рождения А.А. Ахматовой: "))   # 1889
    if chosen_birth_year == akhmatova_birth_year:
        correct_answers += 1
    else:
        wrong_answers += 1

    chosen_birth_year = int(input("Введите год рождения М.Ю. Лермонтова: "))   # 1814
    if chosen_birth_year == lermontov_birth_year:
        correct_answers += 1
    else:
        wrong_answers += 1

    chosen_birth_year = int(input("Введите год рождения А.А. Блока: "))   # 1880
    if chosen_birth_year == blok_birth_year:
        correct_answers += 1
    else:
        wrong_answers += 1

    chosen_birth_year = int(input("Введите год рождения Н.А. Некрасова: "))   # 1821
    if chosen_birth_year == nekrasov_birth_year:
        correct_answers += 1
    else:
        wrong_answers += 1

    print('\n_______________________________________')
    print('Количество правильных ответов: ',correct_answers)
    print('Количество неправильных ответов: ', wrong_answers)
    print('Процент правильных ответов: ', correct_answers*100/total_questions,'%')
    print('Процент неправильных ответов: ', wrong_answers*100/total_questions,'%')
    print('_______________________________________\n')

    new_play = input('Хотите начать игру сначала? (Да/Нет) ')
    while new_play != "Да" and new_play != "Нет":
        new_play = input('Для повторной игры наберите "Да" - для выхода наберите "Нет": ')

else:
    print('\nБлагодарим за игру!')






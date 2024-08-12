import random

magic_num = random.randint(1, 101)
tryes = 7

print('Привет! Я хочу сыграть с тобой в игру "Угадай число"')
print('Целое число загадывается в диапозоне от 1 до 100')
print('Всего будет', tryes, 'попыток!')
print('Ну что, начнем?')


def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    return False


while tryes > 0:



    num = input('Введи чиcло от 1 до 100')
    if not is_valid(num):
        print('Может все таки введем нужное нам число?')
        continue
    num = int(num)

    if magic_num < num:
        print('Твое число больше')
        tryes -=1
        print('Осталось попыток', tryes)
    elif magic_num > num:
        print('Твое число меньше')
        tryes -= 1
        print('Осталось попыток', tryes)
    elif magic_num == num:
        print('Вы угадали!! Поздравляем :)')
        print('Желаете сыграть еще?')
        answer = input('Введите "Да" или "Нет"').lower()
        if answer == 'нет':
            print('Еще увидимся!')
            break
        elif answer == 'да':
            magic_num = random.randint(1, 101)
            tryes = 7
            continue


    if tryes == 0:
        print('Попытки закончились! Сыграем снова?')
        lose_game_answer = input('Введите "Да" или "Нет"').lower()
        if lose_game_answer == 'нет':
            print('Жаль :(')
            print('Еще увидимся!')
            break
        elif lose_game_answer == 'да':
            magic_num = random.randint(1, 101)
            tryes = 7
            continue


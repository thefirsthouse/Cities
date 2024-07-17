import random

def last_ltr(answer):
    stop_letters = ('ъ', 'ы', 'ь')
    last_letter = answer[-1]
    if (last_letter == 'й' and 'Йошкар-Ола' not in available_cities) or \
        (last_letter in stop_letters):
        last_letter = answer[-2]
        if answer[-2] in stop_letters:
            last_letter = answer[-3]
    
    return last_letter


cities = []
with open('ru') as file:
    for x in file:
        cities.append(x[:-1])
available_cities = list(cities)

bot_last_letter, user_last_letter = 0, 0
bot_answer = random.choice(available_cities)

print('чтобы сдаться нажмите "enter"')

game_is_over = False
user_surrendered = False
while not game_is_over:
    print(bot_answer)
    bot_last_letter = last_ltr(bot_answer)
    
    user_answered = False
    user_answer = str(input('ваш ответ: '))
    
    if len(user_answer) == 0:
        user_surrendered = True
        game_is_over = True
    elif user_answer.lower()[0] != bot_last_letter:
        print(f'нет, введите город на букву "{bot_last_letter}"!')
    elif user_answer not in cities:
        print('такого города в России нет!')
    elif user_answer in cities and user_answer not in available_cities:
        print('такой город уже был!')
    else:
        user_answered = True
        available_cities.remove(bot_answer)
    
    if user_answered:
        available_cities.remove(user_answer)
        user_last_letter = last_ltr(user_answer)
        for city in available_cities:
            if city.lower()[0] == user_last_letter:
                bot_answer = city
                break
        else:
            print(f'я не знаю больше городов на "{user_last_letter}"')
            game_is_over = True

if user_surrendered:
    print('игра завершена. бот победил')
else:
    print('вы победили')
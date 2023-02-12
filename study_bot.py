from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from config_study_bot import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.types.web_app_info import WebAppInfo
from random import randint

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()

user: dict = {'in_game': False}

list_for_bot = ['Камень', 'Ножница', 'Бумага']

def bot_choose_card():
    id = randint(0, 2)
    bot_choice = list_for_bot[id]
    return bot_choice

# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Камень')
button_2: KeyboardButton = KeyboardButton(text='Ножницы')
button_3: KeyboardButton = KeyboardButton(text='Бумага')
button_4: KeyboardButton = KeyboardButton(text='Стоп')

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1], [button_2], [button_3], [button_4]],
                                    resize_keyboard = True,

                                    row_width=3)

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Приветик. Я местный кот\n Как смотришь на то, чтобы поиграть в камень/ножницы/бумага ?). \n Enter /apply to play! \n Правила хоть помнишь? Напиши /help если че')
    bot_choose_card()

@dp.message(Text(text='/help'))
async def help_fun(message: Message):
    await message.answer('Задачка игры такая: \n -Выиграть у меня поставив знак который бьет мой \n -Бумага бьет камень \n -Камень бьет ножницы \n -Ножницы бумагу \n Ты готов? Вводи /apply')

@dp.message(Text(text='/apply'))
async def apply(message: Message):
    await message.answer('Гуд. Я ща загадаю быстренько, а ты выбирай.)', reply_markup=keyboard)
    user['in_game'] = True

@dp.message(Text(text='Стоп'))
async def stop_game(message: Message):
    await message.answer('Игра остановлена!')
    user['in_game'] = False
    await message.answer('Чтобы продолжить играть напиши /apply')

#принимает значение когда id игры положительный
@dp.message(lambda x: x.text and x.text != 'Стоп')
async def game_process(message: Message):
    bot_choice = bot_choose_card()
    if user['in_game'] == True:
        # для мувов когда ничья
        if message.text == bot_choice:
            await message.answer(f'Мой выбор - {bot_choice}')
            await message.answer('Ничья. Тоже ниче так :)')
            await message.answer('Хочешь продолжить? Если нет - нажми "Стоп"')
            print(f'Выбор игрока - {message.text}, выбор бота {bot_choice}')

        # для мувов когда выиграл

        elif message.text == 'Бумага' and bot_choice == 'Камень':
            await message.answer(f'Мой выбор - {bot_choice}')
            await message.answer('Ты выиграл. Красавчик!')
            await message.answer('Хочешь продолжить? Если нет - нажми "Стоп"')
            print(f'Выбор игрока - {message.text}, выбор бота {bot_choice}')

        elif message.text == 'Ножницы' and bot_choice == 'Бумага':
            await message.answer(f'Мой выбор - {bot_choice}')
            await message.answer('Ты выиграл. Красавчик!')
            await message.answer('Хочешь продолжить? Если нет - нажми "Стоп"')
            print(f'Выбор игрока - {message.text}, выбор бота {bot_choice}')

        elif message.text == 'Камень' and bot_choice == 'Ножницы':
            await message.answer(f'Мой выбор - {bot_choice}')
            await message.answer('Ты выиграл. Красавчик!')
            await message.answer('Хочешь продолжить? Если нет - нажми "Стоп"')
            print(f'Выбор игрока - {message.text}, выбор бота {bot_choice}')

        #для мувов когда слил
        elif message.text == 'Бумага' and bot_choice == 'Ножницы':
            await message.answer(f'Мой выбор - {bot_choice}')
            await message.answer('Проиграл. Ну ниче. Выиграешь еще меня как-то <3')
            await message.answer('Хочешь продолжить? Если нет - нажми "Стоп"')
            print(f'Выбор игрока - {message.text}, выбор бота {bot_choice}')

        elif message.text == 'Ножницы' and bot_choice == 'Камень':
            await message.answer(f'Мой выбор - {bot_choice}')
            await message.answer('Проиграл. Ну ниче. Выиграешь еще меня как-то <3')
            await message.answer('Хочешь продолжить? Если нет - нажми "Стоп"')
            print(f'Выбор игрока - {message.text}, выбор бота {bot_choice}')

        elif message.text == 'Камень' and bot_choice == 'Бумага':
            await message.answer(f'Мой выбор - {bot_choice}')
            await message.answer('Проиграл. Ну ниче. Выиграешь еще меня как-то <3')
            await message.answer('Хочешь продолжить? Если нет - нажми "Стоп"')
            print(f'Выбор игрока - {message.text}, выбор бота {bot_choice}')

        elif message.text != 'Бумага' and message.text != 'Ножницы' and message.text != 'Камень':
            await message.answer('Ошибочка. Нажми камень/ножница/бумага. Я обычные сообщения не принимаю ;)))')

    else:
        await message.answer('Ошибочка')


if __name__ == '__main__':
    dp.run_polling(bot)


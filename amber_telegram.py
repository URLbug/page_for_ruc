from aiogram import Bot, Dispatcher, types, executor

from database import User, db

import json


token = json.load(open("./json/token.json", 'rb'))

bot = Bot(token['TOKEN'])

dp = Dispatcher(bot)

@dp.message_handler(commands=['new_send'])
async def start(m: types.Message):
    user = [[i.first_name, i.last_name, i.email, i.about] for i in db.session.query(User).distinct()]
    
    user_ = """Имя: {}
               
               Фамилия: {}
       
               Электронная почта: {}
       
               Обо мне:
               {}
    """

    for i in user:
        await m.reply(user_.format(i[0], i[1], i[2], i[3]))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
from telethon import TelegramClient, events
from telethon import Button
from telethon.tl import custom
from DataBase import *
from config import *

client = TelegramClient('TestTask', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    if event.is_private:
        session = Session()
        print(event.chat.id)
        user = session.query(User).filter_by(user_id=event.chat.id).first()
        messages = session.query(Message).all()
        print(messages)
        if not user:
            user = User(event.chat.id)
            user.step = 1
            session.add(user)
        if '/start' == event.raw_text or 'Привет' == event.raw_text:
            await event.reply('Меню А\n-Б\n-С')

        if 'А' == event.raw_text:
            await event.reply('Меню А\n-Б\n-С')
            user.step = 1

        elif 'Б' == event.raw_text:
            await event.reply('Меню Б\n-Г\n-А')
            print('A')
            user.step = 2

        elif 'В' == event.raw_text:
            if not user.step == 2:
                await event.reply('ТекстТекстТекст')

        elif 'Г' == event.raw_text:
            await event.reply('функция Г')
            await client.send_message(entity=event.message.to_id, message='Меню А\n-Б\n-С')
            user.step = 1
        else:
            return

        chat_id = event.chat.id
        message_id = event.message.id
        text = event.message.message
        message = Message(text, message_id, chat_id, chat_id)
        session.add(message)

        session.commit()
        session.remove()


async def bot():
    me = await client.get_me()

client.start()
client.run_until_disconnected()



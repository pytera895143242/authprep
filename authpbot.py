from pyrogram import Client
from pyrogram import filters
from pyrogram import types
import sqlite3
import time
import random
import asyncio
app = Client('my_accounts')

my_id = 941730379


@app.on_message(filters.text)
async def payments (client,message):
    if (message.text[0:2] =='Пп' and message.from_user.id == my_id) or message.text[0:18] == 'Добавь прокладку @':
        if message.text[0:18] == 'Добавь прокладку @':
            id_user = message.chat.id
            user_channel = message.text[19:]

            try:
                a = await app.create_channel(title=message.chat.first_name)
                await app.send_message(chat_id=a.id, text=f"""<b>Фильмы 2021 скрыты от посторонних глаз. И доступны на приватном канале по ссылке ниже. Заходи и следуй инструкции</b>

<a href = https://t.me/MovieAndSerialsBot?start={user_channel}>🍿НАЧАТЬ СМОТРЕТЬ🍿</a>""")

                await app.add_chat_members(chat_id=a.id, user_ids=id_user)
                await app.promote_chat_member(chat_id=a.id, user_id=id_user, can_manage_chat=True, can_change_info=True,
                                              can_post_messages=True, can_edit_messages=True, can_delete_messages=True,
                                              can_restrict_members=True, can_invite_users=True, can_pin_messages=True,
                                              can_manage_voice_chats=True)

                url = await app.export_chat_invite_link(chat_id=a.id)
                await asyncio.sleep(3)

                await app.send_message(chat_id=message.chat.id, text=f"""Это прокладка:
{url}

В дальнейшем используешь только эту ссылку. Ты админ в этом канале, поменяй аву и имя канала. Имя используй такое же как и в основном тг канале с фильмами.""")

            except:
                await app.send_message(chat_id=message.chat.id, text="""Не могу создать тебе прокладку и добавить тебя туда.

Что бы это исправить переходи в настройки, нажимай

    - Конфидециальность
    - Группы и каналы
И добавь меня в список тех, кто тебя может приглашать в группы

После этого напиши мне и мы повторим попытку""")
        else:
            try:
                id_user = message.chat.id
                user_channel = message.text[4:]


                a = await app.create_channel(title=message.chat.first_name)
                await app.send_message(chat_id=a.id,text=f"""<b>Фильмы 2021 скрыты от посторонних глаз. И доступны на приватном канале по ссылке ниже. Заходи и следуй инструкции</b>
                
    <a href = https://t.me/MovieAndSerialsBot?start={user_channel}>🍿НАЧАТЬ СМОТРЕТЬ🍿</a>""",disable_web_page_preview=True)

                await app.add_chat_members(chat_id=a.id,user_ids= id_user)
                await app.promote_chat_member(chat_id=a.id,user_id=id_user,can_manage_chat= True,can_change_info= True,can_post_messages = True, can_edit_messages= True, can_delete_messages = True, can_restrict_members= True,can_invite_users = True, can_pin_messages = True,can_manage_voice_chats = True)

                url = await app.export_chat_invite_link(chat_id=a.id)
                await asyncio.sleep(3)

                await app.send_message(chat_id=message.chat.id,text=f"""Это прокладка:\n{url}
        
В дальнейшем используешь только эту ссылку. Ты админ в этом канале, поменяй аву и имя канала. Имя используй такое же как и в основном тг канале с фильмами.""")

            except:
                await app.send_message(chat_id=message.chat.id,text="""Не могу создать тебе прокладку и добавить тебя туда.
    
Что бы это исправить переходи в настройки, нажимай

    - Конфидециальность
    - Группы и каналы
И добавь меня в список тех, кто тебя может приглашать в группы

После этого напиши мне и мы повторим попытку""")

app.run()
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink, Callback, EMPTY_KEYBOARD, BaseStateGroup
from vkbottle import GroupTypes, GroupEventType , PhotoMessageUploader
from vkbottle.bot import Bot, Message
from vkbottle.user import User
import asyncio
import re
import time
from io import BytesIO
import requests
from flask import Flask
import threading
import os
import ssl
import aiohttp
import logging
logging.basicConfig(level=logging.DEBUG)
ssl_context = ssl.create_default_context()



class BotWithSender(User):
    async def sender(self, peer_id: int, message: str, payload=None):
        await self.api.messages.send(peer_id=peer_id, message=message, random_id=0, payload=payload)

Denis = User("vk1.a.Wu5KGqQNtr4DpgfFSbkR-SPcDGSJ0YQjE84Dp5CYo-H1TPZFiTt9JvYoE_L8naeDNOjSN0VSuSKPwnFzRbq9AbS8dZCaSnz6PQOIxDTAtDMde-EK03jjMrF9EaNAVs-UIMCrpOk-81odrt0WNeZzs_4qe6PK3RqkXm0un0cG1Q1GD9en7zv0zD57WlTsp6btigEVuwYAO6Nb-7W1lYrI_w")  # Укажи свой токен
gosha = BotWithSender('vk1.a.wl9gKEEsjqPFfO83ZYX_DICNf_H796MhoE0Kj52-5IFW7xyL4tKnaWhaqexBq6Za2txTF_I2si7gwN3d9NW0yO9TxKFqgMVJihauPB8_Tq8jV4FGufEOCRnKaiWtS4YyyKkah8v5_Okw4l7HpufjepfCbey_yNeYaG900s9GzHzAJQj55bI2yVD2EBaJZR1RmzJ_NU6bPee5eVBNBddD9A')
bot = Bot("vk1.a.2dG-eNOBzQsxYGyWUeXgEK8FJ3kwWkZDE3F1JjeLIAaOIGbl0FK6CT-Pk7gpJ2FvfPzoYODyGKJRGM_1d9bhoJ7WY5XIL_bBDxvbqgEZu7cWiTyLUDB0O8_2aTwebxlorkurVzx4Q2Q1w777PmyaXtXzs8IMwPl3WOGp31gNzJ_4e5PgyF1TwzdR9gWWbTXOq7wNABVRMqATHhCrekiVSA")
hotdog = User('vk1.a.hqgSXtT4nkztV3-BsKOkoQjup_gVNqb3-XJsAw_NY8JlT5XN-AnDYr267MRQFmlOm8iZlIblBSz6p5UPmWQ4iEC5rv4_aDRF37obtNHnbBZMaHPHUw-zktYi_l2mov5xJMtQE9bwCt5000OA_ICmJhMi__lP8bvJNcMAXZdH01YMijaMzRp1rnlwDgj_eFudQzDBYNlCop4A_z-mSvcJHQ')

app = Flask(__name__)

uploader = PhotoMessageUploader(bot.api)

MRK = 2000000459  
helper_mrk = 2000000003     
frede = 180427590  

helper_er = 2000000004
er = 2000000006

def replace_ids_with_links(text):
    return re.sub(r"\[id(\d+)\|(.+?)\]", r"[https://vk.com/id\1|\2]", text)

dt = 2000000001
group = 2000000015
frede = -180427590  
dt_h = 2000000126
group_gosha = 2000000010
nabor = True
last_nabor_time = 0
nabor_interval = 2400
rtop = False

nabor_text = ('⚡️ Эй! Ты готов влиться в пиздатый клан DemonTale? ⚡️\n'             
    'Открыт набор в легендарный клан DemonTale! Хотите играть с лучшими? Вот твой шанс!\n\n'

    '🔥 Почему стоит к нам вступить:\n'
    '👥 Дружный коллектив с поддержкой на каждом шагу\n'
    '🎁 Зарплата монетами, чтобы не чувствовать себя зря\n'
    '🏰 Союз с крутыми ребятами из DopiDUO\n'
    '🏰 DemonTale – мы на 8-м уровне, и это только начало!\n\n'

    '📍 Постоянные статы:\n'
    '  8🛡 3🗡 4🔮\n'
    '  22❤ 2🩸 1🏃🏿‍♂\n'
    '    2🔱\n\n'

    '⚔️ Требования к тебе:\n'
    '🎮 Реальная взаимовыручка\n'
    '⚡ Проявлять любую активность из:\n'
    '— Арена, минимум 65/60 боев 🍾\n'
    '— Битва с боссами 👹\n'
    '— Скам лохов (новичков) 💰\n'
    '📊 Сумма стат 300+\n\n'

    '💬 Готов доказать свою ценность? Пиши заявку этим ребятам:\n'
    '[https://vk.com/larnikys|ле чоза птица] / [https://vk.com/free.hotdog|хотдог] / [https://vk.com/ratatyi14|глава]')

async def get_user_name(user_id):
    user_info = await Denis.api.users.get(user_ids=[user_id])
    if user_info:
        return f"{user_info[0].first_name} {user_info[0].last_name}"
    return "Неизвестный пользователь"

check = False

async def check_item(name,item,message:Message):
    print('f')
    await gosha.sender(frede, '💰 Обмен', payload='{"data": "newchange"}') #newchange 💰 Обмен
    await asyncio.sleep(3)
    await gosha.sender(frede,f'{name}')
    await asyncio.sleep(3)
    await gosha.sender(frede,'Балтика 9 1')
    await asyncio.sleep(3)
    await gosha.sender(frede,f'{item} 999999999999')

async def get_bot_name(bot_id: int):
    if bot_id < 0:  # ID ботов и групп в ВК всегда отрицательный
        group_id = abs(bot_id)
        group_info = await bot.api.groups.get_by_id(group_id=group_id)
        return group_info[0].name  # Название группы
    else:
        return "Неизвестный бот"  # На случай, если бот использует User API

clan = False
carta = False
carta_id = 0

@bot.on.message()
async def helper(message: Message):
    global nabor, last_nabor_time , rtop ,check , clan , carta , carta_id
    current_time = time.time()
    message_text = message.text.lower()
    if message.peer_id == dt:
        
        if message.text.lower() == 'топ':
            try:
                rtop = False
                await gosha.api.messages.send(
                    peer_id=frede,
                    message='⭐ Топ кланов',
                    payload='{"data": "topclans"}',
                    random_id=0,
                )
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")
        
        if 'птоп' in message.text.lower():
            rtop = True
            try:
                await gosha.api.messages.send(
                    peer_id=frede,
                    message='⭐ Топ кланов',
                    payload='{"data": "topclans"}',
                    random_id=0,
                )
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")

        if '⭐Топ' in message.text:
            try:
                rtop = False
                await gosha.api.messages.send(
                    peer_id=frede,
                    message='⭐ Топ кланов',
                    payload='{"data": "topclans"}',
                    random_id=0,
                )
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")

        if message.text.lower() == 'карточка':
            if carta == False:
                carta = True
                rtop = False
            
                await message.answer('Секунду ...')
                carta_id = message.from_id
                await gosha.api.request('messages.sendMessageEvent', {'author_id':-180427590, 'payload':'{"data": "clanmembers"}', 'peer_id':-180427590})
                await asyncio.sleep(2)
                await gosha.api.request('messages.sendMessageEvent', {'author_id':-180427590, 'payload':'{"data": "topclans"}', 'peer_id':-180427590})
                await asyncio.sleep(2)
                await gosha.api.request('messages.sendMessageEvent', {'author_id':-180427590, 'payload':f'{{"data": "viewfrede {carta_id}"}}', 'peer_id':-180427590})
            else:
                await message.answer('падаже')
        
        if message.text.lower() == 'клан':
            print('проверка')
            clan = True
            if clan == True:
                try:
                    await gosha.api.request('messages.sendMessageEvent', {'author_id':-180427590, 'payload':'{"data": "clanmembers"}', 'peer_id':-180427590})

                except Exception as e:
                    print(f"Ошибка при отправке сообщения: {e}")
        
        if message.text.lower() == 'набор':
            if nabor == True:
                nabor = False
                last_nabor_time = current_time
                await hotdog.api.messages.send(
                    peer_id=group,
                    message=nabor_text,
                    random_id=0,
                )
                await bot.api.messages.send(
                peer_id=dt,
                message='✅ Набор отправлен',
                random_id=0,
                )            
                
                await asyncio.sleep(nabor_interval)
                nabor = True
            else:
                remaining_time = int(nabor_interval - (current_time - last_nabor_time))

                await bot.api.messages.send(
                    peer_id=dt,
                    message=f'Набор уже отправлен , подождите {remaining_time} сек.',
                    random_id=0,
                )

        if message.text == 'Текст набора':
            await bot.api.messages.send(
                peer_id=dt,
                message=nabor_text,
                random_id=0
            )

        if '✉' in message.text:
            if nabor == True:
                nabor = False
                last_nabor_time = current_time
                await hotdog.api.messages.send(
                    peer_id=group,
                    message=nabor_text,
                    random_id=0,
                )
                await bot.api.messages.send(
                peer_id=dt,
                message='✅ Набор отправлен',
                random_id=0,
                )            
                
                await asyncio.sleep(nabor_interval)
                nabor = True
            else:
                remaining_time = int(nabor_interval - (current_time - last_nabor_time))

                await bot.api.messages.send(
                    peer_id=dt,
                    message=f'Набор уже отправлен , подождите {remaining_time} сек.',
                    random_id=0,
                )

        if message.text.lower() =='команды':
            await bot.api.messages.send(
                peer_id=dt,
                message='Список команд:\n'
                'Клан - чекнуть клан\n'
                'Топ - чекнуть топ кланов\n'
                'птоп - подробный топ кланов\n'
                'Набор - отправить набор клана в беседу',
                random_id=0,
            )
        
        if message.text == '/вступить':
            await bot.api.messages.send(
                peer_id=dt,
                message='По поводу вступления в клан писать -->  [https://vk.com/ratatyi14|главе]',
                random_id=0,
            )
        
        if message.text.lower() == 'вступить':
            await bot.api.messages.send(
                peer_id=dt,
                message='По поводу вступления в клан писать -->  [https://vk.com/ratatyi14|главе]',
                random_id=0
            )            

        if not message.fwd_messages:
            if message.text.lower() == "гет":

                result = message.reply_message.from_id
                await gosha.api.messages.send(
                    peer_id=frede,
                    message=f'@id{result}',
                    payload=f'{{"data": "viewfrede {result}"}}',
                    random_id=0
                )

            if message.text.lower() == "глянуть":

                result = message.reply_message.from_id
                await gosha.api.messages.send(
                    peer_id=frede,
                    message=f'@id{result}',
                    payload=f'{{"data": "viewfrede {result}"}}',
                    random_id=0
                )

        if 'гет' in message.text.lower():
            username = message.text[4:].strip()
            if username.startswith("https://vk.com/"):
                username = username.replace("https://vk.com/", "")
            elif '@' in username:
                username = username[3:12] # [id659583910|@free.hotdog]
              
              
            user_info = await bot.api.users.get(user_ids=username)
            user_id = user_info[0].id

            await gosha.api.messages.send(
                peer_id=frede,
                message=f'@id{user_id}',
                payload=f'{{"data": "viewfrede {user_id}"}}',
                random_id=0
            )

        if 'глянуть' in message.text.lower():
            username = message.text[8:].strip()
            if username.startswith("https://vk.com/"):
                username = username.replace("https://vk.com/", "")
            elif '@' in username:
                username = username[3:12] # [id659583910|@free.hotdog]
              
              
            user_info = await bot.api.users.get(user_ids=username)
            user_id = user_info[0].id

            await gosha.api.messages.send(
                peer_id=frede,
                message=f'@id{user_id}',
                payload=f'{{"data": "viewfrede {user_id}"}}',
                random_id=0
            )

        if message.text.lower() == 'соло боссы':
            await bot.api.messages.send(
                peer_id=dt,
                message='Список соло боссов:\n\n'
                'Растеньице\n'
                'Сосунок\n' 
                'Бравлер\n'
                'Гуленыш\n' 
                'Орк дибил\n'
                'Пенелопа\n'
                'Данилка\n'
                'Дерево в депрессии\n'
                'Банда кошкодевок\n'
                'Волшебный сундучок\n'
                'Шрикардо Милос\n'
                'Ведьма\n'
                "Король крысов\n"
                'Маньяк снеговик\n'
                'Русал_очко\n'
                'Псевдогигант\n',
                random_id=0
            )

        if message_text[0:3] == 'чек':

            if check == False:
                check = True
                if message.reply_message:
                    text = message.text
                    words = text.split()
                    reply_info = await bot.api.users.get(user_ids=message.reply_message.from_id)
                    name = reply_info[0].id
                    if len(words) < 2:
                        await message.answer("Ошибка 2", disable_mentions=1)
                        check = False
                        return
                    item = " ".join(words[1:])
                    await message.answer(f'ID: {name}\nПредмет: {item}',disable_mentions=1,)
                    await check_item(name,item,message)

                else:
                    text = message.text
                    words = text.split()
                    if len(words) < 3:
                        await message.answer("Ошибка 1", disable_mentions=1)
                        check = False
                        return
                    
                    name = words[1]
                    item = " ".join(words[2:])
                    await message.answer(f'ID: {name}\nПредмет: {item}',disable_mentions=1,)
                    await check_item(name,item,message)
            else:
                await message.answer('Ошибка . Сработало ограничение на пользование командой')

        if message.text.lower() == 'дай руну':
            await message.answer('нет')

carta_text = []

@gosha.on.message()
async def gosha_helper(message:Message):
    global rtop , check , clan , carta ,carta_text , carta_id
    

    if message.peer_id == frede:
        
        if '🏰 Список участников:' in message.text:
            if clan :
                print(message.text)
                keyboard = Keyboard(inline=True)
                keyboard.add(Text('⭐Топ'))
                keyboard.add(Text('✉'))
                keyboard.add(Text('птоп'))
                text = message.text
                lines = text.split('\n')
                first_11_lines = lines[:11]
                clan = "\n".join(first_11_lines)
                clan1 = replace_ids_with_links(clan)
                clan2 = clan1.replace('️⭐','')
                clan3 = clan2.replace(' ⭐️ ','')
                clan4 = clan3.replace('⭐',' ')
                clan5 = clan4.replace('🏰 Список участников:','🏰   Доска почёта   🏰')
                clan6 = clan5.replace('1)','🥇')
                clan7 = clan6.replace('2)','🥈')
                clan = clan7.replace('3)','🥉')


                print(clan)
                await bot.api.messages.send(
                    peer_id=dt,
                    message=f'{clan}',
                    random_id=0,
                    dont_parse_links=False,
                    keyboard=keyboard,
                )
                clan = False
            
            elif carta :
                text = message.text
                carta_text.clear()
                pattern = rf"(\d+)\) .*?\[id{carta_id}\|.*?\]: (\d+)🔰"
                
                match = re.search(pattern, text)
                place = int(match.group(1))
                points = int(match.group(2))   # Извлекаем очки
                carta_text.append(points)
                carta_text.append(place)

        if '⭐ Топ кланов:' in message.text:
            
            if carta:
                text = message.text
                pattern = r".*?\) .*?DemоnTale.*?-\s(\d+)🔰"
                match = re.search(pattern, text)
                clan_points = int(match.group(1))   # Извлекаем очки
                carta_text.append(clan_points)

            elif rtop == False:
                text = message.text
                await bot.api.messages.send(
                    peer_id=dt,
                    message=f'{text}',
                    random_id=0,
                    dont_parse_links=False,
                )
            
            elif rtop == True:
                text = message.text
                lines = text.split('\n')
                first_11_lines = lines[1:6]
                text = "\n".join(first_11_lines)
                pattern = r'\)\s([^\(]+)\s\(\d+lvl\)\s-\s(\d+)🔰'
                matches = re.findall(pattern, text)
                clans = [(clan_name.strip(), int(clan_exp)) for clan_name, clan_exp in matches]
                response = []
                for i in range(len(clans)):
                    clan_name, clan_exp = clans[i]
                    response.append(f"{i + 1}){clan_name}-{clan_exp}🔰")

                    if i < len(clans) - 1:
                        next_clan_exp = clans[i + 1][1]
                        difference = clan_exp - next_clan_exp
                        response.append(f"ㅤㅤ↑{difference}🔰↓")
                texts = ("\n".join(response))


                await bot.api.messages.send(
                    peer_id=dt,
                    message=f'⭐ Подробный рейтинг кланов:\n{texts}',
                    random_id=0,
                    dont_parse_links=False,
                )
                rtop = False

        if '💰 Баланс:' in message.text:
            if '🌀 Чудо-монеты: ' in message.text:
                print('r')
            
            else:
                if carta:
                    photo_attachments = []
                    text = message.text
                    # Загружаем фото из сообщения
                    for attachment in message.attachments:
                        if attachment.photo:
                            # Получаем URL самого большого размера изображения
                            photo_url = attachment.photo.sizes[-1].url
                            # Загружаем изображение
                            response = requests.get(photo_url)
                            # Подготавливаем изображение к загрузке на VK
                            photo_attachments.append(
                                await uploader.upload(BytesIO(response.content), peer_id=dt)
                            )

                    lines = text.split('\n')
                    name1 = lines[:1]
                    name = name1[0]
                    exp = carta_text[0]
                    exp_number =  carta_text[1]
                    
                    exp_clan = carta_text[2]
                    
                    exp_share = (exp / exp_clan) * 100
                    

                    exp_number_text = (f'{exp_number})')

                    if exp_number == 1:
                        exp_number = '🥇'
                        exp_number_text = (f'{exp_number}')
                    if exp_number == 2:
                        exp_number = '🥈'
                        exp_number_text = (f'{exp_number}')
                    if exp_number == 3:
                        exp_number = '🥉'
                        exp_number_text = (f'{exp_number}')

                    
                    await bot.api.messages.send(
                        peer_id = dt,
                        message=f'👤 {name} \n{exp_number_text} Очки клана: {exp} 🔰\n{name} нафармил {exp_share:.2f}% от очков клана',
                        attachment=photo_attachments,
                        random_id=0,
                        disable_mentions=1,
                    )
                    carta = False
                
                else:
                    photo_attachments = []
                    
                    # Загружаем фото из сообщения
                    for attachment in message.attachments:
                        if attachment.photo:
                            # Получаем URL самого большого размера изображения
                            photo_url = attachment.photo.sizes[-1].url
                            # Загружаем изображение
                            response = requests.get(photo_url)
                            # Подготавливаем изображение к загрузке на VK
                            photo_attachments.append(
                                await uploader.upload(BytesIO(response.content), peer_id=dt)
                            )
                    await bot.api.messages.send(
                        peer_id=dt,
                        message=message.text,
                        attachment=",".join(photo_attachments),
                        random_id=0,
                    )

        if 'Количество' in message.text:
            if check:
                text = message.text
                await bot.api.messages.send(
                    peer_id=dt,
                    message = f'{text}',
                    random_id=0,
                    disable_mentions=1,
                )

                check = False

        if message.text == 'Этот чел не зареган в ботике':
            if check:
                text = message.text
                await bot.api.messages.send(
                    peer_id = dt,
                    message=f'{text}',
                    random_id=0,
                )
                
                check = False

        if any(phrase in message.text for phrase in ['ни спамь емо е', 'падажи, не спамь', 'я тута', 'Нипонил']):
            if check:
                text = message.text
                await bot.api.messages.send(
                    peer_id = dt,
                    message=f'Произошла ошибка :\n{text}',
                    random_id=0
                )
                
                check = False
        
        if 'не найден' in message.text:
            if check:
                text = message.text
                await bot.api.messages.send(
                    peer_id = dt,
                    message=f'{text}',
                    disable_mentions=1,
                    random_id=0,
                )
                
                check = False

    if message.peer_id == group_gosha:
        if '🏰 Атака на локацию' in message.text:
            if message.from_id == frede:
                text = message.text
                await bot.api.messages.send(
                    peer_id=dt,
                    message=f'{text}',
                    random_id=0,
                    dont_parse_links=False,
                )
        if '🏰 Локация' in message.text:
            if message.from_id == frede:
                text = message.text
                await bot.api.messages.send(
                    peer_id=dt,
                    message=f'{text}',
                    random_id=0,
                    attachment=None,
                    dont_parse_links=False,
                )                

@Denis.on.message()
async def message_handler(message: Message):
    
    if message.peer_id == MRK:  # Проверяем, что сообщение из нужной беседы
        photo = None
        sticker  = None 
        audio_message = None
        sender_id = message.from_id  # ID отправителя
        sender_name = await get_user_name(sender_id)  # Получаем имя и фамилию отправителя
        text = message.text  # Текст сообщения
        
        # Стикеры , Фото , Аудио сообщения
        if message.attachments:
            try:
                # Проверка фото в вложениях
                photo_attachments = []
                for attachment in message.attachments:
                    if attachment.photo:
                        # Берём самое большое изображение
                        photo_url = sorted(attachment.photo.sizes, key=lambda s: s.height * s.width, reverse=True)[0].url
                        # Загружаем изображение
                        response = requests.get(photo_url)
                        # Подготавливаем изображение к загрузке на VK
                        photo_attachment = await uploader.upload(BytesIO(response.content), peer_id=dt)
                        photo_attachments.append(photo_attachment)

                # Формируем строку вложений
                if photo_attachments:
                    photo = ",".join(photo_attachments)
            except Exception as e:
                await bot.api.messages.send(
                    peer_id=helper_mrk,
                    message=f"Ошибка при обработке фото: {e}",
                    random_id=0,
                )
                print(f"Ошибка при обработке фото: {e}")

            try:
                # Проверка стикеров
                if message.attachments[0].sticker:
                    sticker = message.attachments[0].sticker.sticker_id

                    sender_info = await bot.api.users.get(user_ids=message.from_id)
                    sender_first = sender_info[0].first_name
                    sender_last = sender_info[0].last_name

                    # Отправляем стикер в нужную беседу
                    await bot.api.messages.send(
                        peer_id=helper_mrk,
                        message='',
                        sticker_id=sticker,
                        random_id=0,
                        disable_mentions=1,
                    )
                    await bot.api.messages.send(
                        peer_id=helper_mrk,
                        message=f'↑ Стикер от [id{message.from_id}|{sender_first} {sender_last}]',
                        random_id=0,
                        disable_mentions=1,
                    )
            except Exception:
                pass

            try:
                # Проверка голосовых сообщений
                if message.attachments[0].audio_message:
                    audio_message = message.attachments[0].audio_message.link_mp3


            except Exception:
                pass
        
        # Сообщения , без ответов и пересланных сообщений
        if not message.fwd_messages and not message.reply_message:
            if '-' in str(message.from_id):  # Проверяем, что сообщение отправлено ботом
                bot_name = await get_bot_name(message.from_id)  # Автоматически определяем имя бота
                await bot.api.messages.send(
                    peer_id=helper_mrk,
                    random_id=0,
                    message=f'👤{bot_name}\n📜> {text}',
                    attachment=photo if photo else None,
                    sticker_id=sticker,
                    disable_mentions=1,
                )
            else:  # Сообщение от пользователя
                sender_info = await bot.api.users.get(user_ids=message.from_id)
                first = sender_info[0].first_name
                last = sender_info[0].last_name

                await bot.api.messages.send(
                    peer_id=helper_mrk,
                    random_id=0,
                    message=f'👤 [id{message.from_id}|{first} {last}]:\n📜> {message.text}',
                    attachment=photo if photo else None,
                    disable_mentions=1
                )
                if audio_message:
                    await bot.api.messages.send(
                        peer_id=helper_mrk,
                        random_id=0,
                        message=f'🎙 Голосовое сообщение от {first} {last}: \n{audio_message}',
                        disable_mentions=1
                    )

            return
        
        # Сообщения с ответом
        if message.reply_message:
            try:
                if '-' in str(message.reply_message):  # Проверяем, что сообщение отправлено ботом
                    bot_name = await get_bot_name(message.reply_message)  # Автоматически определяем имя бота
                    reply_info = await bot.api.users.get(user_ids=message.reply_message.from_id)
                    reply_first = reply_info[0].first_name
                    reply_last = reply_info[0].last_na
                    
                    original_text = message.reply_message.text or "Без текста"
                    if len(original_text) > 12:
                        original_text = f'{original_text[:12]} ...'

                    else:
                        original_text =message.reply_message.text or 'Без текста'

                    await bot.api.messages.send(
                        peer_id=helper_mrk,
                        random_id=0,
                        message=(
                            f"👤 [id{sender_id}|{sender_name}]\n"
                            f"  |{bot_name}:\n"
                            f"  |{original_text}\n"
                            f"📜> {message.text}"
                        ),
                        attachment=audio_message if audio_message else (photo if photo else None),
                        disable_mentions=1
                    )           
                
                else:
                
                    # Получаем информацию об оригинальном сообщении
                    reply_info = await bot.api.users.get(user_ids=message.reply_message.from_id)
                    reply_first = reply_info[0].first_name
                    reply_last = reply_info[0].last_name

                    original_text = message.reply_message.text or "Без текста"
                    if len(original_text) > 12:
                        original_text = f'{original_text[:12]} ...'

                    await bot.api.messages.send(
                        peer_id=helper_mrk,
                        random_id=0,
                        message=(
                            f"👤 [id{sender_id}|{sender_name}]\n"
                            f"  |[id{message.reply_message.from_id}|{reply_first} {reply_last}]:\n"
                            f"  |{original_text}\n"
                            f"📜> {message.text}"
                        ),
                        attachment=audio_message if audio_message else (photo if photo else None),
                        disable_mentions=1
                    )
                    if audio_message:
                        await bot.api.messages.send(
                            peer_id=helper_mrk,
                            random_id=0,
                            message=f'🎙 Голосовое сообщение от {first} {last}: \n{audio_message}',
                            disable_mentions=1
                        )               
                    return
            except Exception as e:
                print(e)
            
        # Пересланные сообщения
        if not message.reply_message and message.fwd_messages:
            try:
                # Проверяем, есть ли пересланные сообщения
                fwd_message = message.fwd_messages[0] if message.fwd_messages else None

                if fwd_message is None:
                    await bot.api.messages.send(
                        peer_id=helper_mrk,
                        random_id=0,
                        message="Ошибка: нет данных о пересланном сообщении.",
                        attachment=photo if photo else None, 
                        disable_mentions=1
                    )
                    return

                # Проверяем, кто отправил пересланное сообщение
                fwd_from_id = fwd_message.from_id
                if not fwd_from_id:
                    await bot.api.messages.send(
                        peer_id=helper_mrk,
                        random_id=0,
                        message="Ошибка: пересланное сообщение не содержит from_id.",
                        disable_mentions=1
                    )
                    return

                # Получаем имя отправителя пересланного сообщения
                if fwd_from_id < 0:  # Если это сообщество или бот
                    group_id = abs(fwd_from_id)  # Убираем "-"
                    group_info = await bot.api.groups.get_by_id(group_id=group_id)
                    first2 = group_info[0].name
                    last2 = ""  # У сообществ нет фамилии
                else:  # Если это пользователь
                    sender_fwd = await bot.api.users.get(fwd_from_id)
                    first2 = sender_fwd[0].first_name
                    last2 = sender_fwd[0].last_name

                # Получаем данные отправителя текущего сообщения
                sender = await bot.api.users.get(message.from_id)
                first = sender[0].first_name
                last = sender[0].last_name

                # Текст пересланного сообщения
                fwd_text = fwd_message.text if fwd_message.text else "Текст отсутствует"

                # Отправляем сообщение
                await bot.api.messages.send(
                    peer_id=helper_mrk,
                    random_id=0,
                    message=(
                        f"👤 *Ответ от [id{message.from_id}|{first} {last}]*\n"
                        f"📜 {message.text}\n\n"
                        f"↪️ На сообщение от [id{fwd_from_id}|{first2} {last2}]:\n"
                        f"📄 > {fwd_text}"
                    ),
                    attachment=photo if photo else None, 
                    disable_mentions=1
                )

                if audio_message:
                    await bot.api.messages.send(
                        peer_id=helper_mrk,
                        random_id=0,
                        message=f'🎙 Голосовое сообщение от {first} {last}: \n{audio_message}',
                        disable_mentions=1
                    )

            except Exception as e:
                await bot.api.messages.send(
                    peer_id=helper_mrk,
                    message=f"Ошибка при обработке пересланного сообщения: {e}",
                    random_id=0,
                )


@app.route('/')
def index():
    return "Бот запущен и работает!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

async def run_users():
    await asyncio.gather(Denis.run_polling(), bot.run_polling(), gosha.run_polling(),hotdog.run_polling())
    await threading.Thread(target=run_flask).start()

asyncio.run(run_users())

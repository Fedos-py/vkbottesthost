import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests

vk = vk_api.VkApi(token="15a4c8cc3ceaa121d1afc5032f40846ef7f01b1655f97560950e5535986e165cb49d472b72c9ede63a1be")
#longpoll = VkLongPoll(vk)
bot_api = vk.get_api()
otvet = ''

# Функция посылающая сообщение
def write_msg(peer_id, message):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random_id})

while True:
    longpoll = VkBotLongPoll(vk, 201978017)
    try:
        for event in longpoll.listen():
            print(event)
            write_msg(event.object.peer_id, f'@id{event.object.from_id}(Пользователь) написал {event.object.text}')
    except Exception as e:
        print(e)
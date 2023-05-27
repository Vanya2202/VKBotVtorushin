import datetime
import vk_api
import sqlite3
from vk_api.longpoll import VkLongPoll, VkEventType

# <Имя бота> сохрани фразу <фраза>
# <Имя бота> напиши фразу
class VKBot:
	def __init__(self, bot_name, api_token):
		self.session = vk_api.VkApi(token=api_token)
		self.longpoll = VkLongPoll(self.session)
		self.vk = self.session.get_api()
		self.bot_name = bot_name

	def send_message(self, message, id):
		self.vk.messages.send(user_id=id, message=message, random_id=datetime.datetime.now().microsecond)

	def start(self):
		for event in self.longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text.split(" ")[0] == self.bot_name:
				self.send_message("Привет мир!", event.user_id)






bot = VKBot("Test", "vk1.a.NGi1Be3DBsow87hMscvPUIgHK10nh1pKkXvK2zppRBxCHZHRaRGcUqYqvs2p83Ia5vs6sDTeAM_ZjDp_yZ6datvff0y446UQRzxw3HVP59B0uqg1wDTkL05vj-0xJ_avVrTWmLUQ5M2rStaeR17RnmYdpFxOByoGPGMZ4cVp1NJeXTwMwYpSTyeRZfzT3FVjMaV0xWGyH8JVtcjp3a-Vog")
bot.start()

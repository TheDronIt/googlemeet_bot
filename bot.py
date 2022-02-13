import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.upload import VkUpload
from datetime import datetime, timedelta
from multiprocessing import Process
from selenium import webdriver
from threading import Thread
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import account, rasp

#Settings
minimum_number_of_users_to_logout = 6 #Normal value 6
minimum_number_of_messages_to_send = 6 #Normal value 6

admin = [
	'219648345', #Дрон
]


vk = vk_api.VkApi(token=account.vk_token)
longpoll = VkLongPoll(vk)
print("Bot launched")


#Today info
current_datetime = datetime.now()
weekday_today = int(current_datetime.isoweekday())
day_today = current_datetime.day
month_today = current_datetime.month
now_hour = current_datetime.hour
now_minute = current_datetime.minute
messages_count = 0
print(current_datetime)

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('media.navigator.permission.disabled', True)
#option.add_argument("--headless") #Without browser window
driver = webdriver.Firefox(options=option)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id':get_random_id()})



def weektype():
	now = datetime.now()
	sep = datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)
	d1 = sep - timedelta(days=sep.weekday())
	d2 = now - timedelta(days=now.weekday())
	weektype = ((d2 - d1).days // 7) % 2 #1Blue 0Red
	return weektype


def GoogleAuth():
	try:
		driver.get("https://accounts.google.com")
		mail_input = driver.find_element(By.ID, "identifierId")
		mail_input.send_keys(account.togu_mail)

		btn_next = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
		btn_next.click()

		time.sleep(5)

		togu_name_input = driver.find_element(By.ID, "id_username")
		togu_password_input = driver.find_element(By.ID, "id_password")

		togu_name_input.send_keys(account.togu_name)
		togu_password_input.send_keys(account.togu_password)
		togu_btn_next = driver.find_element(By.XPATH, "/html/body/div/div/form/div/div/div[1]/div[1]/button").click()
		time.sleep(5)
	except:
		print("Ошибка авторизации\nПерезапускаем")
		time.sleep(5)
		GoogleAuth()


def GoogleMeet_conntect(link):
	driver.get(link) #Google Meet link
	time.sleep(2)
	mute_microphone()
	turn_off_webcam()
	time.sleep(1)
	meet_connect = driver.find_element(By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()
	global messages_count
	messages_count = 0 #Count messages in chat
	open_chat()

def GoogleMeet_disconntect():
	driver.find_element(By.XPATH, "/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button").click()


def GoogleMeet_send_message(message):
	chat = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[5]/div/div[1]/div[2]/textarea')
	chat.send_keys(message)
	send_btn = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[5]/span/button').click()

def Screenshot():
	site = driver.find_element(By.TAG_NAME, "html")
	site.screenshot('screenshot.png')
	time.sleep(2)


def Close_browser():
	time.sleep(5)
	driver.close()
	driver.quit()


def open_chat():
	#add try
	chat = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[3]/div/div/div[3]/span/button')
	chat_open = chat.get_attribute("aria-pressed")
	if chat_open == "false":
		chat.click()


def mute_microphone():
	#add try
	microphone = driver.find_element(By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div") 
	microphone_muted = microphone.get_attribute("data-is-muted")
	if str(microphone_muted) == "false":
		site = driver.find_element(By.TAG_NAME, "html")
		site.send_keys(Keys.CONTROL + 'D') #Mute microphone


def turn_off_webcam():
	#add try
	webcam = driver.find_element(By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div") 
	webcam_turned_off = webcam.get_attribute("data-is-muted")
	if str(webcam_turned_off) == "false":
		site = driver.find_element(By.TAG_NAME, "html")
		site.send_keys(Keys.CONTROL + 'E') #Mute microphone


def exit_with_a_minimum_of_users():
	try:
		number_of_users = int(driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[3]/div/div/div[2]/div/div').text)
		if number_of_users <= minimum_number_of_users_to_logout:
			GoogleMeet_disconntect()
	except:
		pass


def automatic_message_sending():
	try:
		chat = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[3]').find_elements(By.CSS_SELECTOR, 'div.YTbUzc')
		global messages_count
		if len(chat) >= minimum_number_of_messages_to_send:
			if messages_count == 0:
				GoogleMeet_send_message("+")
				time.sleep(7)#normal 7
				chat = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[3]').find_elements(By.CSS_SELECTOR, 'div.YTbUzc')
				messages_count = len(chat)
			elif len(chat) >= (messages_count + minimum_number_of_messages_to_send):
				GoogleMeet_send_message("+")
				time.sleep(7) #normal 7
				chat = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[3]').find_elements(By.CSS_SELECTOR, 'div.YTbUzc')
				messages_count = len(chat)
	except:
		pass














def ManageBot():
	while 1:
		for event in longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW:
				if event.to_me:
					request = event.text.lower() #get message from VK

					#Get command and message
					tmp_command = request.split()
					command = tmp_command[0]
					tmp_count = 1
					command_message = ""
					for word in tmp_command:
						if tmp_count != 1:
							command_message = command_message +" "+ str(word)
						tmp_count = tmp_count + 1
					command_message = ' '.join(command_message.split())

					if request == "информация":
						if str(event.user_id) in admin:
							write_msg(event.user_id, "Статус: Админ\n\nДоступные команды:\n▸Подключиться *ссылка*\n▸Отключиться\n▸Написать *сообщение*\n▸Скриншот")
						else:
							write_msg(event.user_id, "Доступные команды:\n")
					elif request == "123":
						automatic_message_sending()
					elif request == "отключиться":
						if str(event.user_id) in admin:
							GoogleMeet_disconntect()
							write_msg(event.user_id, "Отключился")
						else:
							write_msg(event.user_id, "Ошибка доступа")
					elif request == "скриншот":
						if str(event.user_id) in admin:
							Screenshot()
							upload = vk_api.VkUpload(vk)
							photo = upload.photo_messages('screenshot.png')
							owner_id = photo[0]['owner_id']
							photo_id = photo[0]['id']
							access_key = photo[0]['access_key']
							attachment = f'photo{owner_id}_{photo_id}_{access_key}'
							vk.method("messages.send", {"peer_id": event.peer_id, "message": "", "attachment": attachment, "random_id": 0})
						else:
							write_msg(event.user_id, "Ошибка доступа")
					elif command == "подключиться":
						if str(event.user_id) in admin:
							try:
								GoogleMeet_conntect(command_message)
							except:
								write_msg(event.user_id, "Ошибка подключения\nВозможно вы неверно указали ссылку\nПример: Подключиться https://meet.google.com/ffx-dvcy-scp")
						else:
							write_msg(event.user_id, "Ошибка доступа")
					elif command == "написать":
						if str(event.user_id) in admin:
							try:
								GoogleMeet_send_message(command_message)
							except:
								write_msg(event.user_id, "Не удалось отправить сообещние\nВозможны вы не подключились к конференции")
						else:
							write_msg(event.user_id, "Ошибка доступа")
					else:
						write_msg(event.user_id, "Такой команды нет\nНапиши 'Информация', чтобы получить доступные команды")


def Timer():
	while 1:
		
		#Today info
		current_datetime = datetime.now()
		weekday_today = int(current_datetime.isoweekday())
		day_today = current_datetime.day
		month_today = current_datetime.month
		now_hour = current_datetime.hour
		now_minute = current_datetime.minute
		time_now = str(now_hour)+":"+str(now_minute)

		weekday_in_rasp_dict = str(weekday_today)+str(weektype())

		if weekday_in_rasp_dict in rasp.week_day: #Find dict with lessons on needed day of week
			if time_now in rasp.week_day[weekday_in_rasp_dict]: #Check out time now with time in dict today
				for time_in_list in rasp.week_day[weekday_in_rasp_dict]: 
					if time_now == time_in_list: #If now lesson, we connect to google meet link
						GoogleMeet_conntect(rasp.week_day[weekday_in_rasp_dict][time_in_list][0])
		time.sleep(60)



def Automatic_control():
	while 1:
		exit_with_a_minimum_of_users()
		automatic_message_sending()
		time.sleep(1)






GoogleAuth()

t1 = threading.Thread(target=ManageBot)
t2 = threading.Thread(target=Timer)
t3 = threading.Thread(target=Automatic_control)
t1.start()
t2.start()
t3.start()
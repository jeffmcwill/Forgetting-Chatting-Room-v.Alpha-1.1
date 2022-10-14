import threading
import socket
import time

#Proyecto de Conexion TCP a internet (Haciendo un chat anonimo.)


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999)) #ejecutar una vez, si se ejecuta 2 veces dara error siempre.

server.listen()

#.........................................................................

clients = []
nicknames = []

def broadcast(message):
	for client in clients:
		client.send(message)

def handle(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f"\n {nickname} se ha desconectado!".encode('ascii'))
			nicknames.remove(nickname)
			break

def receive():
	while True:
		client, address = server.accept()
		print("--------------------------------")
		print(f"se ha conectado {str(address)}")
		print("--------------------------------")

		client.send("NICK".encode('ascii'))
		nickname = client.recv(1024).decode('ascii')
		nicknames.append(nickname)
		clients.append(client)

		print("--------------------------------")
		print(f"el nombre del cliente es {nickname}!")
		broadcast(f"{nickname} ha entrado al chat, Saludenlo!".encode('ascii'))
		client.send("\n------------------------------------".encode('ascii'))
		client.send("\nte has conectado a la sala de chat!".encode('ascii'))
		client.send("\n_Reglas para el usuario: ".encode('ascii'))
		client.send("\n1. Prohibido usar *Enie* dara error al usuario.".encode('ascii'))
		client.send("\n2. Se puede usar cualquier version del archivo cliente para charlar aqui.".encode('ascii'))
		client.send("\n3. Recuerda que el chat se borra automaticamente al cerrarse.".encode('ascii'))
		client.send("\n4. se puede ejecutar tambien en dispositivos android.".encode('ascii'))
		client.send("\n------------------------------------".encode('ascii'))
		print("----------------------------------------------------")
		print(f"Usuarios conectados: {nicknames}")

		thread = threading.Thread(target=handle,args=(client,))
		thread.start()

print("El servidor esta listo para usarse.")
time.sleep(1)
print("------------------------------------")
time.sleep(1)
print("Esperando a los usuarios o clientes...")
receive()









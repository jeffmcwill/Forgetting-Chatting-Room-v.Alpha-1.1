import threading
import socket

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
		print("----------------------------------------------------")
		client.send("\nte has conectado!".encode('ascii'))
		print("----------------------------------------------------")

		thread = threading.Thread(target=handle,args=(client,))
		thread.start()

print("El servidor esta listo para usarse.")
print("------------------------------------")
print("Esperado usuarios o clientes...")
receive()









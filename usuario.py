import threading
import socket

#proyecto de conecxion y chatting entre tcp y puertos para uso entre usuarios
#con el codigo que se pide al principio. aun en desarrollo.
#------------------------------------------------------------------------------

print("""
 __i
|---|    
|[_]|    
|:::|   - Forgetting Chatting Room V.1.1 alpha - 
|:::|    
`\   \   
  \_=_\

----------------------------------------------------------""")
print("chatting privado entre usuarios y TCPS (Modelo Intranet).")
print("----------------------------------------------------------")

nickname=input("*elije el nombre que te guste para entrar al chat: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#requiere el FORWAIRDING (aparece al ejecutar el comando ngrok.exe tcp 9999)
#tcp://0.tcp.sa.ngrok.io:15856#

print("---------------------------------")
print("Ejemplo asi: 0.tcp.sa.ngrok.io")
tcp=input("dame el TCP *sin el http ni los dos puntos*: ")
portal=int(input("dame el numero de puerto: "))
print("----------------------------------")

#client.connect(("0.tcp.sa.ngrok.io",15856)) tendria que ser asi pero le añadi los input 
#para que no tengamos que ir modificando este archivo a cada rato.

client.connect((tcp,portal))
print("Todo correcto :3")

#lamentablemente por motivos de seguridad o por que el socket suele variar, cada vez que
#apaguemos el servidor o cerremos el cmd, tendremos que cambiar el client.

#print(client.recv(1024).decode())
#client.send("Hey server".encode())

#..............................................................................

def receive():
	while True:
		try:
			message=client.recv(1024).decode('ascii')
			if message == "NICK":
				client.send(nickname.encode('ascii'))
			else:
				print(message)
		except:
			print("¡Un error ocurrio, cierra la pestaña y vuelve a ejecutarlo!")
			client.close()
			break

def write():
	while True:
		message=(f'{nickname} :{input(" ")}')
		client.send(message.encode('ascii'))
		print("-")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_theread = threading.Thread(target=write)
write_theread.start()
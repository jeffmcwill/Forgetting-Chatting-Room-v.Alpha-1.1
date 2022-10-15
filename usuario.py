import threading
import socket
import time

#proyecto de coneccion y chatting entre tcp y puertos para uso entre usuarios
#con el codigo que se pide al principio. aun en desarrollo.
#------------------------------------------------------------------------------

print("""
 __i
|---|    
|[_]|    
|:::|   - TCP Chatting Room V.1.2.1 alpha - 
|:::|    		By Jeff McWill.
`\   \   
  \_=_\

----------------------------------------------------------""")
time.sleep(1)
print("chatting privado entre usuarios y TCPS (Modelo Intranet).")
time.sleep(1)
print("----------------------------------------------------------")
time.sleep(1)
nickname=input("*elije el nombre que te guste para entrar al chat: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#requiere el FORWAIRDING (aparece al ejecutar el comando ngrok.exe tcp 9999)
#tcp://0.tcp.sa.ngrok.io:15856#

print("""--------------------------------------------------------------------
Esta conexion funciona con el sistema de Ngrok, que permite usar una pc como
servidor, y permitir el uso de archivos locales como abierto a las personas
que le pasen el codigo y puerto.
*Ejemplo asi: 0.tcp.sa.ngrok.io y puerto: 15232* 
--------------------------------------------------------------------""")
tcp=input("dame el TCP *sin el http ni los dos puntos*: ")
print("--------------------------------------------------")
portal=int(input("dame el numero de puerto: "))
print("----------------------------------------")

#client.connect(("0.tcp.sa.ngrok.io",15856)) tendria que ser asi pero le añadi los input 
#para que no tengamos que ir modificando este archivo a cada rato.
try:
	client.connect((tcp,portal))
	print("Todo correcto :3")
except:
	print("No se encuentra el servidor disponible, reintentalo de nuevo.")

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
			print("¡Un error ocurrio, cierra la pestaña y vuelve a ejecutar el servidor!")
			client.close()
			break

def write():
	while True:
		message=(f'{nickname}: {input(" ")}')
		client.send(message.encode('ascii'))
		print("-")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_theread = threading.Thread(target=write)
write_theread.start()

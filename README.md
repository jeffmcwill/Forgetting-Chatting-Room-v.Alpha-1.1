# Forgetting-Chatting-Room-v.Alpha-1.1 (Funcional/Comp con Pydroid3)

este es un proyecto hecho enteramente en python. es un chatting room que utiliza un servidor (que puede ser nuestra pc) y un archivo usuario, ambos en python, 
para que se puedan conectar por medio de Sockets y Ngrok a una sala de chat.

Pasos a seguir...

este programa es compatible con cualquier dispositivo (inclusive android) que 
use python y tenga el archivo usuario.py
.Necesitas tener cuenta en Ngrok (solo el usuario que vaya a ser admin/server)
.Los demas participantes que quieran entrar solo necesitan tener python,
el archivo usuario.py y el codigo tcp y puerto para poder conectarse 
remotamente. (no necesitan cuenta en ngrok,aclaro.)

---------------------------------------------------------------------------
1. para conectarlo requieres de usar el cmd, ir a la carpeta donde esta el
nGROw 
cd (*lugar donde dejaste los archivos de python y el exe de ngrow*)
todos los archivos tanto el Ngrok.exe y server.py y usuario.py deben estar em
el mismo lugar.
_pon el comando 
python -m http.server 9999
esto abrira un servidor en python en el puerto 9999

2. ya en otra ventana cmd debes de ejecutar el "ngrow":
_cd (blalblal)
y el comando
_ngrok.exe http 9999

3. despues en el lugar donde ejecutamos el local 9999 de python
tenemos que presionar el CRTL + C para que nos permita usar el teclado.
y luego poner el comando.
ngrok tcp 9999

*en caso de error ir aqui
https://infinitbility.com/how-to-fix-ngrok-your-account-is-limited-to-1-
simultaneous-ngrok-client-session-issue/
*o pon: tskill /A ngrok

*listo ambos canales conectados
ahora lo que queda es ir a un cmd y ejecutar el archivo server.py
despues las personas que quieran entrar al chat.
deben ejecutar el client.py para entrar y hablar.
aunque esto de ejecutarlo en cmd es opcional, se pueden ejecutar ambos archivos
con doble click.
funciona tambien en la version de pydroid de android, solo ejecuta el archivo
usuario y lo dejara entrar. 

ejemplos:
tcp: 0.tcp.sa.ngrok.io
porta: 13000

ADVERTENCIA: esta es una primera version de este programa, lo ire actualizando con el paso del tiempo, funciona pero tiene varios bugs que seran corregidos 
proximamente.

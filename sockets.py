#!/usr/bin/env python
 
#importamos el modulo para trabajar con sockets
import socket
 
#Creamos un objeto socket para el servidor. Podemos dejarlo sin parametros pero si 
#quieren pueden pasarlos de la manera server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
 
#Nos conectamos al servidor con el metodo connect. Tiene dos parametros
#El primero es la IP del servidor y el segundo el puerto de conexion
s.connect(("192.168.1.x", 9999))
 
#Creamos un bucle para retener la conexion
while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    mensaje = raw_input("Mensaje a enviar &gt;&gt; ")
 
    #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
    s.send(mensaje)
 
    #Si por alguna razon el mensaje es close cerramos la conexion
    if mensaje == "close":
        break
 
#Imprimimos la palabra Adios para cuando se cierre la conexion
print "Adios."
 
#Cerramos la instancia del objeto servidor
s.close()
Ahora vamos a programar el servidor:

#!/usr/bin/env python
 
#importamos el modulo socket
import socket
 
#instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
#Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind(("", 9999))
 
#Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
#El numero de conexiones entrantes que vamos a aceptar
s.listen(1)
 
#Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este 
#devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
sc, addr = s.accept()
 
 
while True:
 
    #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro 
    #la cantidad de bytes para recibir
    recibido = sc.recv(1024)
 
    #Si el mensaje recibido es la palabra close se cierra la aplicacion
    if recibido == "close":
        break
 
    #Si se reciben datos nos muestra la IP y el mensaje recibido
    print str(addr[0]) + " dice: ", recibido
 
    #Devolvemos el mensaje al cliente
    sc.send(recibido)
print "Adios."
 
#Cerramos la instancia del socket cliente y servidor
sc.close()
s.close()
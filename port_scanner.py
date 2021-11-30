#Escaner de Puertos
#Importamos los Módulos requeridos
import sys
import socket
from datetime import datetime

# Especificamos el target; debe ser escrito después del comando
if len(sys.argv) == 2:

   # Hacemos resolución de nombre hacia IP
   target = socket.gethostbyname(sys.argv[1])

#Si la resolución es posible, entonces continuamos, de lo contrario entramos al else:
else:
    print("Datos Insuficientes")
    exit()

#Agregamos graficación
#Escribimos 50 guiones
print("*" * 50)

#Escribimos las acciones realizadas
print("Analizando el Objetivo: " + target)

#Escribimos la Fecha y la hora de inicio
print("Análisis iniciado :" + str(datetime.now()))

#Escribimos 50 guiones
print("*" * 50)

#try nos permite controlar los errores si algo falla
try:
  # Analizamos los puertos del 1 al 65,535 por medio de un ciclo
    for port in range(1, 65535):
        #Creamos el Socket de conexión hacia cada puerto y lo llamamos "s"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Definimos un Timeout
        socket.setdefaulttimeout(1)
        #Hacemos la conexión al puerto y le asignamos la variable result
        result = s.connect_ex((target, port))
        #Hacemos la prueba lógica para saber si el puerto está abierto o no
        if result == 0:
            #Si está abierto escibimos el resultado
            print("El Puerto {} está abierto".format(port))
        #Cerramos la conexión
        s.close()

#Manejamos las excepciones, por ejemplo "CTRL+C"
except KeyboardInterrupt:
    print("\n Cerrando el Programa !!!")
    sys.exit()
#Si no podemos resolver el host:
except socket.gaierror:
    print("\n El Nombre del host no puede ser resuelto!!!")
    sys.exit()
#Si no podemos contactar al servidor:
except socket.error:
    print('\n Host No Responde!!!')
    sys.exit()

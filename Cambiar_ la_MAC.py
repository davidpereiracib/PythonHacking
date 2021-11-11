#Debes colocar como nombre de este archivo: main.py, por que de lo contrario no funcionaría; en el próximo video explico en más detalle.


if __name__ == '__main__':
    interfase="eth0"
    nueva_MAC="22:11:33:44:55:14"
    print("Desactivando la interfase")
    subprocess.run(["ifconfig","eth0","down"])
    print("Cambiando la direccion MAC de la interfase:", interfase, " a ", nueva_MAC)
    subprocess.run(["ifconfig",interfase, "hw","ether",nueva_MAC])
    print("La direccion MAC cambio a: ", nueva_MAC)
    subprocess.run(["ifconfig",interfase, "up"])
    print("La Interfase esta lista")
    subprocess.run(["ifconfig"])

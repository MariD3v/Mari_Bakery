'''
Features: 

•   El cliente puede decidir pedir varias veces ✅
•	Hacer un generador aleatorio de pedidos. ✅
•	Anotar los pedidos de forma organizada, siguiendo la plantilla del establecimiento y almacenandose
    en el fichero de cada dia.✅
•	Hay un número finito de mesas (4). Después de servidos, los clientes se levantarán espontáneamente liberando las mesas. 
•	Crear función limpiar mesas.

Objetivos:

Después de un tiempo dado
•	¿Cuáles han sido los ingresos de la pastelería? ✅
•	¿Cuántas mesas se limpiaron en el tiempo de jornada? 
'''
import random
from datetime import datetime
import os

lista_pasteles = ['Choco', 'Naranja', 'Quesito', 'Choco Blanco']

def anotar_pedidos(nombre, sabores, precio):
    ahora = datetime.now()
    fecha_pedidos = str('_' + str(ahora.day) + '_' + str(ahora.month) + '_' + str(ahora.year))
    url_archivo = str('database/Pedidos' + fecha_pedidos + '.txt')

    if os.path.isfile(url_archivo): #Si ya hay creado un fichero de hoy
        archivo_txt = open(url_archivo, 'a+')
        cliente = nombre
        pedido = sabores
        cuenta = precio
        archivo_txt.write('\nCliente: ' + cliente + '\nPedido: ' + pedido + '\nCuenta: ' + str(cuenta) + '\n')
        archivo_txt.close()

    else: #Si no hay ningún fichero de hoy creado aun
        archivo_txt = open(url_archivo, 'x') #Lo creamos
        archivo_txt.close()
        archivo_txt = open(url_archivo, 'a+') #Lo abrimos y añadimos la información
        cliente = nombre
        pedido = sabores
        cuenta = precio
        archivo_txt.write('\nCliente: ' + cliente + '\nPedido: ' + pedido + '\nCuenta: ' + str(cuenta) + '\n')
        archivo_txt.close()
        
def generador_pedidos():
    sabor = random.choice(lista_pasteles)
    return sabor

def listaSabores():

    for sabores in lista_pasteles:
        print("\t-", sabores)
    else:
        print('Si necesitas un sabor en especifico dimelo')

def dinero(sabor):
    ganancias = 0
    if sabor.lower() == 'choco':
        precio = 10
        ganancias += precio
    elif sabor.lower() == 'naranja':
        precio = 12
        ganancias += precio
    elif sabor.lower() == 'quesito':
        precio = 15
        ganancias += precio
    elif sabor.lower() == 'choco blanco':
        precio = 18
        ganancias += precio
    else: #Resto de sabores
        precio = 20
        ganancias += precio
    return ganancias

def pasteleria_main():
    ganancias = 0

    #Primer cliente
    print('Bienvenido/a a la Pasteleria de Mari')
    name = input('¿Cuál es tu nombre? ')
    print('Encantada de conocerte', name, 'Aqui podemos ofrecerte gran variedad de pastelines')
    generador = input('¿Deseas que te aconseje un sabor? ')
    if generador.lower() == 'si':
        saborEscogido = generador_pedidos()
    else:
        print('¿De que sabor quieres tu pastel? Tenemos los siguientes sabores:')
        listaSabores() 
        saborEscogido = input()
    ganancias += dinero(saborEscogido)
    print('Muy bien! Pastelín de',saborEscogido,'saliendo!')
    anotar_pedidos(name, saborEscogido, dinero(saborEscogido))

    repetir = input('¿Quiéres algo más? ' )
    while repetir.lower() == 'si':
        saborEscogido = input('¿De que sabor quieres tu nuevo pastel? ')
        ganancias += dinero(saborEscogido)
        print('Muy bien! Pastelín de',saborEscogido,'saliendo!')
        repetir = input('¿Quiéres algo más? ')
        print('Que tengas un buen dia.🥰')
        anotar_pedidos(name, saborEscogido, dinero(saborEscogido))

    nuevo_cliente = input('¿Hay algún cliente más? ')

    #El resto de clientes
    while nuevo_cliente.lower() == 'si':
        print('Bienvenido/a a la Pasteleria de Mari')
        name = input('¿Cuál es tu nombre? ')
        print('Encantada de conocerte', name, 'Aqui podemos ofrecerte gran variedad de pastelines')
        print('¿Quieres que te aconseje un sabor? ')
        generador = input()
        if generador.lower() == 'si':
            saborEscogido = generador_pedidos()
        else:
            print('¿De que sabor quieres tu pastel? Tenemos los siguientes sabores:')
            listaSabores() 
            saborEscogido = input()
        ganancias += dinero(saborEscogido)
        print('Muy bien! Pastelín de',saborEscogido,'saliendo!')
        anotar_pedidos(name, saborEscogido, dinero(saborEscogido))
        print('¿Quiéres algo más? ')
        repetir = input()
        while repetir.lower() == 'si':
            saborEscogido = input('¿De que sabor quieres tu nuevo pastel? ')
            ganancias += dinero(saborEscogido)
            print('Muy bien! Pastelín de',saborEscogido,'saliendo!')
            anotar_pedidos(name, saborEscogido, dinero(saborEscogido))
            repetir = input('¿Quiéres algo más? ')
        print('Que tengas un buen dia.🥰')
        nuevo_cliente = input('¿Hay algún cliente más? ')
        

    #Cuando no hay más clientes
    print('Entonces me tomo un descanso 🥰' + '\nLas ganancias del dia son ' + str(ganancias) + ' euros.')

pasteleria_main()


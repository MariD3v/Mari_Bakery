def listaSabores():

    for sabores in lista_pasteles:
        print("\t-", sabores)
    else:
        print('Si necesitas un sabor en especifico dimelo')

#Primer cliente    
lista_pasteles = ['Choco', 'Naranja', 'Quesito', 'Choco Blanco']
print('Bienvenido/a a la Pasteleria de Mari')
name = input('¿Cuál es tu nombre? ')
print('Encantada de conocerte', name, 'Aqui podemos ofrecerte gran variedad de pastelines')
print('¿De que sabor quieres tu pastel? Tenemos los siguientes sabores:')
listaSabores() 
saborEscogido = input()
print('Muy bien! Pastelín de',saborEscogido,'saliendo!')
nuevo_cliente = input('¿Hay algún cliente más? ')

#El resto de clientes
while nuevo_cliente.lower() == 'si':
    print('Bienvenido/a a la Pasteleria de Mari')
    name = input('¿Cuál es tu nombre? ')
    print('Encantada de conocerte', name, 'Aqui podemos ofrecerte gran variedad de pastelines')
    print('¿De que sabor quieres tu pastel? Tenemos los siguientes sabores:')
    listaSabores() 
    saborEscogido = input()
    print('Muy bien! Pastelín de',saborEscogido,'saliendo!')
    nuevo_cliente = input('¿Hay algún cliente más? ')

#Cuando no hay más clientes
print('Entonces me tomo un descanso 🥰')

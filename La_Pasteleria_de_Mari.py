lista_pasteles = ['Choco', 'Nalanja', 'Quezito', 'Choco Blanco']

print('Bienvenido/a a la Pasteleria de Mari')
name = input('¿Cuál es tu nombre?')
print('Encantada de conocerte', name, 'Aqui podemos ofrecerte gran variedad de pastelines')
print('¿De que sabor quieres tu pastel? Tenemos los siguientes sabores')
for sabores in lista_pasteles:
    print(sabores)
else:
    print('Si necesitas un sabor en especifico dimelo')

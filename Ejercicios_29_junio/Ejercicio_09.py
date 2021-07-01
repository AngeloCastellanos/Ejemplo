edad = int(input('Ingrese edad: '))

if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10

print('El precio de la entrada es: ', precio, 'euros, ', 'porque su edad es de: ', edad)
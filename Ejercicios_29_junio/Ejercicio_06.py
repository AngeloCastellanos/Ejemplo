var1 = '1234'

mensaje = ''

while var1 != mensaje:
  mensaje = input('Ingrese contraseña: ')
  if  var1 != mensaje:
      print('Contraseña incorrecta.')
  
print('La contraseña es correcta.', var1)


while True:
    frase = input('Introduce algo:')
    if frase == 'salir':
        break
    print(frase)
alpabeto = 'abcdefghijklmnopqrstuvwxyz'

print('f' in alpabeto)
print('F' in alpabeto)
print('1' in alpabeto)
print('ghi' in alpabeto)
print('Xyz' in alpabeto)

alpabeto = 'a' + alpabeto
alpabeto = alpabeto + 'z'

print(alpabeto)

print('lambda30'.isalnum())
print('lambda30'.isalpha())
print('lambda30'.isdigit())
print('lambda30'.islower())
print('lambda30'.isspace())
print('MAY'.isupper())
print('Bienvenidos al curso '.split())
print('Bienvenidos al curso '.swapcase())
print('Bienvenidos al curso '.title())
print('Bienvenidos al curso '.upper())

lista = ['omega', 'alfa', 'pi', 'gama']
print(lista)
lista.sort()
print(lista)
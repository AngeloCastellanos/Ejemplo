num1 = int(input('Ingrese primer número: '))
num2 = int(input('Ingrese segundo número: '))

try:
    division = num1/num2
    print('División: ', division)
except ZeroDivisionError:
    print('Error división entre 0')
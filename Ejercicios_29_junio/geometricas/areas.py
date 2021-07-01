import math

def areaCuadrado():
    ladoC = float(input('Ingrese el valor del lado: '))
    return print('El area del cuadrado es: ', pow(ladoC, 2))

def areaRectangulo():
    lado1 = float(input('Ingrese el valor del lado uno: '))
    lado2 = float(input('Ingrese el valor del lado dos: '))
    return print('El area del rectangulo es: ', lado1*lado2)

def areaCirculo():
    pi = 3.1416
    lado = float(input('Ingrese el valor del radio: '))
    return print('El area del circulo es: ', pi*pow(lado, 2))

if __name__ == ('__main__'):
    print('Estoy en la función principal.')
    
else:
    print('En este momento me comporto como un modulo')
def perCuadrado():
    lado = float(input('Ingrese el valor del lado: '))
    return print('El perimetro del cuadrado es: ', 4 * lado)

def perRectangulo():
    long1 = float(input('Ingrese el valor del longitud uno: '))
    long2 = float(input('Ingrese el valor del longitud dos: '))
    return print('El perimetro del cuadrado es: ', (2*long1)*(2*long2))

def perCirculo():
    pi = 3.1416
    radio = float(input('Ingrese el valor del radio: '))
    return print('El perimetro del circulo es: ', 2 * pi * radio)

if __name__ == ('__main__'):
    print('Estoy en la función principal.')
    perCuadrado()
    perRectangulo()
    perCirculo()
    
else:
    print('En este momento me comporto como un modulo')
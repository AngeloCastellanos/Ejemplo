nombre = str(input('¿Como te llamas?'))
edad = int(input('¿Cuantos años tienes?'))
direccion = str(input('¿Cual es tu dirección?'))
telefono = int(input('¿Cual es tu numero de telefono?'))

persona = {'nombre: ' : nombre,
            'edad: ' : edad,
            'direccion: ' : direccion,
            'telefono: ' : telefono}

print(nombre['nombre'], 'tiene', 
persona['edad'], 'años, vive en ',
persona['direccion'], ' y su numero de telefono es', 
persona['telefono'])
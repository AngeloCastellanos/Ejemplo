"""ca_a = float(input("Inserta long primer cateto: "))
ca_b = float(input("Inserta long segundo cateto: "))

hipo = (ca_a ** 2 + ca_b ** 2) ** .5

print(hipo)

myList = [4,3,5.8,False,"hola"]
'print("Lista 1: ", myList)
'print("Lista 2: ", myList[4])
'myList[1] = "curso"
'print("Lista 3: ", myList)
'myList[0] = myList[4]
'print("Lista 4: ", myList)
>>>del myList[4]
>>>print("Lista 5: ", myList)


numbers = [1,2,3,4,5]
print(numbers)

algo = int(input('Ingrese número a reemplazar: '))
numbers[2] = algo
print('Lista 1: ', numbers)

del numbers[4] 
print('Lista 2: ', numbers)

print('Lista 3: ', len(numbers))


myList = [4,3,5.8,False,"hola"]
print("Lista 1: ", myList)

myList.append(9)
print('Lista 2: ', myList)

myList.append(10)
print('Lista 3: ', myList)

myList.extend(range(11,14))
print('Lista 4: ', myList)

conteo = myList.count(5)
print('Conteo: ', conteo)

myList.insert(9, True)
print('Lista 5: ', myList)

myList.remove(12)
print('Lista 6: ', myList)

---------

myList = []

for i in range(7):
    myList.append(i+1)
print(myList)

myList.reverse()
print(myList)

myList.sort()
print(myList)

ubicacion = myList.index(3)
print(ubicacion)

myList.pop(ubicacion)
print(myList)


**********

#otro
lista1 = [1,2,3,4]
lista2 = [1,2,3,4]
lista3 = lista1, [1,2,3,4]

lista1.append(6)
print('Lista 1: ', lista1, 'Mem: ', id(lista1))
print('Lista 2: ', lista2, 'Mem: ', id(lista2))
print('Lista 3: ', lista3, 'Mem: ', id(lista3))

-------------
myList = [10,8,6,4,2]
newList = myList[1:3]

print(newList)


----

myList = [10,8,6,4,2]

myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]

print(myList)

--------

a = 'D'
b = 'F'
c = 'Z'
d = 'A'

lst = [a, b, c, d]
lst.sort()

print(lst)


----------------

#otro
def saludo():
    print('Bienveniso al curso.')
    print('Diplomado')

for i in range(3):
    saludo()

******

def mensaje():
    print('Este es un mensaje inicial.')

print('Inicio')
mensaje()
print('Fin.')

*******


dir(math)
def sum(a,b,c):
    print(a, "+", b, "+", c, "=", a + b + c)


sum(1,2,3)
sum(c = 1, a = 2, b = 3)
sum(3, c = 1, b = 2)
sum(3, b = 1, c = 2)
sum(4, 3, c = 2)
sum(4, b = 3, c = 2)"""

#otro

def introduction(firstname, lastname = 'Smith'):
    print('Hello, my name is,', firstname, lastname)

introduction('John', 'Doe')
introduction('John')
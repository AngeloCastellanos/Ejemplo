
#otro

"""def saludo():
    print("Bienvenidos al curso")
    return "hola"

x = saludo()

print("El retorno de la función. Es: ", x)

-----
valor = None
def strangeFunction(n):
    if(n % 2 == 0):
        return "es par"

print(strangeFunction(2))
----
def sumOfList(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum

print(sumOfList([5,4,3]))
print(sumOfList({5}))
-----
def strangeList(n):
    strangeList = []
    for i in range(0, n):
        strangeList.insert(0, i)
    return strangeList

print(strangeList(5))
----
def scopeTest():
    x = 123

scopeTest()
print(x)

---


def miFunction():
    global var
    var = 2
    print('¿Conozco a la variable?', var)


var = 1
miFunction()
print(var)

----

def miFuncion(n):
    print("Yo obtuve", n)
    n += 1
    print("Yo ahora tengo", n)

var = 1
miFuncion(var)
print(var)
---

def imc(peso, altura):
    return peso / altura ** 2

print(imc(2,5))

---

def esUnTriangulo(a,b,c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(esUnTriangulo(1, 1, 1))
print(esUnTriangulo(1, 1, 3))

---------

def esUnTriangulo(a,b,c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a,b,c):
    print("Felicidades, puede ser un triangulo.")
else:
    print("Lo siento, no puede ser un triangulo.")

--------

def enter_number(i: int):
    return int(input(f"Digite numero: {i + 1}: "))
def multiplicar(lst: list):
    res = 1
    
    for i in range(len(lst)):
        res *= lst[i]
        
    return res
print("Bienvenido a la multiplicación")
lst = []
for i in range(5):
    lst.append(enter_number(i))
print(lst)
print("La multiplicación es:", multiplicar(lst))

dict = {'cat':'chat','dog':'chien','horse':'cheval'}

phoneNumbers = {'boss' : 532616487, 'suzy' : 98764513}

emptyDictionary = {}

print(dict)

"""
diccionario = {"clave1":234,
    "clave2":True,
    "Clave3":"Valor 1",
    "Clave4":[1,2,3,4]
    }

print('1. ',diccionario)
print('2. ',type(diccionario))
print('3. ',len(diccionario))
print('4. ',diccionario["clave1"])
print('5. ',diccionario.keys())
print('6. ',sorted(diccionario.keys()))
print('7. ',diccionario.items())
print('8. ',diccionario.values())
print('9. ',diccionario)
diccionario[4]="Color"
print('10. ',diccionario)
print('10. ',diccionario.popitem())
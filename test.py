lst = [1,2]

for v in range(2):
    lst.insert(-1, lst[v])

print(lst)

nums = [1,2,3]
vals = nums

print(nums)
print(vals)

var1 = 2
var2 = 3


def func1(a):
    return None

def func2(a):
    return func1(a)*func1(a)

print(func2(2))

print(1//2)

def func(a,b):
    return b ** a

print(func(b=2, 2))


z = 0
y = 10
x = y < z and z > y or y > z and z < y

print(x)

IN = ''

print(In)

list = [x * x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(list))

a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)


nums = [1,2,3]
vals = nums
del vals[:]

print(vals)

x = int(input())
y = int(input())
x= x % y
x= x % y
y= y % x

print(y)


y = input()
x = input()
print(x + y)

print("a", "b", "c", sep="sep")

x = 1 // 5 + 1 / 5
print(x)

tuple[1] = tuple[1]+tuple[0]

x = float(input())
y = float(input())
print(y ** (1 / x))


dct = {'uno':'dos', 'tres':'uno', 'dos':'tres'}
v = dct['tres']

for k in range(len(dct)):
    v = dct[v]

print(v)

lst = [i for i in range(-1,-2)]

print(lst)


def fun(a,b, c = 0):
    return fun()

print(fun(b=1))



def fun(x,y):
    if x == y:
        return x
    else:
        return fun(x, y-1)

print(fun(0,3))



i = 0
while i < i + 2:
    i += 1
    print("*")
else:
    print("*")


tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

dd = {"1":"0", "0":"1"}
for x in dd.vals():_


dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)

for x in dct.keys():
    print(dct[x][1],end="")


def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
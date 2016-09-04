import random

"""
In order to make HASHING works ---> Hashing HomoMorphism must APPLY
Redefine functionality + Redefine Hash
Hash Functions have to be made equality otherwise it won't work


Math Rule:      x == y  implies  Hash(x) == Hash(y)

Contrapositive: x != y      implies     Hash(x) != Hash(y)

The equivivelence class is defined by HashFunc() not the objects consuming HashFunc()
"""


class MyStr(str):
    'Make the kind of String that does CASE-INSENSITIVE Comparision'

    def __eq__(self, other):
        return self.lower() == other.lower()

    def __hash__(self):
        return hash(self.lower())


class MyInt(int):
    'randomize hash'

    def __hash__(self):
        return random.randrange(1000)


names = map(str, 'Jigar is taking python training Again jigar'.split())
print(set(names))

names = map(MyStr, 'Jigar is taking python training Again jigar'.split())
print(set(names))

if hash(MyStr("Jigar")) == hash(MyStr("jiGar")):
    print(True)

# Try this after removing __hash__ from MyStr definition, won't work because Hashing HomoMorphism broke
if MyStr("Jigar") == MyStr("jiGar"):
    print(True)

# Funny, set didn't remove duplicate 10, Why! ?? Ans: __hash__ randomized
values = [10, 20, 30, 40, 10]
print(set(map(MyInt, values)))

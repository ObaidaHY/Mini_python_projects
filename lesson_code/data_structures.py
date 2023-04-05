text = "Hello World!"

# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
print(list(text))

# {'H', 'W', 'o', ' ', 'l', 'r', '!', 'e', 'd'}
print(set(text))

# ['H','e']
list_a = list(text)
print(list_a[:2])

# TypeError: 'set' object is not subscriptable
set_a = set(text)
set_a.add(3)
# print(set_a[:2])

# [1,2,3,4,5]
list_a.append(5)
print(list_a)

# AttributeError: 'tuple' object has no attribute 'append'
tuple_a = (1, 2, 3, 4)
# tuple_a.append(5)
print(tuple_a)
print(tuple_a[::-1])

# <class 'dict'>
a = {}
print(type(a))

# <class 'set'>
b = set()
print(type(b))

# <class 'set'>
c = set({})
print(type(c))

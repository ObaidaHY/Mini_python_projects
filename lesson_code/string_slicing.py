parrot = "Norwegian Blue"

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,432;432:543 534,780"
separators = number[1::4]
print(separators)

values = "".join(char for char in number).split()
print(f'the values are {values}')

values = "".join(char if char not in separators
                 else " " for char in number)
print(f'the values are {values}')

values = "".join(char if char not in separators
                 else " " for char in number).split()
print(f'the values are {values}')

print(parrot[-4:-2])
print(parrot[-4:12])
print(parrot[14:0:-1])
print(parrot[0:14:-1])

print(parrot[14::-1])
print(parrot[::-1])
print(parrot[::1])
print(parrot[:-1])
print(parrot[:1])

print(parrot[0:6])
print(parrot[3:5])
print(parrot[10:])
print(parrot[:])

print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[-14])

message_one = " Hello world "
message_two = " Hi there Josh "

# file = open('file.txt', 'a')
# print(message_one, file=file)
# file.close()

# a Open for writing at end (file created)
with open('file.txt', 'a') as file:
    file.write(message_one)

# a+ Open for reading & writing at end (file created)
with open('file.txt', 'a+') as file:
    file.write(message_two)
    file.seek(0)
    print(file.read())

# r Open for reading at start (file not created)
with open('file.txt', 'r') as file:
    print(file.read())

# r+ Open for reading & writing at start (file not created)
with open('file.txt', 'r+') as file:
    file.write(message_two * 2)
    file.seek(0)
    print(file.read())

# w Truncate file to zero/nil & open for writing (file created)
with open('file.txt', 'w') as file:
    file.write(message_two)

# w+ Truncate file to zero/nil & open for writing & reading (file created)
with open('file.txt', 'w+') as file:
    file.write(message_two * 2)
    file.seek(0)
    print(file.read())

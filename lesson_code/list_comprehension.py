# squares = []
# for x in range(10):
#     squares.append(x ** 2)

squares = [x ** 2 for x in range(10)]
print(squares)

# print(10) if 1 == 1 else print("yes")
# i = 19 if 1 == 1 else print("yes")

my_list = [1, 2, 3]

# list_to_print = []
# for elem in my_list:
#     if elem % 2 > 0:
#         list_to_print.append(elem)
#     else:
#         list_to_print.append("")
# print(list_to_print)

print([elem if elem % 2 > 0 else "" for elem in my_list])
print([elem for elem in my_list if elem % 2 > 0])

list_comp = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(list_comp)

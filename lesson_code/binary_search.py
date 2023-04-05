import random


# used to learn/test debug tool functionality
def print_msg(num):
    print(f"num is {num} - printed with user-function")


def find_value(col, low, high, num_to_find):
    # if low <= high:
    while low <= high:  # 0 (log n)
        middle = (low + high) // 2

        if col[middle] == num_to_find:
            return middle

        elif col[middle] < num_to_find:
            low = middle + 1
            # return find_value(col, low, high, num_to_find)

        else:
            high = middle - 1
            # return find_value(col, low, high, num_to_find)
    return -1


collection = []
lowest_index = 0
# number_to_find = 27
collection_size = random.randint(10, 100)

for i in range(collection_size):
    last_value = 0 if len(collection) == 0 else collection[-1]
    rand_value = random.randint(last_value, i * 10)
    print(f"rand_value is {rand_value}")
    collection.append(rand_value)

number_to_find = collection[random.randrange(collection_size)]
print(f"collection length is {len(collection)}")
print_msg(number_to_find)

result_index = find_value(collection, lowest_index, len(collection) - 1, number_to_find)

if result_index == -1:
    print("This item was not found in the list")
else:
    print(f"The number {number_to_find} was found at index position {result_index}")

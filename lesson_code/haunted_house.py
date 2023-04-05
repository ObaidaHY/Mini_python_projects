import random

all_exits = ["north", "south", "east", "west", "up", "down", "left", "right"]
opposite_exit = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east',
                 'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', }

random_index = random.randrange(len(all_exits))
correct_exit = all_exits[random_index]
attempt_counter = 0
exit_choice = ""

print("You are stuck in a haunted house with one exit. If you don't escape, you're in big trouble.")


def print_opposite():
    print(f"Opposite direction of {opposite_exit[correct_exit]}")


def print_first_letter():
    print(f"The exit starts with {correct_exit[0]}")


def print_backwards():
    print(f"{correct_exit[::-1]} backwards")


def print_cardinal():
    if correct_exit in all_exits[:4]:
        print(f"The exit is in one of the four cardinal directions")
    else:
        print(f"The exit is in a body relative direction")


hint_list = [print_opposite, print_first_letter, print_cardinal, print_backwards]

while exit_choice.casefold() != correct_exit:
    if attempt_counter >= 3 and hint_list:
        hint_choice = input("Would you like a hint: ")
        if hint_choice.casefold() == 'yes':
            hint_function = random.choice(hint_list)
            hint_function()
            hint_list.remove(hint_function)
            attempt_counter = 0

    exit_choice = input("Please choose an exit: ")
    # Code below changes the exit everytime to increase difficulty
    # random_index = random.randrange(len(all_exits))
    # correct_exit = all_exits[random_index]
    if exit_choice.casefold() == correct_exit:
        print("You have escaped")
    if exit_choice.casefold() == "quit":
        print("Game Over")
        break

    attempt_counter += 1

# else:
#     print("you have escaped with else")

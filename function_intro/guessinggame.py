import random

guess = 0
highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
print("Please guess number between 1 and {}: ".format(highest))


def get_integer(prompt):
    """
    Get an integer from the standard Input (stdin)

    The function will continue looping, and prompting
    the user, until a valid int is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{} is not a number".format(temp))


while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")

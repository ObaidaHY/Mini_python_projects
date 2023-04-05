# To measure efficiency of code machine-independently
# Emphasis is always placed on worst-case
# General Rules: (1) ignore constants
# (2) below terms dominate as follows
# O(1) < O(logn) < O(n) < O(nlogn)
# O(n^2) < O(2^n) < O(n!)

# efficiency = 3 * O(1) = O(1) - constant dropped
x = 5 + (15 * 20)  # O(1)
y = 15 - 2  # O(1)
print(x + y)  # O(1)


# efficiency = n * O(1) = O(n) - linear time
def loop_print_one(n):
    for z in range(0, n):
        print(z)  # O(1)


# efficiency = O(1) + O(n) = O(n) - latter dominates
def loop_print_two(n):
    j = 5 + (15 * 20)  # O(1)
    for i in range(j, n):  # O(n)
        print(i)


# efficiency = O(n) * O(n) = O(n^2) - quadratic time
def loop_print_three(n):
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            print(j)

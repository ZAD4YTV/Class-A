x = 5
y = 6

# Comparision Operators
if x == y:
    print("X is equals to Y")

if x != y:
    print("X is not equals to Y")

if x > y:
    print("X is greater than Y")

if x < y:
    print("X is less than Y")

if x >= y:
    print("X is greater or equals than Y")

if x <= y:
    print("X is less or equals than Y")


# Logical Operators

if x != y and x > y:
    print("X is not equals than Y, and X is greater than Y")


if x == y or y > x:
    print("X is equals than Y or Y is greater than X")

if not(x == 5):
    print("This block only run if X isn't equals to 5")

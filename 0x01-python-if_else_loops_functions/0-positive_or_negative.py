#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positiv7e")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")

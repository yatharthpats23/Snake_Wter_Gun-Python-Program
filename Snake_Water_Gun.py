#-1 for snake
#0 for water
#1 for gun

import random

computer = random.choice([-1, 0, 1])

Userstr = input("Enter your choice (s/w/g): ")

UserDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

User = UserDict[Userstr]

print(f"User chose {reverseDict[User]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == User:
    print("It is a Draw")

elif computer == -1 and User == 1:
    print("User Wins")

elif computer == -1 and User == 0:
    print("User Loses")

elif computer == 1 and User == -1:
    print("User Loses")

elif computer == 1 and User == 0:
    print("User Wins")

elif computer == 0 and User == 1:
    print("User Loses")

elif computer == 0 and User == -1:
    print("User Wins")

else:
    print("Something went wrong!")
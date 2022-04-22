import random

sachin_wins=0
Computer_wins=0

options=["rock","paper","scissors"]

while True:
    sachin_input=input("Type rock/paper/scissors or Q to quit: ").lower()
    if sachin_input=="q":
        break

    if sachin_input not in options:
        continue
    random_number=random.randint(0,2)
    # rock:0, paer:1, scissors:2

    computer_pick=options[random_number]
    print("Computer picked",computer_pick + " ,")

    if sachin_input=="rock" and computer_pick=="scissors":
        print("Sachin wins")
        sachin_wins +=1
        continue
    if sachin_input=="paper" and computer_pick=="rock":
        print("sachin wins")
        sachin_wins +=1
        continue
    if sachin_input=="scissors" and computer_pick=="paper":
        print("sachin wins")
        sachin_wins +=1
        continue
    else:
        print("Computer wins")
        Computer_wins +=1
        continue

print("You won ",sachin_wins,"times")
print("computer wins",Computer_wins,"times")
print("goodbye!")




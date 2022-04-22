name=input("Enter your name: ")
print("welcome to the adventure game Mr" )

answer=input("you are on road:would you like to go to right or left type(right/left)")

if answer=="right":
    answer=input("you reached mumbai Marve beach in Mumbai would you like to swim or take a boat(swim/boat)? ")
    if answer=="swim":
        print(name,"you got killed by shark")
        quit
    elif answer=="boat":
        print(name,"You reached Dubai HABIBI you got killed by MAFIA don PABLO EMILO ESCOBAR")
        quit
elif answer=="left":
    print(name,"you reached KarwAR ")

else:
    print("Not an valid option")

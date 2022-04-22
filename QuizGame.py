print("Welcome to the Quiz game")
playing=input("Do you want to play quiz? ")

if playing!="yes":
    quit()
    
print("Okay! Lets Play ")


score=0
Answer=input("What is IDLE in python ")
if Answer==("IDLE"):
    print("Correct!")
    score +=1
else:
    print("Incorrect")

Answer=input("What is  in python")
if Answer==("IDLE"):
    print("Correct!")
    score +=1
else:
    print("Incorrect")

Answer=input("What is IDLE in python")
if Answer==("Integrated Development learning Envirnoment"):
    print("Correct!")
    score +=1
else:
    print("Incorrect")

print("Your score "+str(score)+ " Question correct")

    


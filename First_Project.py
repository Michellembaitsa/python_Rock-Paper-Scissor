from random import randint #importing a module.

choice = ["Rock", "Paper", "Scissors"]

computer = choice[randint(0,2)] #The comp will select its random numbers

player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("It's a tie :0")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!, I covered you!")
        else:
            print("You win for now:(")
    elif player == "Paper":
        if computer == "Scissors":
            print("You have been cut,You lose!")
        else:
            print("You win! but not for long.")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose, you got smashed!")
        else:
            print("You win but only this once.")
    else:
        print("Try again.")
    player = False #If you do not set it to true, the loop will not continue.
    computer = choice[randint(0,2)]

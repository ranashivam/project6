import random

userWins = 0
computerWins = 0

options = ["stone", "paper", "scissors"]

while True:
    userInput = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if userInput == "q":
        break

    randomNumber = random.randint(0,2)
    # stone: 0, paper:1, scissors:2
    computerGuess = options[randomNumber]
    print("Computer Picked", computerGuess , ".")

    if userInput not in options:
        continue
    elif userInput == "stone" and computerGuess == "scissors":
        print("You Won!")
        userWins += 1
    elif userInput == "paper" and computerGuess == "stone":
        print("You Won!")
        userWins += 1
    elif userInput == "scissors" and computerGuess == "paper":
        print("You Won!")
        userWins += 1
    else:
        print("You Lost! Computer Wins!!!!")
        computerWins += 1

print("You Won", userWins, "times")
print("Computer Wins", computerWins, "times")
print("GoodBye!!")
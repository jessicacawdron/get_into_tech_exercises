from random import randint


def play():
    playing = input("Would you like to play rock paper, scissors? Y or N: ")
    decision = ["Y", "N"]
    while playing not in decision:
        print("Sorry that isn't a valid input.\n"
              "Type\n"
              "Y to play\n"
              "N to exit\n")
        playing = input("Would you like to play rock paper, scissors? Y or N: ")
    return playing


def welcome():
    print("Welcome to the game of Rock, Paper Scissors!")
    print("Do you think you can beat your opponent?")
    print("Each game consists of three rounds and the best of three wins.")
    print("To choose your go enter\n"
          "R for Rock\n"
          "P for Paper\n"
          "S for Scissors\n")


def computer_turn():
    choice = randint(0, 2)
    if choice == 0:
        print("Your opponent chose Rock")
        return choice
    elif choice == 1:
        print("Your opponent chose Paper")
        return choice
    elif choice == 2:
        print("Your opponent chose Scissors")
        return choice


def user_turn():
    user = input("Please enter your go: ")
    options = ["R", "P", "S"]
    while user not in options:
        print("Sorry that isn't a valid input.\n"
              "Enter\n"
              "R for Rock\n"
              "P for Paper\n"
              "S for Scissors\n")
        user = input("Please enter your go: ")
    if user == "R":
        print("You chose Rock")
        return 0
    elif user == "P":
        print("You Chose Paper")
        return 1
    elif user == "S":
        print("You Chose Scissors")
        return 2


def game(*, uservalue, computervalue, userscore, compscore):
    if uservalue == computervalue:
        print("DRAW")
        print("Your score is: ", userscore, "Your opponents score is: ", compscore)
        return userscore, compscore
    elif uservalue == 0 and computervalue == 2:
        print("Rock beats Scissors - YOU WIN")
        userscore += 1
        print("Your score is: ", userscore, "Your opponents score is: ", compscore)
        return userscore, compscore
    elif uservalue == 1 and computervalue == 0:
        print("Paper beats Rock - YOU WIN")
        userscore += 1
        print("Your score is: ", userscore, "Your opponents score is: ", compscore)
        return userscore, compscore
    elif uservalue == 2 and computervalue == 1:
        print("Scissors beats Paper - YOU WIN")
        userscore += 1
        print("Your score is: ", userscore, "Your opponents score is: ", compscore)
        return userscore, compscore
    else:
        compscore += 1
        if uservalue == 2 and computervalue == 0:
            print("Rock beats Scissors - YOU LOSE")
        elif uservalue == 1 and computervalue == 2:
            print("Scissors beats Paper - YOU LOSE")
        elif uservalue == 0 and computervalue == 1:
         print("Paper beats Rock - YOU LOSE")
    print("Your score is: ", userscore, "Your opponents score is: ", compscore)
    return userscore, compscore


def result(score1, score2):
    if score1 > score2:
        print("----------------------\n"
              "Congratulations\n"
              "You won the game!\n"
              "----------------------")
    elif score2 > score1:
        print("----------------------\n"
              "Oh no... you lost\n"
              "Better luck next time!\n"
              "----------------------")
    elif score1 == score2:
        print("----------------------\n"
              "It's a draw\n"
              "Go for the win next time!\n"
              "----------------------")
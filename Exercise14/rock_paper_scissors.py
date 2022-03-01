import random


def computer_turn():
    choice = random.randint(0, 2)
    return choice


def computer_choice():
    if compgo == 0:
        return "Rock"
    elif compgo == 1:
        return "Paper"
    elif compgo == 2:
        return "Scissors"


def user_turn(userinput):
    if userinput == "R":
        return 0
    elif userinput == "P":
        return 1
    elif userinput == "S":
        return 2
    else:
        return "Not a valid input."


def user_choice(userinput):
    if userinput == "R":
        return "Rock"
    elif userinput == "P":
        return "Paper"
    elif userinput == "S":
        return "Scissors"


def draw(uservalue, computervalue):
    if uservalue == computervalue:
        print("DRAW")


def win(*, uservalue, computervalue):
    if uservalue == 0 and computervalue == 2:
        print("Rock beats Scissors - YOU WIN")
        return 1
    elif uservalue == 1 and computervalue == 0:
        print("Paper beats Rock - YOU WIN")
        return 1
    elif uservalue == 2 and computervalue == 1:
        print("Scissors beats Paper - YOU WIN")
        return 1
    else:
        return 0


def lose(*, uservalue, computervalue):
    if uservalue == 2 and computervalue == 0:
        print("Rock beats Scissors - YOU LOSE")
        return 1
    elif uservalue == 1 and computervalue == 2:
        print("Scissors beats Paper - YOU LOSE")
        return 1
    elif uservalue == 0 and computervalue == 1:
        print("Paper beats Rock - YOU LOSE")
        return 1
    else:
        return 0


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


play = input("Would you like to play rock paper, scissors? Y or N: ")

while play != "N":
    print("Welcome to the game of Rock, Paper Scissors!")
    print("Do you think you can beat your opponent?")
    print("Each game consists of three rounds and the best of three wins.")
    print("To choose your go enter\n"
          "R for Rock\n"
          "P for Paper\n"
          "S for Scissors\n")
    n = 1
    user_points = 0
    comp_points = 0
    options = ["R", "P", "S"]

    while n <= 3:
        user = input("Please enter your go: ")
        while user not in options:
            print("Sorry that isn't a valid input.\n"
                  "Enter\n"
                  "R for Rock\n"
                  "P for Paper\n"
                  "S for Scissors\n")
            user = input("Please enter your go: ")

        usergo = user_turn(user)
        compgo = computer_turn()

        print("You chose", user_choice(user), "and your opponent chose", computer_choice())

        user_points = user_points + win(uservalue=usergo, computervalue=compgo)
        comp_points = comp_points + lose(uservalue=usergo, computervalue=compgo)
        draw(uservalue=usergo, computervalue=compgo)

        print("Your score is: ", user_points, "and your opponents score is: ", comp_points, "\n")

        n = n+1

    result(user_points, comp_points)
    play = input("Would you like to play again? Y or N :")

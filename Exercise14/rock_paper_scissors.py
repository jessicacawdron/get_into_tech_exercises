import rpsmodule

while rpsmodule.play() != "N":
    rpsmodule.welcome()
    n = 1
    user_points = 0
    comp_points = 0

    while n <= 3:
        user = rpsmodule.user_turn()
        comp = rpsmodule.computer_turn()
        x, y = rpsmodule.game(uservalue=user, computervalue=comp, userscore=user_points, compscore=comp_points)
        user_points = x
        comp_points = y

        n = n+1

    rpsmodule.result(user_points, comp_points)

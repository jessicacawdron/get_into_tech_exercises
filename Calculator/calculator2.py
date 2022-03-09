def multiply(list1):
    product = 1
    for i in list1:
        product *= i
    return product


def divide(list1):
    total = list1[0]
    for i in list1[1:]:
        total /= i
    return total


playername = input("Please enter your name: ")
filename = "%s.txt" % playername
userlog = open(filename, 'a+')

calc = input("Hello there! Would you like to use the calculator? Type Y to continue or N to exit. : ")
x = 1
while calc != "N":
    print("\n Calculator user log for", playername + ".", " Calculation", x, file=userlog)
    number_input = input("Please enter your numbers separated by a space: ")
    number_list = number_input.split()
    print(number_list)
    print("User entered the following list of numbers: ", number_list, file=userlog)

    for i in range(len(number_list)):
        try:
            number_list[i] = float(number_list[i])
        except ValueError:
            print("You can only use numbers!")
            number_input = input("Please enter your numbers separated by a space: ")
            number_list = number_input.split()
            for j in range(len(number_list)):
                number_list[j] = float(number_list[j])

    operation = input('''
    Please specify an operation to perform on the numbers provided from the option provided.
    Type + to add the numbers
    Type - to subtract the numbers
    Type * to multiply the numbers
    Type / to divide the numbers
    : ''')

    while operation != "+" and operation != "-" and operation != "*" and operation != "/":
        print("This is not a valid operation")
        operation = input("Please input one of the following +, -, * or / \n :")

    if operation == "+":
        print("The sum of the numbers is", sum(number_list))
        print("Calculation: ", number_input.replace(" ", " + "), " = ", sum(number_list))
        print("\nThe sum of the numbers is", sum(number_list), file=userlog)
        print("\nCalculation: ", number_input.replace(" ", " + "), " = ", sum(number_list), file=userlog)
    elif operation == "-":
        subtracting = number_list[0] - sum(number_list[1:])
        print("Subtracting the numbers gives: ", subtracting)
        print("Calculation: ", number_input.replace(" ", " - "), " = ", subtracting)
        print("\nSubtracting the numbers gives: ", subtracting, file=userlog)
        print("\nCalculation: ", number_input.replace(" ", " - "), " = ", subtracting, file=userlog)
    elif operation == "*":
        print("The product of the numbers is: ", multiply(number_list))
        print("Calculation: ", number_input.replace(" ", " * "), " = ", multiply(number_list))
        print("\nThe product of the numbers is: ", multiply(number_list), file=userlog)
        print("\nCalculation: ", number_input.replace(" ", " * "), " = ", multiply(number_list), file=userlog)
    else:
        while 0 in number_list[1:]:
            print("Error - cannot divide by zero.")
            number_input = input("Please enter your numbers separated by a space: ")
            number_list = number_input.split()
            for i in range(len(number_list)):
                number_list[i] = float(number_list[i])

        print("Diving the numbers gives:", divide(number_list))
        print("Calculation: ", number_input.replace(" ", " ÷ "), " = ", divide(number_list))
        print("\nDiving the numbers gives:", divide(number_list), file=userlog)
        print("\nCalculation: ", number_input.replace(" ", " ÷ "), " = ", divide(number_list), file=userlog)

    calc = str(input("Would you like to continue using the calculator? Type N to stop calculating. :"))
    x = 2


userlog.close()

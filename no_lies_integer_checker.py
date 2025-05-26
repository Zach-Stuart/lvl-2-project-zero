# functions
def int_check(question):
    """checks users enter an integer"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # return response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# main routine

# loop for testing
while True:
    print()

    # ask user for their name
    name = input("Name: ") # replace with call to 'not blank' function

    # ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # output error and success message
    if age < 12:
        print(f"{name} is too young.")
    elif age > 120:
        print(f"{name} is too old.")
    else:
        print(f"{name} has purchased a ticket!")
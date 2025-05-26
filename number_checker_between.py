# functions
def int_check(question, low, high):
    """checks users enter an integer between two values"""

    error = f"Oops - please enter an integer between {low} and {high}."

    while True:

        try:
            # change response to an integer and check it's more than 0
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine

# loop for testing

while True:
    print()

    # ask user for an integer
    my_num = int_check(question= "Choose a number: ", low= 1, high= 10)

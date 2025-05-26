# functions
def num_check(question, num_type, exitcode=None):
    """checks users enter an integer / float that is more than
    zero (or optional exit code)"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - please enter an integer more than zero."
        change_to = float

    while True:
        response = input(question).lower()

        # check for exit code
        if response == exitcode:
            return response

        try:
            # change response to an integer and check it's more than 0
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine

# loop for testing
while True:
    print()

    my_float = num_check(question="Please enter a number more than 0: ", num_type="float", exitcode="")
    print(f"You chose {my_float}")
    print()
    my_int = num_check(question="Please enter a number more than 0: ", num_type="integer", exitcode="")
    if my_int == "":
        print("You have chosen infinite mode.")
    else:
        print(f"You chose {my_int}")

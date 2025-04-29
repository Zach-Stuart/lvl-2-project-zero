# functions
def not_blank(question):
    """checks that user response isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again\n")


# main routine
who = not_blank("Please enter your name: ")
print(f"Hello, {who}")

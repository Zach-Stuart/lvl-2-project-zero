# functions
def make_statement(statement, decoration, lines=1):
    """emphasises headings (3 lines), subheadings (2 lines), and mini-headings (1 line). emojis are only used for
    single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# main routine
make_statement("This is a test", decoration="=", lines=3)
print()
make_statement("This is also a test", decoration="*", lines=2)
print()
make_statement("This is yet another test", decoration="👀")

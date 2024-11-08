# Generates headings (eg ----heading----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print("""
    Instructions go here.
    -Instruction 1 
    -Instruction 2
    -etc
    """)


# Ask user for a number between 1 and 200
def num_check(question):
    error = "Please enter an number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for or a number
            response = int(response)

            # check that number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):
    error = "please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print("please enter a number that is more than zero")

        except ValueError:
            print(error)


# Main routine goes here

statement_generator(statement="The Ultimate Factor Finder", decoration="-")


# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()


while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break

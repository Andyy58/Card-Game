# ======================================================================================================================
# UTILITIES.PY
# A library containing basic
# ======================================================================================================================
# ======================================================================================================================
# Obtains an integer from the user, if entered value is not an integer, asks the user again
def intput(prompt, errorMsgInt, min, max, minMaxErrorMsg):
    userInput = input(prompt)
    while True:
        if not userInput.isdigit():
            userInput = input(errorMsgInt + "Please try again: ")
        elif int(userInput) < min or int(userInput) > max:
            userInput = input(minMaxErrorMsg + " Please try again: ")
        else:
            return int(userInput)
            break


# ======================================================================================================================
# ======================================================================================================================
# Obtains a string from the user, if input is not a string, asks the user again
def stringput(prompt):
    userInput = input(prompt)
    while userInput.isalpha() == False:
        userInput = input(
            'That is an invalid input. Be sure to enter a string (No numerical values). Please try again\n>')


# Prints out the given text letter by letter simulating typing
def slow_type(word, speed):
    import sys, time
    for letter in word:
        print(letter, end="")
        sys.stdout.flush()
        time.sleep(speed)


# Clears the console by printing "\n" to return
def clear(amount=40):
    print("\n" * amount)

# "Press enter to continue"
def cont():
    input("Press enter to continue ")

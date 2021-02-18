"""
CS2450: Milestone 1
William Martell
Tanner Erekson
Derrek Buttars
Matthew Palmer
"""

memory = ["+0000"] * 100
accumulator = 0


def add(memory_location):
    """Adds a number from a specific location in memory to the number in the accumulator."""

    global accumulator

    memory_value = memory[memory_location]
    accumulator += memory_value
    return


def subtract(memory_location):
    """Subtracts a number from a specific location in memory from the number in the accumulator."""

    global accumulator

    memory_value = memory[memory_location]
    accumulator -= memory_value
    return


def multiply(memory_location):
    """Multiplies a number from a specific memory location to the number in the accumulator
    and returns the accumulator"""

    global accumulator

    memory_value = memory[memory_location]
    accumulator *= memory_value
    return


def divide(memory_location):
    """Divides the number in the accumulator by a number from a specific location in memory
    and returns the accumulator."""

    global accumulator

    memory_value = memory[memory_location]
    accumulator /= memory_value
    return


def read(memory_location):
    """Asks the user for an integer and puts it into a specific location in memory"""

    userInput = input("Enter an integer between -9999 and 9999: ")
    # if type(userInput) != int:
    #     print("must be an integer")
    try:
        userInput = int(userInput)
    except ValueError:
        print("Must be an int")
    except TypeError:
        print("Must be an int")
    else:
        if userInput > 9999 or userInput < -9999:
            print("must be an integer between -9999 and +9999")

        else:
            if userInput > 0:
                userInput = str(userInput)
                userInput = "+" + userInput.zfill(
                    4
                )  # Formats input to be the same as memory format
            memory[memory_location] = userInput
            return


def write(memory_location):
    """Prints the contents of the given memory location to the screen"""

    print(memory[memory_location])
    return


def load(memory_location):
    """ Will take a memory location and load what ever is there into the accumulator  """

    global accumulator

    accumulator = memory[memory_location]
    return


def store(memory_location):
    """ Will take whatever is in the accumulator and will store it in the given location """

    memory[memory_location] = accumulator
    return


def branch_neg():
    """Checks if the accumulator is < 0. returns True if yes, and False if no"""

    if accumulator < 0:
        return True
    else:
        return False


def branch_zero():
    """Checks if the accumulator = 0. returns True if yes, and False if no"""

    if accumulator == 0:
        return True
    else:
        return False


def clean_memory():
    """Checks memory for valid words and prompts a change if invalid instruction is found"""

    print("\n ---- Loading Memory... ----")

    index = 0
    while index < len(memory):
        number = memory[index]
        valid = False

        while not (valid):
            if (len(number) != 5) and (
                number != "-99999"
            ):  # Checks if length of instruction is correct
                print(f"{number} is not a valid instruction")
                number = str(input("Enter a valid instruction:"))

            elif (number[0] not in ("+", "-")) and (
                number != "-99999"
            ):  # Checks if instruction contain a + (Except if -99999)
                print(f"{number} is not a valid instruction")
                number = str(input("Enter a valid instruction:"))

            else:
                valid = True
                memory[index] = str(number)
        index += 1

    print("---- Memory Loaded ----\n")

    return


def run_instructions():
    """Runs the program written into the memory"""

    print("\n---- Running Program ----\n")

    for i in memory:
        if i == "-99999":
            break
        op = int(i[1:3])
        memory_location = int(i[3:5])

        if op == 10:
            read(memory_location)
        elif op == 11:
            write(memory_location)
        elif op == 20:
            load(memory_location)
        elif op == 21:
            store(memory_location)
        elif op == 30:
            add(memory_location)
        elif op == 31:
            subtract(memory_location)
        elif op == 32:
            divide(memory_location)
        elif op == 33:
            multiply(memory_location)
        elif op == 40:
            pass
        elif op == 41:
            pass
        elif op == 42:
            pass
        elif op == 43:  # Halt the program
            break


def main():
    entry_command = 1
    program_counter = 0

    print(
        "---- Instructions given in the UVsim must be in the format of +0000.  Ex. +1001 is a valid instruction ----"
    )

    while entry_command != "-99999":
        entry_command = input(str(program_counter).zfill(2) + " ? ")
        if entry_command != "-99999":
            memory[program_counter] = entry_command
            program_counter += 1

    clean_memory()
    run_instructions()

    print("REGISTERS:\n")
    print("Accumulator:    " + str(accumulator) + "\n")
    print("Instruction Counter:    ")
    print("InstructionRegister:    ")
    print("Operation Code:         ")
    print("Operand:                ")

    for i in memory:
        print(i)


if __name__ == "__main__":
    main()

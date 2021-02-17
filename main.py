"""
CS2450: Milestone 1
William Martell
Tanner Erekson
Derrek Buttars
Matthew Palmer
"""
memory = ["+0000"]*100


def add(memory_location, accumulator):
    """Adds a number from a specific locaiton in memory to the number in the accumulator."""

    memory_value = memory[memory_location]
    accumulator += memory_value
    return accumulator


def subtract(memory_location, accumulator):
    """Subtracts a number from a specific location in memory from the number in the accumulator."""

    memory_value = memory[memory_location]
    accumulator -= memory_value
    return accumulator


def multiply(memory_location, accumulator):
    """Multiplies a number from a specific memory location to the number in the accumulator
    and returns the accumulator"""

    memory_value = memory[memory_location]
    accumulator *= memory_value
    return accumulator


def divide(memory_location, accumulator):
    """Divides the number in the accumulator by a number from a specific location in memory
    and returns the accumulator."""

    memory_value = memory[memory_location]
    accumulator /= memory_value
    return accumulator


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
            memory[memory_location] = userInput
            return


def write(memory_location):
    """Prints the contents of the given memory location to the screen"""

    print(memory[memory_location])
    return


def load(memory_location, accumulator):
    """ Will take a memory location and load what ever is there into the accumulator  """
    accumulator = memory[memory_location]
    return accumulator


def store(memory_location, accumulator):
    """ Will take whatever is in the accumulator and will store it in the given location """
    memory[memory_location] = accumulator
    return

def clean_memory(lyst):
    for i in lyst:
        i = str(i)
        if len(i) != 5:  # Checks if length of instruction is correct
            if i != "-99999":
                print(f"{i} is not a valid instruction")

        elif i[0] != "+":  # Checks if instruction contain a + (Except if -99999)
            if i != "-99999":
                print(f"{i} is not a valid instruction")
    return lyst


def main():
    entry_command = 1
    program_counter = 0
    accumulator = 0
    print(
        "~~ Instructions given in the UVsim must be in the format of +0000.  Ex. +1001 is a valid instruction ~~"
    )

    while entry_command != "-99999":
        entry_command = input(str(program_counter).zfill(2) + " ? ")
        memory.append(entry_command)
        program_counter += 1

    cleaned_memory = clean_memory(memory)
    

    #Where Matthew is going to take this information and make the run_program function with the cleaned_memory as a parameter.
    for i in memory:
        op = int(i[1:3])
        memory_location = int(i[3:5])

        if op == 10:
            read(memory_location)
        if op == 11:
            write(memory_location)
        if op == 20:
            load(memory_location, accumulator)
        if op == 21:
            store(memory_location, accumulator)
        if op == 30:
            add(memory_location, accumulator)
        if op == 31:
            subtract(memory_location, accumulator)
        if op == 32:
            divide(memory_location, accumulator)
        if op == 33:
            multiply(memory_location, accumulator)


if __name__ == "__main__":
    main()

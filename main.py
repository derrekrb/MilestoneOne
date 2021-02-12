def add(number, accumulator):
    return accumulator


def subtract():
    return 5


def multiply():
    return


def divide():
    return


def read(memoryDestination):
    """Asks the user for an integer and puts it into a specific location in memory"""

    userInput = input("Enter an integer: ")
    memory[memoryDestination] = userInput
    return


def write(memoryLocation):
    '''Prints the contents of the given memory location to the screen'''
    
    print(memory[memoryLocation])
    return


def load():
    return


def store():
    return


def main():
    program_counter = 0
    memory = []
    entry_command = 1
    accumulator = 0

    while entry_command != -99999:
        entry_command = int((input(str(program_counter).zfill(2) + " ? ")))
        memory.append(entry_command)
        program_counter += 1

    # for i in memory:
    # print(i)


if __name__ == "__main__":
    main()

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


def load(location):
    """ Will take a memory location and load what ever is there into the accumulator  """
    accumulator = memory[location]
    return accumulator

def store(location):
    """ Will take whatever is in the accumulator and will store it in the given location """
    memory[location]= accumulator




def main():
    program_counter = 0
    memory = []
    entry_command = 1
    accumulator = 0

    while entry_command != -99999:
        entry_command = int((input(str(program_counter).zfill(2) + " ? ")))
        memory.append(entry_command)
        program_counter += 1


    for i in memory:
        i = str(i)
        op = int(i[0:2])
        num = int(i[2:4])
        
        if op == 10:
            read()
        if op == 11:
            write()
        if op == 20:
            load(num)
        if op == 21:
            store(num)
        if op == 30:
            add()
        if op == 31:
            subtract()
        if op == 32:
            divide()
        if op == 33:
            multiply()
        
    

    # for i in memory:
    # print(i)



if __name__ == "__main__":
    main()

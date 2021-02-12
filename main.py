"""
CS2450: Milestone 1
William Martell
Tanner Erekson
Derrek Buttars
Matthew Palmer
"""
memory = []


def add(memory_location, accumulator):
    '''Adds a number from a specific locaiton in memory to the number in the accumulator.'''
    
    memory_value = memory[memory_location]
    accumulator += memory_value
    return accumulator


def subtract(memory_location, accumulator):
    '''Subtracts a number from a specific location in memory from the number in the accumulator.'''
    
    memory_value = memory[memory_location]
    accumulator -= memory_value
    return accumulator


def multiply(memory_location, accumulator):
    '''Multiplies a number from a specific memory location to the number in the accumulator
    and returns the accumulator'''
    
    memory_value = memory[memory_location]
    accumulator *= memory_value
    return accumulator


def divide(memory_location, accumulator):
    '''Divides the number in the accumulator by a number from a specific location in memory
    and returns the accumulator.'''
    
    memory_value = memory[memory_location]
    accumulator /= memory_value
    return accumulator


def read(memory_location):
    """Asks the user for an integer and puts it into a specific location in memory"""

    userInput = input("Enter an integer: ")
    memory[memory_location] = userInput
    return


def write(memory_location):
    '''Prints the contents of the given memory location to the screen'''
    
    print(memory[memory_location])
    return


def load(memory_location, accumulator):
    """ Will take a memory location and load what ever is there into the accumulator  """
    accumulator = memory[memory_location]
    return accumulator

def store(memory_location, accumulator):
    """ Will take whatever is in the accumulator and will store it in the given location """
    memory[memory_location]= accumulator
    return



def main():
    entry_command = 1
    program_counter = 0
    accumulator = 0
    
    while entry_command != -99999:
        entry_command = int((input(str(program_counter).zfill(2) + " ? ")))
        memory.append(entry_command)
        program_counter += 1


    for i in memory:
        i = str(i)
        op = int(i[0:2])
        memory_location = int(i[2:4])
        
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
        
    

    # for i in memory:
    # print(i)



if __name__ == "__main__":
    main()

def add(number, accumulator):
    return accumulator


def subtract():
    return

def multiply():
    return

def divide():
    return

def read():
    return

def write():
    return

def load(location, accumulator):
    accumulator = memory[location]
    return accumulator

def store(location, accumulator):
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
        
        if op == 10:
            print("read")
        if op == 11:
            print("write")
        if op == 20:
            print("load")
        if op == 21:
            print("store")
        if op == 30:
            print("add")
        if op == 31:
            print("subtract")
        if op == 32:
            print("divide")
        if op == 33:
            print("multiply")
        
    


if __name__ == "__main__":
    main()

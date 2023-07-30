if __name__ == "__main__":
    
    numberOfElements = int(input())
    elements = set(map(int,input().split()))
    numberOfCommands = int(input())
    
    for i in range(numberOfCommands):
        command = input().split()
        if command[0] == "pop":
            elements.pop()
            # print(command)
            # print(myset)
        elif command[0] == "discard":
            elements.discard(int(command[1]))
            # print(myset)
        else:
            if command[1] not in elements:
                continue
            elements.remove(int(command[1]))
            # print(myset)
    print(sum(list(elements)))
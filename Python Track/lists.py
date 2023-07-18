if __name__ == '__main__':
    N = int(input())
    operations = ["insert", "print", "remove", "append", "sort", "pop", "reverse"]
    for i in range (N):
        choice = input().split()
        if choice[0] not in operations:
            print("No such operations. Choose among", end = " ")
            print(operations)
        else:
            print("Successfully received!")
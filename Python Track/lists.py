if __name__ == '__main__':
    N = int(input())
    operations = ["insert", "print", "remove", "append", "sort", "pop", "reverse"]
    numbers = []
    for i in range (N):
        choice = input().split()
        if choice[0] not in operations:
            print("No such operations. Choose among", end = " ")
            print(operations)
        elif choice[0] == "insert":
            # print(choice[1], end = " ")
            # print( choice[2])
            position = int(choice[1])
            element = int(choice[2])
            numbers.insert(position, element)
            # print(numbers)
        elif choice[0] == "print":
            print(numbers)
        elif choice[0] == "remove":
            numbers.remove(int(choice[1]))
            # print(numbers)
        elif choice[0] == "append":
            numbers.append(int(choice[1]))
            # print(numbers)
        elif choice[0] == "sort":
            numbers.sort()
            # print(numbers)
        elif choice[0] == "pop":
            numbers.pop(-1)
            # print(numbers)
        else:
            numbers.reverse()
            # print(numbers)
# print(numbers)
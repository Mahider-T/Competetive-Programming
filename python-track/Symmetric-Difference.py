# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = int(input())
    first_list = input().split()
    b = int(input())
    second_list = input().split()   
    final = []
    for i in range(a):
        if first_list[i] not in second_list and first_list[i] not in final:
            final.append(first_list[i])
    
    for i in range(b):
        if second_list[i] not in first_list and second_list[i] not in final:
            final.append(second_list[i])   
    
    final = list(map(int, final))
    final.sort()
    for i in final:
        print(i)
    # print(final)

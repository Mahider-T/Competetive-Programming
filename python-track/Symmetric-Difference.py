# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    # 4
    # 2 4 5 9
    # 4
    # 2 4 11 12
    
    one = input()
    two = set(input().split())
    three = input()
    four = set(input().split())
    
    symmetricDifference = list(two.difference(four).union(four.difference(two)))
    sortedFinal = list(map(int, symmetricDifference))
    sortedFinal.sort()
    # print(type(sortedFinal))  
    
    for item in sortedFinal:
        print(item)
    
    # print(f"{aMinusB} and {bMinusA}") 
    # print(aMinusB)
    
    
    
    # print(one)
    # print(two)
    # print(three)
    # print(four)
    # myset = set()
    # print(final)

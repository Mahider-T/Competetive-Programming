# Enter your code here. Read input from STDIN. Print output to STDOUT
numbers = list(map(int, input().split()))
array = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

n = numbers[0]
m = numbers[1]

happiness = 0
for item in array:
    if item in setA or item in setB:
        if item in setA:
            happiness += 1
        elif item in setB:
            happiness -= 1
        else:
            continue

print(happiness)
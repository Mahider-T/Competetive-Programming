# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input()) #number of shoes in the shop
shoeSizes = list(map(int, input().split())) # all available sizes
shoeSizes = Counter(shoeSizes)
N = int(input()) # number of customers

total = 0

for i in range(N):
    purchase = list(map(int, input().split()))
    if shoeSizes[purchase[0]] > 0:
        shoeSizes[purchase[0]] -= 1
        total += purchase[1]
    #     print(shoeSizes[purchase[0]])
    # else:
    #     print("Depleted")
        

print(total)

# print(shoeSizes)
# print(purchases)
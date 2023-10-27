# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N = int(input())
letters = input().split()
K = int(input())

arr = []
indices = []
count = 0
for i in range(1,N+1):
    arr.append(i)
comb = list(combinations(arr, K))

for i in range(len(letters)):
    if letters[i] == 'a':
        indices.append(i+1)
        

for pair in comb:
    for index in indices:
        if index in pair:
            count += 1
            break

print(count/len(comb))
# print(count)
# print(len(comb))
# print(comb)
# print(index)
# print(indices)
# print(arr)
# print(list(combinations(arr, K)))
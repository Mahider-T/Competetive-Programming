# Enter your code here. Read input from STDIN. Print output to STDOUTfrom itertools import permutations
from itertools import combinations
s = list(input().split())
term = s[0]
number = int(s[1])

# print(f"{term} {number}")
term = list(term)
term.sort()

for i in range(1, number+1):
    ls = list(combinations(term, i))
    ls.sort()
    for tuples in ls:
        for i in range(len(tuples)):
            if (len(tuples) - i) > 1:
                print(tuples[i], end = "")
            else:
                print(tuples[i])
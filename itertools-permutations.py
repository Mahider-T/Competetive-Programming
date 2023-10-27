# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s = list(input().split())
term = s[0]
number = int(s[1])


ls = list(permutations(term, number))
ls.sort()
# print(ls)
for tuples in ls:
    for i in range(len(tuples)):
        if (len(tuples) - i) > 1:
            print(tuples[i], end = "")
        else:
            print(tuples[i])
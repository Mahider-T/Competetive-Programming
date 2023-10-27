from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = list(product(A, B)) 
for each in answer:
    print(each, end = " ")
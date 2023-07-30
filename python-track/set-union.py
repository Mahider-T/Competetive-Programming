# Enter your code here. Read input from STDIN. Print output to STDOUT
englishSub = int(input())
englishStudents = set(map(int, input().split()))
frenchSub = int(input())
frenchStudents = set(map(int, input().split()))

answer = len(list(englishStudents.union(frenchStudents)))
print(answer)
# print( f"{englishStudents} + {frenchStudents}")

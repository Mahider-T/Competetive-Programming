if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    count = 0
    results = student_marks[query_name]
    arrayLength = len(results)
    for i in range(arrayLength):
        sum += results[i]
    average = sum/arrayLength
    print("{0:.2f}".format(average))
    
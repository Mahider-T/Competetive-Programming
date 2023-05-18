if __name__ == '__main__':
    biggerList = []
    scoreList = []
    finalListOfStudents = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if (score not in scoreList):
            scoreList.append(score)
        student = [name, score]
        biggerList.append(student)
    scoreList.sort()
    targetScore = scoreList[1]
    for i in range(len(biggerList)):
        if(biggerList[i][1] == targetScore):
            finalListOfStudents.append(biggerList[i][0])
    
finalListOfStudents.sort()
for i in finalListOfStudents:
    print(i)
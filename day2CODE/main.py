file = open("input.txt","r")

myChoice = 0
cpChoice = 0
totalScore = 0
# 1 rock    A X
# 2 paper   B Y
# 3 scisors C Z

# X lose
# Y draw
# Z win

while True:
    Line = file.readline()
    if not Line:
        break;

    if 'A' in Line:
        cpChoice = 1    #Rock
    elif 'B' in Line:
        cpChoice = 2    #Paper
    elif 'C' in Line:
        cpChoice = 3    #Scissors

    if 'X' in Line:
        if cpChoice == 1:
            myChoice = 3
        elif cpChoice == 2:
            myChoice = 1
        else:
            myChoice = 2

    elif 'Y' in Line:
        myChoice = cpChoice
    elif 'Z' in Line:
        if cpChoice == 1:
            myChoice = 2
        elif cpChoice == 2:
            myChoice = 3
        else:
            myChoice = 1


    # tie
    totalScore += myChoice
    if myChoice == cpChoice:
        totalScore += 3

    #i chose rock
    elif myChoice == 1:
        if cpChoice == 3:
            totalScore += 6
    #i chose paper
    elif myChoice == 2:
        if cpChoice == 1:
            totalScore += 6

    #i chose scisors
    elif myChoice == 3:
        if cpChoice == 2:
            totalScore +=6


print ("total score is ", totalScore)

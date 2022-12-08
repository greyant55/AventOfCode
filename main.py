
maxCal = 0
maxCal2 = 1
maxCal3 = 2

maxIndex = 0
maxIndex2 = 0
maxIndex3 = 0

currentCal = 0
currentIndex = 1

file = open("input.txt","r")

while True:
    Line = file.readline()
    if not Line:
        break;

    if Line.strip('\n') == "":
        print()
        if currentCal > maxCal and currentCal < maxCal2:
            maxCal = currentCal
            maxIndex = currentIndex
        elif currentCal > maxCal2 and currentCal < maxCal3:
            maxCal = maxCal2
            maxCal2 = currentCal
            maxIndex = maxIndex2
            maxIndex2 = currentIndex
        elif currentCal > maxCal3:
            maxCal = maxCal2
            maxCal2 = maxCal3
            maxCal3 = currentCal
            maxIndex = maxIndex2
            maxIndex2 = maxIndex3
            maxIndex3 = currentIndex


        currentIndex += 1
        currentCal = 0
    else:
        print(int(Line.strip('\n')))
        currentCal += int(Line.strip('\n'))
        #print ("Current calories in this elf", currentCal)


print ("The Elf with the most cals is elf #", maxIndex3)
print ("he has this many calories: ", maxCal3)
print ("The Elf with the 2nd most cals is elf #", maxIndex2)
print ("he has this many calories: ", maxCal2)
print ("The Elf with the 3rd most cals is elf #", maxIndex)
print ("he has this many calories: ", maxCal)

totalCal = maxCal + maxCal2 + maxCal3
print ("The total calories is ", totalCal)




#print (ord('a')-96)
#print (ord('z')-96)
#print (ord('A')-38)
#print (ord('Z')-38)

score = 0
file = open("input.txt","r")
while True:
    Line = file.readline()
    Line = Line.replace('\n','')
    Line2 = file.readline()
    Line2 = Line2.replace('\n', '')
    Line3 = file.readline()
    Line3 = Line3.replace('\n', '')
    if not Line:
       break;

    #print(int(len(Line)/2))
    for x in range (len(Line)):
        for y in range (len(Line2)):
            for z in range (len(Line3)):
                if Line[x] == Line2 [y] and Line2[y] == Line3[z]:
                    same = Line[x]
                    #print ("the same letter is", same)
#    for x in range(int(len(Line)/2)):
#        #first half
#        #print (x)
#        for y in range(int(len(Line)/2), len(Line)):
            #second half
            #print(y)
#            if Line[x] == Line[y]:
#                same = Line[x]
 #               print ("the same letter is ",Line[x])
    #print ("the same letter is", same)
    if same.isupper():
        score += (ord(same) - 38)
    else:
        score += (ord(same) - 96)

print ("the final score is ", score)
f = open("dati3.txt", "r")
lines = f.readlines()
linesF = []

for l in lines:
    linesF.append(l.rstrip())

def calc(x, R):

    treeCount = 0
    currentPosX = 0
    simbol = "."
    blockLenght = len(linesF[0])
    l = 0

    while l < len(linesF)-R:
        currentPosX += x
        currentPosX = currentPosX % blockLenght
        #print(currentPosX, l+R)
        simbol = lines[l+R][currentPosX]
        #print(simbol)
        if simbol == "#":
            treeCount += 1
        l += R
    print(treeCount)
    return(treeCount)



t1 = calc(1,1)
t2 = calc(3,1)
t3 = calc(5,1)
t4 = calc(7,1)
t5 = calc(1,2)

treeMult = t1*t2*t3*t4*t5


print(treeMult)
#print(linesF)
#print(len(linesF))
#print(blockLenght)
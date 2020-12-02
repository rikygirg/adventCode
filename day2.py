d = open("dati2.txt", "r")
d = d.read()
dati = d.split(", ")
index = []
passw = []
right1 = []
right2 = []
x = 0
lenght = len(dati)
while x < lenght:
    #print(dati[x])
    dato = dati[x].split(": ")
    index.append(dato[0])
    passw.append(dato[1])
    x += 1

x = 0
while x < lenght:
    letter = index[x][-1]
    num = index[x].split(" ")
    nums = num[0].split("-")
    num1 = int(nums[0])
    num2 = int(nums[1])
    #print(num1,num2,letter)
    letTimes = passw[x].count(letter)
    letterPos1 = passw[x][num1-1]
    letterPos2 = passw[x][num2-1]
    #print(dati[x],letter, letTimes)
    if num1 <= letTimes <= num2:
        right1.append(dati[x])
    if (letterPos1 == letter) ^ (letterPos2 == letter):
        right2.append(dati[x])
    x += 1





print("Correct passwords Prob1:",len(right1))
print("Correct passwords Prob2:",len(right2))
#print(right2)
#print(dati[3])
#print(letter)
#print(index[3])
#print(passw[3])
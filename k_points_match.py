def cmpare(num2,prev):
    county = 0
    for i in range(len(prev)):
        if num2[i]==prev[i]:
            county+=1
    if county == len(num2):
        return True
    else:
        return False

#Fe
with open("spindownFe.txt","r") as f1, open("spinupdown_parsed.txt","w") as f2:
    for line in f1:
        numbers = line.split()
        if len(numbers) == 4:
            f2.write(line)

#Nb
with open("datasample2.txt","r") as f1, open("datasample2_parsed.txt","w") as f2:
    for line in f1:
        numbers = line.split()
        if len(numbers) == 4:
            f2.write(line)

num1_set = []
num2_set = []

with open("spinupdown_parsed.txt","r") as f1:
    for line1 in f1:
        num1 = line1.split()
        num1 = map(float,num1)
        num1_set.append(num1)

num1_no_repeats = [ele for ind, ele in enumerate(num1_set) if ele not in num1_set[:ind]]

with open("datasample2_parsed.txt","r") as f2:
    for line2 in f2:
        num2 = line2.split()
        num2 = map(float,num2)
        num2_set.append(num2)

num2_no_repeats = [ele for ind, ele in enumerate(num2_set) if ele not in num2_set[:ind]]
with open("spindown_result.txt","w") as f3:
    for i in num1_no_repeats:
        for j in num2_no_repeats:
            if (abs(i[0]-j[0]) <= 0.0) and (abs(i[1]-j[1]) <=0.0):
                f3.write("("+str(i[0])+", "+str(i[1])+", "+str(i[2])+")\t("+str(j[0])+", "+str(j[1])+", "+str(j[2])+")\n")
    '''
    if cmpare(num2,prev)==False:
        #print "num2: ",num2
        if (abs(num1[1]-num2[1]) <= 0.0) and (abs(num1[2]-num2[2]) <= 0.0):
            f3.write("("+str(num1[0])+", "+str(num1[1])+", "+str(num1[2])+")"+'\t'+"("+str(num1[0])+", "+str(num1[1])+", "+str(num1[2])+")"+'\n')
            prev = num2
    '''

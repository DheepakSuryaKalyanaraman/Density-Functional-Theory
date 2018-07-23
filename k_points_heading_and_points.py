num1_set = []
hm_set1 = {}
num2_set = []
hm_set2 = {}

with open("datasample.txt","r") as f1:
    key = ""
    value = []
    for line1 in f1:
        num1 = line1.split()
        if len(num1)==4:
            if len(value)>0:
                hm_set1[key]=value
                value = []
            num1 = map(float,num1)
            key = tuple(num1)
            num1_set.append(num1)
        else:
            value.append(line1)
    if  len(value)>0:
        hm_set1[key]=value

num1_no_repeats = [ele for ind, ele in enumerate(num1_set) if ele not in num1_set[:ind]]

with open("datasample2.txt","r") as f2:
    key = set()
    value = []
    for line1 in f2:
        num1 = line1.split()
        if len(num1)==4:
            if len(value)>0:
                hm_set2[key]=value
                value = []
            num1 = map(float,num1)
            key = tuple(num1)
            num2_set.append(num1)
        else:
            value.append(line1)
    if  len(value)>0:
        hm_set2[key]=value

num2_no_repeats = [ele for ind, ele in enumerate(num2_set) if ele not in num2_set[:ind]]

with open("final_result_with_points_and_heading.txt","w") as f3:
    for i in num1_no_repeats:
        for j in num2_no_repeats:
            if (abs(i[0]-j[0]) <= 0.0) and (abs(i[1]-j[1]) <=0.0):
                f3.write("\n("+str(i[0])+", "+str(i[1])+", "+str(i[2])+")\t("+str(j[0])+", "+str(j[1])+", "+str(j[2])+")")
                listy = hm_set1[tuple(i)]
                #print listy

                f3.write("\nFe: ")
                for l in listy:
                    l=l.replace("\t"," ")
                    l = l.replace("\n","")
                    f3.write("("+l+") ")
                #f3.write(listy)
                listy = hm_set2[tuple(j)]
                #print listy
                f3.write("\nNb: ")
                for l in listy:
                    l=l.replace("\t"," ")
                    l=l.replace("\n","")
                    f3.write("("+l+") ")
                #f3.write(listy)
                #f3.write(str(hm_set1[tuple(i)]).replace("\t"," ")+"\t"+str(hm_set2[tuple(j)]).replace("\t"," ")+"\n")

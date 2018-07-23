def generate_combo(num_set):
    result = set()
    permute(num_set,0,len(num_set)-1,result)
    #print result
    return result

def permute(a, l, r, result):
    if l==r:
        result.add(str(a))
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, result)
            a[l], a[i] = a[i], a[l] # backtrack

with open("Nb_heading.txt","r") as fp1, open("24_48_combo.txt","w") as fp2:
    for line in fp1:
        words = line.split()
        fp2.write("\n"+line)
        list_num = set()
        if(abs(float(words[3])-0.0000568) <= 0.0000001):
            num_set = []
            x_pos = round(float(words[0]),7)
            if x_pos != 0.0:
                x_neg = -x_pos
            else:
                x_neg = x_pos
            y_pos = round(float(words[1]),7)
            if y_pos != 0.0:
                y_neg = -y_pos
            else:
                y_neg = y_pos
            z_pos = round(float(words[2]),7)
            if z_pos != 0.0:
                z_neg = -z_pos
            else:
                z_neg = z_pos
            num_set.append(x_pos)
            num_set.append(y_pos)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_pos)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_neg)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_pos)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_neg)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_pos)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_neg)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_neg)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
        elif(abs(float(words[3])-0.000114) <= 0.0000003):
            num_set = []
            x_pos = round(float(words[0]),7)
            x_neg = -x_pos
            y_pos = round(float(words[1]),7)
            y_neg = -y_pos
            z_pos = round(float(words[2]),7)
            z_neg = -z_pos
            num_set.append(x_pos)
            num_set.append(y_pos)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_pos)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_neg)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_pos)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_neg)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_pos)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_neg)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_neg)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
        elif(abs(float(words[3])-0.0000284) <= 0.0000001):
            num_set = []
            x_pos = round(float(words[0]),7)
            if x_pos != 0.0:
                x_neg = -x_pos
            else:
                x_neg = x_pos
            y_pos = round(float(words[1]),7)
            if y_pos != 0.0:
                y_neg = -y_pos
            else:
                y_neg = y_pos
            z_pos = round(float(words[2]),7)
            if z_pos != 0.0:
                z_neg = -z_pos
            else:
                z_neg = z_pos
            num_set.append(x_pos)
            num_set.append(y_pos)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_pos)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_neg)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_pos)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_neg)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_pos)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_neg)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_neg)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
        elif(abs(float(words[3])-0.0000142) <= 0.0000001):
            num_set = []
            x_pos = round(float(words[0]),7)
            if x_pos != 0.0:
                x_neg = -x_pos
            else:
                x_neg = x_pos
            y_pos = round(float(words[1]),7)
            if y_pos != 0.0:
                y_neg = -y_pos
            else:
                y_neg = y_pos
            z_pos = round(float(words[2]),7)
            if z_pos != 0.0:
                z_neg = -z_pos
            else:
                z_neg = z_pos
            num_set.append(x_pos)
            num_set.append(y_pos)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_pos)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_neg)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_pos)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_neg)
            num_set.append(z_pos)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_pos)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_pos)
            num_set.append(y_neg)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
            num_set = []
            num_set.append(x_neg)
            num_set.append(y_neg)
            num_set.append(z_neg)
            list_num.add(str(num_set))
            list_num |= generate_combo(num_set)
        list_temp = list(list_num)
        count = 1
        for i in list_temp:
            if count%4!=0:
                fp2.write(str(i).replace("set","")+"\t")
            else:
                fp2.write(str(i).replace("set","")+"\n")
            count+=1

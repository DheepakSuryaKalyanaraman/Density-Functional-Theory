with open("final_result.txt","r") as f1, open("x_diff_op.txt","w") as f2:
    for line in f1:
        points = line.split()
        num1 = (points[0].replace("(","")).replace(",","")
        num2 = (points[3].replace("(","")).replace(",","")
        diff = str(abs(float(num1)-float(num2)))
        line = line.rstrip("\n\r")
        f2.write(line+"\t"+diff+"\n")

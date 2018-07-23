with open("datasample.txt","r") as f1, open("result_diff.txt","w") as f2:
    for line in f1:
        numbers = line.split()
        if len(numbers)>4:
            diff = abs(float(numbers[1])-float(numbers[2]))
            f2.write(numbers[1]+" "+numbers[2]+" "+str(diff)+"\n")

i=0
header = ""
#4.8412
with open("../../Nbmesh/EIGENVAL") as fp, open("datasample2.txt","w") as f:
    for line in fp:
        i=i+1
        if i>7:
            numbers = line.split()
            if len(numbers) == 4:
                header = line
            elif len(numbers) == 5:
                #data
                num1 = float(numbers[1])
                num2 = float(numbers[2])
                if num1 >= 4.8312 and num1 <= 4.8512:
                    if header != "":
                        f.write(header)
                        header = ""
                    f.write(line)
                elif num2 >= 4.8312 and num2 <= 4.8512:
                    if header != "":
                        f.write(header)
                        header = ""
                    f.write(line)

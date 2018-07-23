i=0
header = ""
with open("../../Femesh/EIGENVAL") as fp, open("spindownFe.txt","w") as f:
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
                if num2 >= 5.6211 and num2 <= 5.6411:
                    if header != "":
                        f.write(header)
                        header = ""
                    f.write(line)

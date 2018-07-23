with open("/home/dkalyan1/python_programs/python_scripts/datasample2.txt","r") as fp1, open("Nb_heading.txt","w") as fp2:
    count = 0
    for line in fp1:
        count+=1
        if count>=1:
            words = line.split()
            if len(words)==4:
                fp2.write(line)

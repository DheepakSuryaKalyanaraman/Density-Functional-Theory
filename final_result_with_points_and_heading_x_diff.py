with open("final_result_with_points_and_heading.txt","r") as f1, open("fr_x_diff_op.txt","w") as f2:
    for line in f1:
        words = line.split()
        if len(words) > 0:
            if words[0] == "Fe:":
                diff = abs(float(words[3])-float(words[4]))
                line = line.replace("\n","")
                f2.write(line+"  diff: "+str(diff)+"\n")
            else:
                f2.write(line)

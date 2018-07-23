########## heading velocity #################
#hv = (1/hbar)*De/Dk
#hbar = 6.582 * 10 ^ (-16)
#De_spinup = abs(Fe_1st_point - Nb_1st_point)
#De_spindown = abs(Fe_2nd_point - Nb_2nd_point)
#Dk = Fe_x - Nb_x
# let k = x_value of Nb(heading)
#v2 = hv / (hbar * k)

hbar = 6.582 * pow(10.0,(-16))
Dk = 0
k = 0
Fe = []
Nb = []
Fepoint = []
Nbpoint = []
heading = ""
with open("final_result_with_points_and_heading.txt","r") as f1, open("heading_velocity.txt","w") as f2:
    for line in f1:
        numbers = line.split()
        if len(numbers) > 1:
            if numbers[0] != "Fe:" and numbers[0] != "Nb:":
                #heading
                Dk = abs(float((numbers[0].replace("(","")).replace(",",""))-float((numbers[3].replace("(","")).replace(",","")))
                k = abs(float((numbers[3].replace("(","")).replace(",","")))
                if Dk == 0:
                    continue
                heading = line
            else:
                if Dk == 0:
                    continue
                import re
                listy = re.findall("\((.*?)\)",line)
                foundNb = False
                for i in listy:
                    point = (i.replace("(","")).replace(")","")
                    plist = point.split()
                    plist = plist[1:]
                    #assuming the above line works
                    if numbers[0] == "Fe:":
                        Fepoint.append(i)
                        Fe.append(float(plist[0]))
                    elif numbers[0] == "Nb:":
                        foundNb = True
                        Nbpoint.append(i)
                        Nb.append(float(plist[0]))
                        Nb.append(float(plist[1]))
                if foundNb == True:
                    for i in range(0, len(Fe)-1, 2):
                        for j in range(0, len(Nb)-1, 2):
                            De_spinup = abs(Fe[i]-Nb[j])
                            De_spindown = abs(Fe[i+1]-Nb[j+1])
                            hv_spinup = (1.0/hbar)*(De_spinup/Dk)
                            hv_spindown = (1.0/hbar)*(De_spindown/Dk)
                            hv2_spinup = 1.0 / (hv_spinup / (hbar * k))
                            hv2_spindown = 1.0 / (hv_spindown / (hbar * k))
                            f2.write(heading)
                            f2.write(Fepoint[i/2]+"\n")
                            f2.write(Nbpoint[j/2]+"\n")
                            f2.write("hv_spinup: "+str(hv_spinup)+"\n")
                            f2.write("hv_spindown: "+str(hv_spindown)+"\n")
                            f2.write("hv2_spinup: "+str(hv2_spinup)+"\n")
                            f2.write("hv2_spindown: "+str(hv2_spindown)+"\n")
                    foundNb = False
                    Fe = []
                    Nb = []
                    Dk = 0
                    k = 0
                    Fepoint = []
                    Nbpoint = []
                    heading = ""
                #reset_every_variable

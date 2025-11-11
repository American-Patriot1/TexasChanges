#---------------------------------------------------I would recomend putting this file in your map folder---------------------------------------------------------

#list order
#province ids int;red int;blue int;green int;province type lake land sea string; coastal boolean; terrain type string; continent int

#set true the ones you want to be checked
requirements = [False,False,False,False,False,False,False,False]

#set or add the values to be required to change a province
checks = [[0],0,0,0,'','','',0]

#set true the ones you want to be changed
changes_done = [False,False,False,False,False,False,False,False]

#set values to what you want edited provinces to have changed
change_to = [0,0,0,0,'','','',0]


#everything below does the program
import csv

province_list=[]

with open ('map/definition.csv','r') as csvfile:
    temp_file=csv.reader(csvfile)
    for a in temp_file:
        temp_split_holder = a[0].split(";")
        temp_split_holder[0]=int(temp_split_holder[0])
        temp_split_holder[1]=int(temp_split_holder[1])
        temp_split_holder[2]=int(temp_split_holder[2])
        temp_split_holder[3]=int(temp_split_holder[3])
        temp_split_holder[7]=int(temp_split_holder[7])
        temp_split_holder[4]=temp_split_holder[4].strip("'")
        temp_split_holder[6]=temp_split_holder[6].strip("'")
        province_list.append(temp_split_holder)

amt_req = 0
for i in range(len(requirements)):
    if requirements[i]==True:
        amt_req+=1
for a in range(len(province_list)):
    prov_req_ful=0
    for b in range(len(requirements)):
        if (requirements[b]==True) and ((province_list[a][b]==checks[b]) or (province_list[a][b] in checks[b])):
            prov_req_ful+=1
    if prov_req_ful==amt_req:
        for b in range(len(changes_done)):
            if (changes_done[b]==True):
                province_list[a][b]=change_to[b]

with open('map/definition.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile,delimiter=';')
    writer.writerows(province_list)
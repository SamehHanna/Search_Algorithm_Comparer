# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:54:06 2019

@author: Hemas
"""
import os
from collections import defaultdict

names=[] #List of all algorithms running
values=[] # list of all dictionaries of the algorithms
# loop on all files in the current directory
for filename in os.listdir():   
    # Gets only the files with _output.txt (output file for ProfTrial.py)
    if filename.endswith("_output.txt"):
        # Reading the file and adding the needed values to dictionary
        dic=defaultdict(list) # special type of dictionary (key:list)
        f = open(filename, 'r')
        text = f.read()
        linesLst= text.split('\n')
        #adding the summary of the running first
        dic["Name"].append(filename.split("_")[0])
        dic["Number_of_Calls"].append(linesLst[2].split()[0])
        dic["Time_Taken"].append(linesLst[2].split()[4])
        # adding the number of calls per each method
        for line in linesLst[8:]:
            if (len(line.strip())==0):
                continue
            dic[line.split("(")[1].strip(")")].append(line.split()[0])
        # Add the algorithm name to names and the dictionary to values
        names.append(filename.split("_")[0])
        values.append(dic)

# Adding all the keys (names of calls) togather
allkeys=[]
for dic in values:
    allkeys.extend(dic.keys())
# removing duplications from the list
allkeys=list(dict.fromkeys(allkeys))

#Printing in a good format 
#Printing Title
title_line="{:^26}".format(" Compare Element / Calls ")
for name in names:
    title_line+="| "+ "{:^25}".format(name.capitalize())+" "
title_line+="\n"+"-"*len(title_line)+"\n"
print (title_line)

#Printing the comparison per each item 
for key in allkeys:
    line="{:^25}".format(key)+" "
    for dic in values:
        if key in dic:
            line+= "| "+"{:^25}".format(dic[key][0])+ " "
        else:
            line+= "| "+"{:^25}".format("0")+ " "
    print (line)

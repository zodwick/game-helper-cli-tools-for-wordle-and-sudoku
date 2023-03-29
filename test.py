# import pandas as pd
# df = pd.read_csv("unigram_freq.csv")
# matrix2 = df[df.columns[0]].as_matrix()
# list2 = matrix2.tolist()
# print(list2[0])

import csv

with open("unigram_freq.csv") as f:
    list2 = [row.split(",")[0] for row in f]
    list_5= list(i for i in list2 if len(i)==5)
    # print(list_5)
    
    
filename = "five_letter_worrrds.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
     
    NewList= [[x] for x in list_5]
    # print(NewList)

    # writing the data rows 
    csvwriter.writerows(NewList)
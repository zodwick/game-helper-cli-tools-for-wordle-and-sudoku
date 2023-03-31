# import pandas as pd
# df = pd.read_csv("unigram_freq.csv")
# matrix2 = df[df.columns[0]].as_matrix()
# list2 = matrix2.tolist()
# print(list2[0])

# import csv

# with open("unigram_freq.csv") as f:
#     list2 = [row.split(",")[0] for row in f]
#     list_5= list(i for i in list2 if len(i)==5)
#     # print(list_5)
    

# file = open('five_letter_words.txt','w')
# # file.writelines(list_5)

# for  item in list_5:
# 	file.write(item+"\n")
# file.close()

# file.close()
    
    
# filename = "five_letter_worrrds2.csv"
    
# writing to csv file 
# with open(filename, 'w') as csvfile: 
#     # creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 
     
#     NewList= [[x] for x in list_5]
#     # print(NewList)

#     # writing the data rows 
#     # csvwriter.writerows(NewList)
#     # csvwriter.writerows(list_5)
#     csvfile.close()
    
# with open("five_letter_worrrds.csv", 'r') as f:
#     reader = csv.reader(f)
#     your_list = list(reader)
#     # print(list(i for i in your_list if len(i)==5))
#     print(list(i for i in your_list if len(your_list[0][0])==5))



file = open('five_letter_words.txt','r')
lines = file.readlines()
words=list(i[0:5] for i in lines )
print(words)
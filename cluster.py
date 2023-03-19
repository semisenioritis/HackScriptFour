import pandas as pd 
import random
dataset = pd.read_csv("test2.csv")
row,cols = dataset.shape
subtract = 0 


def ourmod(number):
    if number >= 0:
        return number
    elif number < 0:
        return number*-1

coord = dataset["Text Coordinates"]
max_y = int(coord[0].split(",")[1].split(")")[0])
min_y = int(coord[0].split(",")[1].split(")")[0])

for i in range(row):
    curr_y = int(coord[i].split(",")[1].split(")")[0])
    if curr_y > max_y:
        max_y = curr_y
    elif curr_y < min_y:
        min_y = curr_y

height = max_y - min_y   
# print(height)

max_x = int(coord[0].split(",")[0].split("(")[1])
min_x = int(coord[0].split(",")[0].split("(")[1])

for i in range(row):
    curr_x = int(coord[i].split(",")[0].split("(")[1])
    if curr_x > max_x:
        max_x = curr_x
    elif curr_x < min_x:
        min_x= curr_x

width = max_x - min_x



ver_cluster = [None] * row
# ver_cluster[0]=1
ver_cluster_count=0
band = width/40
for i in range(row):
    x_cord = int(coord[i].split(",")[0].split("(")[1])
    # print(x_cord)
    if ver_cluster[i] is None:
        ver_cluster[i]=ver_cluster_count+1
        for j in range(i+1,row):
            # print(j)
            x_cord_new = int(coord[j].split(",")[0].split("(")[1])
            subtract = float(ourmod(x_cord_new-x_cord))
            print(subtract)
            # print("Ourmod is "+str(ourmod(x_cord_new-x_cord)))
            # print(type(width/40))
            # print(type(subtract))
            if subtract < band:
                # print()
                print(subtract)
                # print(width)
                # print(j)
                ver_cluster[j]=ver_cluster[i]
    else:
        continue


print(ver_cluster)






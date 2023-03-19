import pandas as pd 
import random
dataset = pd.read_csv("test2.csv")

# datasetx= pd.read_csv("test2.csv") but x sorted
# datasety= pd.read_csv("test2.csv") but y sorted
# coordx=datasetx["Text Coordinates"]
# coordy=datasety["Text Coordinates"]


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

bandx_for_ver = width/40
bandy_for_ver = height/15

# This is the Vertical Clustering

ver_cluster = [None] * row
# ver_cluster[0]=1
ver_cluster_count=0

for i in range(row):
    x_cord = int(coord[i].split(",")[0].split("(")[1])
    # print(x_cord)
    if ver_cluster[i] != None:
        continue

    else:
        ver_cluster_count+=1
        ver_cluster[i]=ver_cluster_count
        for j in range(i+1,row):
            # print(j)
            # x_cord_new = int(coordy[j].split(",")[0].split("(")[1])
            x_cord_new = int(coord[j].split(",")[0].split("(")[1])
            subtract = float(ourmod(x_cord_new-x_cord))
            # print(subtract)
            # print("Ourmod is "+str(ourmod(x_cord_new-x_cord)))
            # print(type(width/40))
            # print(type(subtract))
            if subtract < bandx_for_ver:
                # print()
                # print(subtract)
                # print(width)
                # print(j)
                # closest_y_coordinate_to_me= int(coordy[0].split(",")[1].split(")")[0])
                closest_y_coordinate_to_me= int(coord[0].split(",")[1].split(")")[0])
                for k in range (0,j):
                    if ver_cluster[k] == ver_cluster[i]:
                        # k_y_coord= int(coordy[k].split(",")[1].split(")")[0])
                        k_y_coord= int(coord[k].split(",")[1].split(")")[0])
                        # if ourmod(k_y_coord-int(coordy[j].split(",")[1].split(")")[0])) < ourmod(closest_y_coordinate_to_me-int(coordy[j].split(",")[1].split(")")[0])):
                        if ourmod(k_y_coord-int(coord[j].split(",")[1].split(")")[0])) < ourmod(closest_y_coordinate_to_me-int(coord[j].split(",")[1].split(")")[0])):
                            closest_y_coordinate_to_me=k_y_coord
                # if int(coordy[j].split(",")[1].split(")")[0])-closest_y_coordinate_to_me < bandy_for_ver:
                if int(coord[j].split(",")[1].split(")")[0])-closest_y_coordinate_to_me < bandy_for_ver:
                    # ver_cluster[k]=ver_cluster[i]
                    ver_cluster[j]=ver_cluster[i]


print(ver_cluster)

# bandx_for_hor = width/??
bandy_for_hor = height/75

# This is the Horizontal Clustering

hor_cluster = [None] * row
# hor_cluster[0]=1
hor_cluster_count=0

for i in range(row):
    # x_cord = int(coord[i].split(",")[0].split("(")[1])
    # y_cord = int(coordx[i].split(",")[1].split(")")[0])
    y_cord = int(coord[i].split(",")[1].split(")")[0])
    # print(x_cord)
    if hor_cluster[i] != None:
        continue

    else:
        hor_cluster_count+=1
        hor_cluster[i]=hor_cluster_count
        for j in range(i+1,row):
            # print(j)
            # y_cord_new = int(coordx[j].split(",")[1].split(")")[0])
            y_cord_new = int(coord[j].split(",")[1].split(")")[0])
            subtract = float(ourmod(y_cord_new-y_cord))
            # print(subtract)
            # print("Ourmod is "+str(ourmod(x_cord_new-x_cord)))
            # print(type(width/40))
            # print(type(subtract))
            if subtract < bandy_for_hor:
                # print()
                # print(subtract)
                # print(width)
                # print(j)
                # closest_y_coordinate_to_me= int(coordy[0].split(",")[1].split(")")[0])
                # for k in range (0,j):
                #     if hor_cluster[k] == hor_cluster[i]:
                #         k_y_coord= int(coordy[k].split(",")[1].split(")")[0])
                #         if ourmod(k_y_coord-int(coordy[j].split(",")[1].split(")")[0])) < ourmod(closest_y_coordinate_to_me-int(coordy[j].split(",")[1].split(")")[0])):
                #             closest_y_coordinate_to_me=k_y_coord
                # if int(coordy[j].split(",")[1].split(")")[0])-closest_y_coordinate_to_me < bandx_for_hor:
                #     # hor_cluster[k]=hor_cluster[i]
                hor_cluster[j]=hor_cluster[i]


print(hor_cluster)



# Algo for finding tables in the image using the clusters



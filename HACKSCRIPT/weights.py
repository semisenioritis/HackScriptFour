
import pandas as pd
import math
dataset= pd.read_csv('test.csv')
rows, columns = dataset.shape
print(rows)

print(type(dataset["Text Coordinates"][0]))
newdataset = dataset.drop(["Text Content","SrNo"],axis=1)
# coord = dataset["Text Coordinates"][0]
# x=int(coord.split(",")[0].split("(")[1])
# y=int(coord.split(",")[1].split(")")[0])
# print(y)
import numpy as np
coords_names=[]
# coords_array=np.array([])
coords_array=[]
for i in range(rows):
    coord = dataset["Text Coordinates"][i]
    x=int(coord.split(",")[0].split("(")[1])
    y=int(coord.split(",")[1].split(")")[0])
    coords_array.append((x,y))
# print(coords_array) 
 

# create an empty dictionary
def makeArrayofCoordNames(num):
    coord_names=[]
    for i in range(1, num):
        key =  str(i)
        # print(key)
        coord_names.append(key)
    return coord_names

# loop through the range of numbers 1 to 30 and create a dictionary entry for each number

coords_names = makeArrayofCoordNames(rows) 
# print(coord_names)

# to add weights column to dataset
# def addToDataset(sorted_dict):
#     with open('test2.csv', 'r') as input_file:
#         reader = csv.reader(input_file)
#         rows = list(reader)
#     header = rows[0]
#     header.append('weight')
#     with open('test2.csv', 'w', newline='') as output_file:
#         writer = csv.writer(output_file)
#         writer.writerow(header)
#         for i in range (len(sorted_dict)):
#             new_value = sorted_dict['i'].format(i[0])  # Replace this with the logic for computing the new value
#             i.append(new_value)
#             print(i)
#             writer.writerow(i)

def sortWeights(coords_names, weights):
    sort_dict={}
    for i in range (len(coords_names)):
        sort_dict[coords_names[i]]= weights[i]
    # print(sort_dict)
    sorted_dict = dict(sorted(sort_dict.items(), key=lambda x: x[1]))
    print(sorted_dict)
    keys = list(sorted_dict.keys())
    values = list(sorted_dict.values())
    # print(keys, values)
    # addToDataset(sorted_dict)

def calc_weights(coord_array, coord_names):
    weights=[]
    # print(coord_array)
    
    for i in range(len(coord_names)):
        dist=int(math.dist(coord_array[0], coord_array[i]))
        # print(dist)
        weights.append(dist)
    sortWeights(coords_names,weights)
    weights.reverse()
    # print(weights)

calc_weights(coords_array,coords_names)



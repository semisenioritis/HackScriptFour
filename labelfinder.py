# assuming we have a cluster we get have three columns
import pandas as pd 
import random
dataset = pd.read_csv("test.csv")
row,cols = dataset.shape
print(row)
# print(dataset)
random_weights = []
for i in range(0,row):
    random_weights.append(int(random.sample(range(1,100),1)[0]))

dataset["Weights"] = random_weights
dataset = dataset.sort_values("Weights")
label = ""
print(dataset["Weights"].max())
# print(dataset)
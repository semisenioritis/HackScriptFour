import pandas as pd
def sortcsv(filename):
    df = pd.read_csv(filename)
    coord = df["Text Coordinates"]
    row,col = df.shape
    all_x = []
    all_y = []
    for i in range(row):
    y = int(coord[i].split(",")[1].split(")")[0])
    all_x.append(x)
    df["ycoord"] = all_x
# print(df)
    df.sort_values(by=['ycoord'])
    df.drop('ycoord')
    df.to_csv("sortedy.csv")

    for k in range(row):
    x = int(coord[i].split(",")[0].split("(")[1])
    all_y.append(y)

    df["xcoord"] = all_y
    df.sort_values(by='xcord')
    df.drop('xcoord')
    df.to_csv('sortedbyx.csv')
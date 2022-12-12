import pandas as pd

data = pd.read_csv('final_ds2_eng.csv', header = 0, index_col=0)

print(len(data.index))



for i, row in data.iterrows():

    if i % 1000 == 0:
        print(i)

    for j, row2 in data.iterrows():
        if i != j:
            if row.title == row2.title and row.artist == row2.artist:
                data = data.drop(data.index[j])
    
   

print(len(data.index))

data.to_csv('final_ds2_eng2.csv')
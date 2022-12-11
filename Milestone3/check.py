import pandas as pd

data_int = pd.read_csv('final_ds2.csv', header = 0, index_col=0)
data_eng = pd.read_csv('final_ds2_eng.csv', header = 0, index_col=0)


print(data_int.dtypes)

print(data_eng.dtypes)
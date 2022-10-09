import pandas as pd
from random import rd, seed

# set random seed
seed(42)

# read_csv function - selects only 1% of the data
data = pd.read_csv('ds2.csv', skiprows = lambda x: rd.random() > 0.01 and x > 0, header = 0, index_col = 0)
# print("\nRead file\n")

data.pop('id')
# print("\nDeleted id\n")

data.pop('views')
# print("\nDeleted views\n")

data.pop('features')
# print("\nDeleted features\n")

#print("\nDeleted columns\n")

data.to_csv('ds2litecleaned.csv')

#print("\nWrote file\n")
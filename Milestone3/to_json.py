import pandas as pd


# read_csv function - selects only 1% of the data
data = pd.read_csv('final_ds2_eng.csv', encoding_errors = 'ignore', header = 0, index_col = 0)


data.to_json('final_ds2_eng.json', orient = 'records')

#print("\nWrote file\n")
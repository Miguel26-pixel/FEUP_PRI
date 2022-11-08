import pandas as pd


# read_csv function - selects only 1% of the data
data = pd.read_csv('final_ds2.csv', header = 0, index_col = 0)
# print("\nRead file\n")

print("\nDeleted unnamed\n")

print(data.album_release_date)
#print("\nDeleted columns\n")
data['album_release_date'] = data['album_release_date'].apply(lambda x: x[0:4])

print(data.album_release_date)

data.to_csv('final_ds2.csv')

#print("\nWrote file\n")
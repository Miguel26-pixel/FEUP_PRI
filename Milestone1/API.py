import pandas as pd
import csv
import sys
import requests

maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

sourceDbPath = 'ds2.csv'
targetDbPath = 'final_ds2.csv'
authToken = 'BQCXGZmk5zPiT2FrbZ6MBFvAJL6OmTQUSrBIiJUf8QY2GgH15ybkvQUmk8hJvrO-jh3FobC_4hJyx0Si9pGc81wVhgFHbTh8FX0h_aQVzRnveskXfNiv_K4Ts3LPvhB6JUeq3a-lsynBrOppTbNaXaZwocnVcUSCMXsBsoxN6gIFSzLnGb_zJOBT9f4YqdV9bck'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + authToken}

data = pd.read_csv(sourceDbPath, low_memory=(False), encoding=('utf-8'))

f = open(targetDbPath, 'a', errors='ignore')
writer = csv.writer(f)


for index, row in data.iterrows():
        
    url = 'https://api.spotify.com/v1/search?query=track:' + str(row[1]) + '%20artist:' + str(row[3]) + '&type=track'
    r = requests.get(url, headers=headers)
    
    if (r.status_code != 200):
        print("Bad HTTP response at index " + str(index) + ". Status code : " + str(r.status_code))
        continue
    
    if len(r.json()['tracks']['items']) == 0:
        print("Track not found at index " + str(index) + " : " + str(row[1]) + " by artist " + str(row[3]))
        continue
    
    lista = []
    for i in range (1,6): #id,title,tag,artist,year,lyrics
        lista.append(row[i])

    track = r.json()['tracks']['items'][0]
        
    lista.append(track['track_number'])
    lista.append(track['popularity'])
    lista.append(track['explicit'])
    lista.append(track['duration_ms'])
    lista.append(track['album']['release_date'])
    lista.append(track['album']['total_tracks'])
    lista.append(track['album']['name'])
        
    writer.writerow(lista)
    
    print("Sucess at row number " + str(index))

f.close()

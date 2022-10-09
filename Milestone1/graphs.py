import sys
print(sys.executable)

import pandas as pd
from random import random, seed
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import math



# set random seed
seed(42)

# read_csv function - selects only 1% of the data
data = pd.read_csv('ds_edgar.csv', encoding='latin-1', index_col = 0)
# print("\nRead file\n")

def popularityPerYear(df):
    averages = {}
    data = {}
         
    for index, record in df.iterrows():
        if type(record['album_release_date']) != str: continue
        # skip nulls solution for now 
        
        year = record['album_release_date'][0:4] 
        if year in data:
            data[year].append(record.popularity)
        else:
            data[year] = [record.popularity]            

    
    for year in data.keys():
        if year[0] != "1" and year[0] != "2": continue # skip wrong values
        valueSum = 0
        count = 0
        for popularity in data[year]:
            if popularity > 100: continue # skip wrong values 
            valueSum += popularity
            count += 1
        
        averages[year] = valueSum / count

        sortedAverages = dict(sorted(averages.items(), key=lambda x:x[0]))

    plt.bar(list(sortedAverages.keys()), list(sortedAverages.values()), color ='maroon')
    
    print(max(list(sortedAverages.keys())))
    print(min(list(sortedAverages.keys())))
    plt.xlabel("Year")
    plt.ylabel("Popularity(0-100)")
    plt.title("Song popularity per year")

    x = np.linspace(0, 3, 1000)

    # Get axis to the ticks via the current axis
    ax = plt.gca()
    xticks = ax.xaxis.get_major_ticks()
    for i in range(0, len(sortedAverages) - 1):
        xticks[i].set_visible(False)

    xticks[0].set_visible(True)
    xticks[27].set_visible(True)
    xticks[54].set_visible(True)

    xticks[len(sortedAverages) - 1].set_visible(True)
        

    plt.show()
    


def wordCloudRap(df):
    wordStr = ""
    
    for index, record in df.iterrows():
        if record['tag'] == "rap":
            if type(record.lyrics) != str: continue
            word_list = record.lyrics.split()
            for i in range(len(word_list)):
                word_list[i] = word_list[i].lower()
                
            wordStr += " ".join(word_list) + " "
            
            
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate(wordStr)
 
    # plot the WordCloud image                      
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
     
    plt.show()
    
def musicDuration(df):
    album_relative_position = []
    validDurations = []
    section = {'0': [],
               '1': [],
               '2': [],
               '3': [],
               '4': [],
    }
    
    for index, record in df.iterrows():

        if type(record['track_number']) != str or not(record['track_number'].isdigit()) or type(record['album_total_tracks']) != float or math.isnan(record['album_total_tracks']) : continue
    
        ratio = float(record['track_number']) / float(record['album_total_tracks'])
        # print(ratio)
        # print(record['track_number'])
        # print(record['album_total_tracks'])
        # print(type(record['album_total_tracks']))
        i = str(int(ratio // 0.2))

        if i == '5': i = '4'      
        
        section[i].append(int(record['duration_ms']))

    averages = []
    for i in range(0, 5):
        averages.append(sum( section[str(i)]) / len(section[str(i)])) 
        
        

    plt.bar(['0-20', '20-40', '40-60', '60-80', '80-100'], averages, color ='green')
    plt.ylabel("Music duration(ms)")
    plt.xlabel("Album percentil")
    plt.title("Song duration according to whether the track is one of the first or last in an album")
    plt.show()
    


def explicitTag(df):
    
    explicit = {}
    nonExplicit = {}
    
    for index, record in df.iterrows():
        genre = record['tag']
 
        if record['explicit'] == 'True': 
            explicit[genre] = explicit.get(genre, 0) + 1
        else:
            nonExplicit[genre] = nonExplicit.get(genre, 0) + 1
        
    genresPercentage = {}
    
    for genre in explicit:
        genresPercentage[genre] = explicit[genre] / (explicit[genre] + nonExplicit[genre])
        
    labelList = []
    for key in genresPercentage:
        labelList.append(key + "(" + str(round(genresPercentage[key]*100,1)) + "%)")
        

    plt.pie(list(genresPercentage.values()), labels = labelList)
    plt.show()
    
def percentageTag(df):
    
    genres = {}
    counter = 0
       
    for index, record in df.iterrows():
        genre = record['tag']
 
        genres[genre] = genres.get(genre, 0) + 1
        if genre in ['rap', 'rock', 'pop', 'rb', 'misc', 'country']:
            counter += 1
    
        
    genresPercentage = {}
    for key in genres:
        if key in ['rap', 'rock', 'pop', 'rb', 'misc', 'country']:
            genresPercentage[key] = genres[key] / counter
        
    labelList = []
    for key in genresPercentage:
        print(key)
        labelList.append(str(key) + "(" + str(round(genresPercentage[key]*100,1)) + "%)")
        

    plt.pie(list(genresPercentage.values()), labels = labelList)
    plt.show()



def songsPerYear(df):

    data = {}
         
    for index, record in df.iterrows():
        if type(record['album_release_date']) != str: continue
        # skip nulls solution for now 
        
        year = record['album_release_date'][0:4] 
        if year[0] != "1" and year[0] != "2": continue # skip wrong values
        data[year] = data.get(year, 0) + 1
 

    

    sortedData = dict(sorted(data.items(), key=lambda x:x[0]))

    plt.bar(list(sortedData.keys()), list(sortedData.values()), color ='maroon')
    

    plt.xlabel("Year")
    plt.ylabel("Number of songs")
    plt.title("Song number per year")

    x = np.linspace(0, 3, 1000)

    # Get axis to the ticks via the current axis
    ax = plt.gca()
    xticks = ax.xaxis.get_major_ticks()
    for i in range(0, len(sortedData) - 1):
        xticks[i].set_visible(False)

    xticks[0].set_visible(True)
    xticks[27].set_visible(True)
    xticks[54].set_visible(True)

    xticks[len(sortedData) - 1].set_visible(True)
        

    plt.show()

def wordCloud(df):
    wordStr = ""
    
    for index, record in df.iterrows():
        if type(record.lyrics) != str: continue
        word_list = record.lyrics.split()
        for i in range(len(word_list)):
            word_list[i] = word_list[i].lower()
            
        wordStr += " ".join(word_list) + " "
            
            
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate(wordStr)
 
    # plot the WordCloud image                      
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
     
    plt.show()
    
    
def musicDurationPerDecade(df):
    # averages = {}
    # data = {}
    
    data = []
    
    for index, record in df.iterrows():
        if not(str(record['duration_ms']).isdigit()) or math.isnan(float(record['duration_ms'])): continue
        #if not(record['duration_ms'].isdigit()): continue
        # skip nulls solution for now 
         
        data.append(int(record['duration_ms']))
        print(int(record['duration_ms']))
        
    print(max(data))
    print(min(data))
    plt.hist(data,bins=10, range = (0, 500000), color = 'Orange')
    
    plt.xlabel("Song duration")
    plt.ylabel("Number of songs in group")
    plt.title("Song duration histogram")
    plt.show() 
        
    # for index, record in df.iterrows():
    #     if type(record['album_release_date']) != str: continue
    #     # skip nulls solution for now 
        
    #     year = record['album_release_date'][0:4] 
    #     if (year[0] != "1" and year[0] != "2") or not(record['duration_ms'].isdigit()): continue # skip wrong values
        
    #     data[str(int(year) // 10) + '0'] = data.get(str(int(year) // 10) + '0', []) + [int(record['duration_ms'])]

    
    # for year in data.keys():      
    #     averages[year] = sum(data[year]) / len(data[year])

    #     sortedAverages = dict(sorted(averages.items(), key=lambda x:x[0]))

    # plt.hist(list(sortedAverages.keys()), list(sortedAverages.values()), color ='green')
    

    

    # x = np.linspace(0, 3, 1000)

    # # Get axis to the ticks via the current axis
    # ax = plt.gca()
    # xticks = ax.xaxis.get_major_ticks()
    # for i in range(0, len(sortedAverages) - 1):
    #     xticks[i].set_visible(False)

    # xticks[0].set_visible(True)
    # xticks[4].set_visible(True)
    # xticks[8].set_visible(True)

    # xticks[len(sortedAverages) - 1].set_visible(True)
        

    

#wordCloudRap(data)
#popularityPerYear(data)
#musicDuration(data)
#explicitTag(data)
#percentageTag(data)
#songsPerYear(data)
#wordCloud(data)
#musicDurationPerDecade(data)











# data.pop('id')
# # print("\nDeleted id\n")

# data.pop('views')
# # print("\nDeleted views\n")

# data.pop('features')
# print("\nDeleted features\n")

#print("\nDeleted columns\n")

#data.to_csv('ds_test.csv')

#print("\nWrote file\n")
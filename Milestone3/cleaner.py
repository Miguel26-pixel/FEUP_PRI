import pandas as pd

# from textblob import TextBlob

from spacy.language import Language
from spacy_langdetect import LanguageDetector
import spacy


def get_lang_detector(nlp, name):
    return LanguageDetector()

nlp = spacy.load('en_core_web_sm')  # 1
Language.factory("language_detector", func=get_lang_detector)
nlp.add_pipe('language_detector', last=True)



# set random seed
#seed(42)

# read_csv function - selects only 1% of the data
#data = pd.read_csv('ds2.csv', skiprows = lambda x: rd.random() > 0.01 and x > 0, header = 0, index_col = 0)
data = pd.read_csv('final_ds2.csv', header = 0, index_col=0)

for i, row in data.iterrows():
    # b = TextBlob(row.lyrics)
    # b.detect_language()
    # print(i, b.detect_language())
    # languages.append(b.detect_language())
    if i % 1000 == 0:
        print(i)
    
    doc = nlp(row.lyrics) 
    detect_language = doc._.language['language']
    if detect_language != 'en':
        if i < len(data.index):
            data = data.drop(data.index[i])


# print("\nRead file\n")

#data.pop('id')
# print("\nDeleted id\n")

#data.pop('views')
# print("\nDeleted views\n")

#data.pop('features')
# print("\nDeleted features\n")

#print("\nDeleted columns\n")

data.to_csv('final_ds2_eng.csv')

#print("\nWrote file\n")
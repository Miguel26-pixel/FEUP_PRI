import pandas as pd

from textblob import TextBlob

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

languages = []

for index, row in data.iterrows():
    # b = TextBlob(row.lyrics)
    # b.detect_language()
    # print(index, b.detect_language())
    # languages.append(b.detect_language())
    
    doc = nlp(row.lyrics) #3
    detect_language = doc._.language #4
    languages.append(detect_language['language'])

print(languages.count('en'))
print(len(languages))


# print("\nRead file\n")

data.pop('id')
# print("\nDeleted id\n")

data.pop('views')
# print("\nDeleted views\n")

data.pop('features')
# print("\nDeleted features\n")

#print("\nDeleted columns\n")

#data.to_csv('ds2litecleaned.csv')

#print("\nWrote file\n")
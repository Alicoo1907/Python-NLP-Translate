import csv
import os, glob
import pandas as pd
from deep_translator import GoogleTranslator
#Defines
encoding = 'utf-8-sig'
targetLang = 'tr'

# READ ENGLİSH DATAS
dataset = pd.read_csv('NAWL.csv', sep=';')

# preprocess
meanings = dataset['Meanings'].copy()
ENGdefinitons = dataset['English Definitions'].copy()

# Translate Meanings
with open('Data/meantranslate.csv', 'w', encoding=encoding) as f1:
    writer = csv.writer(f1, delimiter=' ', lineterminator='\n', )
    writer.writerow(["Türkçe Anlam"])
    for i in range(len(meanings.index)):
        meantranslated = GoogleTranslator(source='auto', target=targetLang).translate(str(meanings.loc[[i]]))
        writer.writerow([meantranslated.split(" ", 1)[1].split('\n')[0]])
        print(" {}. meanings".format(i))

# Translate Definitons
with open('Data/deftranslate.csv', 'w', encoding=encoding) as f1:
    writer = csv.writer(f1, delimiter=' ', lineterminator='\n', )
    writer.writerow(["Türkçe Açıklaması"])
    for i in range(len(ENGdefinitons.index)):
        deftranslated = GoogleTranslator(source='auto', target=targetLang).translate(str(ENGdefinitons.loc[[i]]))
        writer.writerow([deftranslated.split(" ", 1)[1].split('\n')[0]])
        print(" {}. definition".format(i))

meanHeader = ['Türkçe Anlam']
meaningsDF = pd.read_csv('Data/meantranslate.csv', names=meanHeader)

DefHeader = ['Türkçe Açıklaması']
definitionsDF = pd.read_csv('Data/deftranslate.csv', names=DefHeader)

#meaning + def 1 csv
meanDEF = pd.concat([meaningsDF, definitionsDF], axis=1)
meanDEF.to_csv("Data/meanDEF.csv", encoding=encoding, index=False, sep=';', quotechar=",",
           header=False, columns=['Türkçe Anlam', 'Türkçe Açıklaması'])

#read mean +def csv
meanDEFDF = pd.read_csv('Data/meanDEF.csv', sep=';')

#concat csv 4 column 2 english two target language
fullTranslated = pd.concat([dataset, meanDEFDF], axis=1)
fullTranslated.to_csv("translated.csv", encoding=encoding, index=False, sep=';',
            header=False)

#İf you want to keep all file delete this 4 lines
dir = 'Data/'
filelist = glob.glob(os.path.join(dir, "*"))
for f in filelist:
    os.remove(f)

last = pd.read_csv('translated.csv', sep=';')
print(last.head())

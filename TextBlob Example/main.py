import sys
from importlib import reload

from textblob import TextBlob

reload(sys)
sys.getdefaultencoding()  # use this for Python3

"""
url = 'input.txt'
file = open(url)
input_sen = file.read()
"""


def PositiveorNegative(polarity):
    if blob.sentiment.polarity < 0:
        print("Negative")
    elif blob.sentiment.polarity > 0:
        print("Positive")
    else:
        print("Neutral")

try:
    while True:
        print('Döngüyü kırmak için CTRL-C basınız')
        input_sen = str(input("İngilizce Bir Metin Girin: "))

        blob = TextBlob(input_sen)
        PositiveorNegative(blob.sentiment.polarity)
        print(blob.sentiment)

        print(type(blob.translate(to='tr')))


        def FileSave(filename, content):
            with open(filename, "a") as myfile:
                myfile.write(content + '\n')


        FileSave('translated.txt', str(blob.translate(to='tr')))

        for word, pos in blob.tags:
            print(word, pos)
except KeyboardInterrupt:
    pass

"""
CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: “there is” … think of it like “there exists”)
FW foreign word
IN preposition/subordinating conjunction
JJ adjective ‘big’
JJR adjective, comparative ‘bigger’
JJS adjective, superlative ‘biggest’
LS list marker 1)
MD modal could, will
NN noun, singular ‘desk’
NNS noun plural ‘desks’
NNP proper noun, singular ‘Harrison’
NNPS proper noun, plural ‘Americans’
PDT predeterminer ‘all the kids’
POS possessive ending parent‘s
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO to go ‘to‘ the store.
UH interjection errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when
"""

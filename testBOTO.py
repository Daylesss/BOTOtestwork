import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pymorphy2 import MorphAnalyzer
from nltk.util import ngrams


with open('russian_words', 'r', encoding='utf-8') as list_ru_words:

    russian =list_ru_words.readlines()
russian_words=[]
for word in russian:
   russian_words.append(word.rstrip('\n'))



definable='ля ля ля ля ля'

definable=definable.lower()

definable = re.sub(r'\W+', ' ', definable)
definable = re.sub(r'\d+', '', definable)

words=word_tokenize(definable, language='russian')

stop_words= set(stopwords.words('russian'))
words = [word for word in words if word not in stop_words]

morph = MorphAnalyzer()
lemmas = [morph.parse(word)[0].normal_form for word in words]


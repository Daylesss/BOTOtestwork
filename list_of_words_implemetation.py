import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pymorphy2 import MorphAnalyzer
from nltk.util import ngrams

# обработка предложения и проверка по словарю

with open('russian_words.txt', 'r', encoding='utf-8') as list_ru_words:  #создание словаря русских слов файл russian words есть в BOTOtestwork.


    russian =list_ru_words.readlines()
russian_words=[]
for word in russian:
   russian_words.append(word.rstrip('\n'))

# токенизация и лемматизация текста для последующей обработки и поска по словарю.

definable=input('Введиите текст для определения:')

definable=definable.lower()

definable = re.sub(r'\W+', ' ', definable)
definable = re.sub(r'\d+', '', definable)

words=word_tokenize(definable, language='russian')

stop_words= set(stopwords.words('russian'))
words = [word for word in words if word not in stop_words]

morph = MorphAnalyzer()
lemmas = [morph.parse(word)[0].normal_form for word in words]

# проверка наличия слов в списке.
# для того, чтобы текмт можно было бы считаь осмысленны в нём должно быть хотя бы одно слово русского языка.

count=0
for lemma in lemmas:
    if  lemma in russian_words: count+=1 break

if count>0: print(' в тексте есть слова русского языка')
else: 'возможно слов русского языка в тексте нет, либо в нём содержатся неологизмы и сленговые выражения'


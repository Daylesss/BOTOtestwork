from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import random
from sklearn.pipeline import Pipeline
from nltk.util import ngrams

# ещё один способ решения, использующий наивные классификаторы Байеса.
# не отличается высокой точностью
# гиперпараметры нужно уточнять


bileberda=[]
alph=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ё']

for _ in range(100000):             # содание датасета "бессмысленных слов"
    bil=''
    for _ in range(random.randint(1,25)):
        bil= bil + alph[random.randint(0,len(alph))-1]
    bileberda.append(bil)




with open('russian_words.txt', 'r', encoding='utf-8') as list_ru_words:     # создание списка русских слов (96 тысяч) 

    russian =list_ru_words.readlines()
russian_words=[]
for word in russian:
   russian_words.append(word.rstrip('\n'))


print(russian_words)


# Подготовка данных


# Формирование обучающих данных и меток
data = russian_words + bileberda
labels = ['русское слово'] * len(russian_words) + ['бессмысленный набор букв'] * len(bileberda)


# Создание пайплайна для классификации
pipeline = Pipeline([
    ('vect', CountVectorizer(ngram_range=(1,2))),
    ('tfidf', TfidfTransformer(use_idf=False)),
    ('clf', MultinomialNB(alpha=0.1)),
])

parameters = {
    'vect__ngram_range': [(1, 1), (1, 2)],  # Размерность N-грамм
    'tfidf__use_idf': (True, False),  # Использование TF-IDF
    'clf__alpha': [0.1, 0.5, 1.0],  # Гиперпараметр сглаживания
}

Создание объекта GridSearchCV для поиска по сетке
grid_search = GridSearchCV(pipeline, parameters, cv=5, scoring='accuracy') #взят наиболее примитиная метрика accuracy
grid_search.fit(data, labels)

Вывод лучших параметров и оценки производительности
print("Лучшие параметры: ", grid_search.best_params_)
print("Лучшая оценка:", grid_search.best_score_)
# Обучение модели
pipeline.fit(data, labels)
# Пример использования модели
input_word = input('Введите слово или набор букв для проверки: ')
prediction = pipeline.predict([input_word])
print(prediction)

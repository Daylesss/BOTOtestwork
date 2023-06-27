import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import emoji
import pymorphy3


# Функция для определения, есть ли хотя бы один токен из русских букв в предложении.
# Исключает предложения на других языках, но допускает предложения типа: 'Люблю Linking park'

def is_one_russian_word(tokens: list, threeshold_russian_words: float = 0) -> bool:
    count=0
    for word in tokens:
        if all(ord(char) >= 1040 and ord(char) <= 1103 for char in word):
            if threeshold_russian_words==0: # при default=0 значении возвращает True
                return True                 # если есть хотя бы один токен из букв русского алфавита.
            count+=1
    # threeshold_russian_words отвечает за минимальный процент содержания токенов из русских букв. 
    return count/len(tokens)>=threeshold_russian_words


# основная функция
# сравнивает суммарное значение score из MorphAnalyzer для лемматизации слова с пороговым.
# threshold - пороговое значение. (настраиваемо)

def is_meaningfull(user_text: str, threshold: float =0.834, threeshold_russian_words: float = 0, remove_stopwords: bool = False) ->bool:

    # проверка на эмодзи. Пропускает сообщения только из эмодзи.

    if emoji.is_emoji(user_text) and len(user_text)<4:
        return True
    
    # len(user_text)<4 исключает спам эмодзи.

    elif emoji.is_emoji(user_text) and len(user_text)>=4:
        return False
    
    # обработка предложения. Исключение всех 'небуквенных' значений.
    user_text= user_text.lower()
    user_text = re.sub(r'\W+', ' ', user_text)
    user_text = re.sub(r'\d+', '', user_text)

    # токенизация
    tokens = words=word_tokenize(user_text, language='russian')

    if is_one_russian_word(tokens, threeshold_russian_words): # проверка на содержание токенов из русских букв

        morph= pymorphy3.MorphAnalyzer()

    # удаление стоп-слов если указано remove_stopwords = True
    # Удаление стоп-слов влияет на score.
        if remove_stopwords:
            stop_words= set(stopwords.words('russian'))
            tokens= [token for token in tokens if token not in stop_words]

        # получение score для каждого токена и сравнение.

        score=0

        for word in tokens:
            p= morph.parse(word)
            score += p[0].score   # суммарный score
        if score>len(tokens)*threshold:
            return True   #если score больше threshold, предложение считается осмысленным.
        else: return False  # в противном случае False

    else:
        return False  # возвращает False если процент токенов из русских букв ниже указанного.

text = 'Было челленджево, но суперски. респект'

print(is_meaningfull(text))

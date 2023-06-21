import openai
#простейший метод с точки зрения реализации, при этом наиболее точный.
openai.api_key = 'API KEY'
# функция определяет, является ли фраза осмысленной на основе того, может ли Chatgpt  сгенерировать следующее слово
def is_nonsense_string(input_string):
    response = openai.Completion.create(
        engine='text-davinci-003', 
        prompt=input_string,
        max_tokens=1, # достаточно одного токена для генерации
        n=1,
        stop=None,
        temperature=0, # исключаем случайные ответы для большей точности
        top_p=1,
        frequency_penalty=0, #предпочтения к определённым словам и фразам на нуле
        presence_penalty=0
    )
    
    completion_text = response.choices[0].text.strip() # возврат сгенерированного слова (или пустой строки)
    

    if completion_text == '': #проверка
        return True
    
    return False

# Примеры тестовых строк
test_strings = ['ыдвшоаыолвтас', 'ля', 'good', '123', '👍', 'Все ок', 'было челенджево, но суперски. респект', '1. Интересно 2. Креативно 3. всё понятно.']

# Проверка строк на бессмысленность
for string in test_strings:
    if not is_nonsense_string(string):
        print(f"{string} - бессмысленная строка")
    else:
        print(f"{string} - допустимая строка")

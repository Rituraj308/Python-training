from translate import Translator
translator = Translator(to_lang="ja")

try:
    with open('translator.txt', mode='r',encoding='utf-8') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('translator-ja.txt', mode='w',encoding='utf-8') as my_file2:
             my_file2.write(translation)
except FileNotFoundError as e:
    print("Check your path ")

from translate import Translator           # we have to install translator package from command prompt( by typing pip3 install translotr)
translator = Translator(to_lang="ja")
# we have to create text file or notepad file and write a sentence in it and save it in our pycharm path folder
try:
    with open('translator.txt', mode='r',encoding='utf-8') as my_file:    # here we are use encoding='utf-8' because we were getting error
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('translator-ja.txt', mode='w',encoding='utf-8') as my_file2:
             my_file2.write(translation)
except FileNotFoundError as e:
    print("Check your path ")

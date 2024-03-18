with open('tests.txt', mode='a') as my_file:
    text = my_file.write('hey its me!')
    print(text)
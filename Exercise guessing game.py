from random import randint
#generate a number 1~10
answer = randint(1,10)
#input from user?

#check that input is a number 1~10
while True:
    try:
        guess = int(input('guess a number 1~10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are genius!')
                break
    except ValueError:
        print('pls enter a number')
        continue

#check if the number is right guess. otherwise
#ask again.
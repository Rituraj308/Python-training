while True:
    try:
        age = int(input('what is your age? '))           # we use 'int' to allow code to accept only numbers
        10/age
    except ValueError:
        print("please enter a number")
        continue
    except ZeroDivisionError:
        print("please enter a number higher than 0")
    else:
        print('thank you!')
        break
    finally:
        print('ok am finally done!')
    print('can you hear me ?')
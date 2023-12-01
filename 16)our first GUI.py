#EXCERSISE
Picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
#1 itrate over picture.
 # if 0 -> print ' '
 # if 1 -> print *
for row in Picture:
    for pixel in row:
        if (pixel == 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('    ')



from random import randint

for i in range(randint(1,9)):
    file_name = ''
    for k in range(randint(1,9)):
        file_name += str(randint(0,9))
    file_name += '.txt'
    print(file_name)







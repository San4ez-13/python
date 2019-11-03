f = open('sasha.txt','r')
# a - дозапись w - перезапись r - чтение
for line in range(5):
    line = f.readline()
    print(line, end = '')
f.close()



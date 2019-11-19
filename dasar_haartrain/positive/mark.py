import os

for img in os.listdir('rawdata'):
    line = 'rawdata/' + img + ' 1 10 30 73 54\n'
    with open('info.txt','a') as f:
        f.write(line)

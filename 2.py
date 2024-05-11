f = open('filename.txt').readline()
_max = -10**30
count = 0
for i in range(len(f)):
    if f[i] == 'X':
        count += 1
        _max = max(_max, count)
    else:
        count = 0
print(_max)

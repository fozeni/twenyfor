f = open('filename.txt').readline()
f = 'XXXYYYYAAYAYAAYYYYYZZZXXXX'
_max = -10**30
count = 0
for i in range(f):
    if f[i] == 'X':
        count += 1
        _max = max(_max, count)
    else:
        count = 0

f = open('').readline()
count = 0
_max = 0
for i in range(len(f)-1):
    if f[i] != f[i+1]:
        count += 2
        _max = max(_max,count)
    else:
        count = 0
print(count-1)

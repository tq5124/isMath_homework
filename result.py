import sys
import string
f = open("base_table.txt")
line = f.readline()
matrix = []
while line:
    strarr = line.splitlines(0)[0].split('.')
    numarr = 0
    for i in strarr:
        numarr <<= 8
        numarr |= (int)(string.atoi(i))
    matrix.append(numarr)
    line = f.readline()
f.close()

def todecimal(i):
    res = ""
    j = 8
    while j > 0:
        if(j!=8):
            res = "." + res
        res = str(i & 255) + res
        i >>= 8
        j -= 1
    return res

def rtobinaryarr(i):
    #i %= 256
    res = [0] * 16
    j = 0
    while i!=0:
        if( i & 1 ):
            res[j] = 1
        j += 1
        i >>= 1
    res.reverse()
    return res

output = open('result.txt', 'w')
index = 1
while index < 65536:
    todo = rtobinaryarr(index)
    tmp = 0
    l = 0
    while l < 16:
        if(todo[l]):
            tmp ^= matrix[l]
        l += 1
    output.write(str(index)+":\t"+todecimal(tmp)+"\n")
    index += 1;
print "done!"
output.close()

import sys
import string
import os

f = open("base_table.txt")
line = f.readline()
matrix = []
base_scale = 0
while line:
    strarr = line.splitlines(0)[0].split('.')
    numarr = 0
    for i in strarr:
        numarr <<= 8
        numarr |= (int)(string.atoi(i))
    matrix.append(numarr)
    base_scale += 1
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
    res = [0] * base_scale
    j = 0
    while i!=0:
        if( i & 1 ):
            res[j] = 1
        j += 1
        i >>= 1
    res.reverse()
    return res

def remove_repeat(base):
    f = open("temp_1.txt","r")
    fn = open("temp_2.txt","w")
    baseresf = open("base_no_repeat.txt","a")
    baseresf.write(base)
    baseresf.close()
    
    line = f.readline()
    while line:
        if(line!=base):
            fn.write(line)
        line = f.readline()
        
    f.close()
    fn.close()
        
    os.rename('temp_1.txt','temp.txt')
    os.rename('temp_2.txt','temp_1.txt')
    os.remove('temp.txt')

#write base
output = open('temp_1.txt', 'w')
index = 1
upper = 2**base_scale
while index < upper:
    todo = rtobinaryarr(index)
    tmp = 0
    l = 0
    while l < base_scale:
        if(todo[l]):
            tmp ^= matrix[l]
        l += 1
    output.write(str(tmp)+"\n")
    index += 1;
print "base written done!"
output.close()

basef = open("base_no_repeat.txt","w")
basef.close()
base_index = 0
while(1):
    f = open("temp_1.txt","r")
    base = f.readline()
    f.close();
    if(base):
        print base_index
        remove_repeat(base)
        base_index += 1
    else:
        break

print "base no repeat done!"
   
#output.write(str(index)+":\t"+todecimal(tmp)+"\n")


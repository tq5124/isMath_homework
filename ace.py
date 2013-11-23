import random,time

class GF:
    def __init__(self, num=0, bit=8):
        self.num = num
        self.bit = bit

    def display(self):
        b = bin(self.num)
        b = b[2:].rjust(self.bit, '0')
        print b

    def __add__(self, other):
        return self.num ^ other.num

    def __mul__(self, other):
        list = []
        y = self.num
        x = bin(other.num)
        x = x[2:]
        for i in x[::-1]:
            if (i == '1'):
                list.append(y)
            y = y << 1
        result = 0
        for i in list:
            result = result ^ i
        return mod(result)

def get_bit(num):
    result = 0
    i = 1
    while (i <= num):
        i = i << 1
        result = result +1
    return result

def _mod(num, m = 283):
    diff = get_bit(num) - 9
    if (diff < 0):
        return num
    else:
        return num ^ (m << diff)

def mod(num, m = 283):
    re = _mod(num)
    while (re != num):
        num = re
        re = _mod(num)
    return num

def main():
    a = GF(0b10000111)
    b = GF(0b10000011)
    c = GF(283)
    c.num = a*b
    c.display()
    print c.num


def test(time = 100000, bit=8):
    for i in range(time):
        a = GF(random.randint(0, 2**bit-1))
        b = GF(random.randint(0, 2**bit-1))
        c = GF()
        c.num = a * b

def create_multable(i_all = 256, j_all = 256, file = 'mul_table.txt'):
    f = open(file, 'w')
    result = ""
    a = GF()
    b = GF()
    c = GF()
    for i in range(i_all):
        for j in range(j_all):
            a.num = i
            b.num = j
            c.num = a * b
            result += str(c.num)
            if (j != j_all-1):
                result += ','
        if (i != i_all-1):
            result += '\n'
    f.write(result)
    f.close()

#main()
t = time.time()
create_multable()
print time.time() - t
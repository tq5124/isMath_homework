# -*- coding: utf-8 -*-
#!/usr/bin/python

import math,random,time,string

class Pol_domain:
    #值
    val = -1
    #不可约多项式
    pol = -1
    #构造函数：283=100011011=x^8+x^4+x^3+x+1
    def __init__(self,val,pol=283):
        self.val = val
        self.pol = pol
    def __del__(self):
        pass
    #加法重载：按位加法等同于按位异或
    def __add__(self,other):
        if(self.pol == other.pol):
            return Pol_domain(self.val^other.val,self.pol)
        else:
            raise "error:多项式不一致"
    #减法重载：二进制下，减法与加法相同
    def __sub__(self,other):
        if(self.pol == other.pol):
            return Pol_domain(self.val^other.val,self.pol)
        else:
            raise "error:多项式不一致"
    #乘法重载
    def __mul__(self,other):
        if(self.pol == other.pol):
            temp_o_val = other.val
            result = 0
            i = 0
            while(temp_o_val > 0):
                result = result ^ ((self.val * (temp_o_val % 2)) << i)
                i = i+1
                temp_o_val = temp_o_val / 2
            return Pol_domain(result,self.pol).standardize()
        else:
            raise "error:多项式不一致"
    #标准化函数：使值为不超过不可约多项式的多项式
    def standardize(self):
        temp_val = self.val
        val_b_len = get_num_len(temp_val)
        pol_b_len = get_num_len(self.pol)
        while(val_b_len >= pol_b_len):
            temp_val = temp_val ^ (self.pol << (val_b_len - pol_b_len))
            val_b_len = get_num_len(temp_val)
        self.val = temp_val
        return Pol_domain(temp_val,self.pol)
#获取数字二进制长度
def get_num_len(num):
    num = int(num)
    i = 0
    if (num == 0):
        i = 1
    while (num > 0):
        i = i + 1
        num = num / 2
    return i
#创建乘法表
def create_mul_table(pol = 283):
    file_object = open('mul_table.txt', 'w')
    pol_len = get_num_len(pol)
    val_len = pol_len - 1
    for i in range(2**val_len):
        for j in range(2**val_len):
            file_object.write(str((Pol_domain(i,pol) * Pol_domain(j,pol)).val))
            if (j != 2**val_len-1):
                file_object.write(",")
        if(i != 2**val_len-1):
            file_object.write("\n")
    file_object.close()
    return
#读取乘法表
def get_mul_table():
    file_object = open('mul_table.txt', 'r')
    data = file_object.read().split('\n')
    for i in range(len(data)):
        data[i] = data[i].split(',')
        for j in range(len(data[i])):
            data[i][j] = string.atoi(data[i][j])
    file_object.close()
    return data
#建立随机数表，方便不同方案测试相同数据
def create_random_table(n = 100000,len = 8):
    file_object = open('random.txt', 'w')
    i = 0
    while(i < n):
        file_object.write(str(int (random.random() * (2**len))) + "," + str(int (random.random() * (2**len))))
        i = i + 1
        if (i != n):
            file_object.write('\n')
    file_object.close()
    return
#普通乘法方式    
def mul_by_tradition():
    input_file = open('random.txt','r')
    all_data = input_file.read().split('\n')
    input_file.close()
    output_file = open('test2.txt', 'w')
    starttime = time.clock()
    for i in all_data:
        j = i.split(',')
        a = string.atoi(j[0])
        b = string.atoi(j[1])
        output_file.write('a = ' + str(a) + ',' + 'b = ' + str(b) + ',' + 'a * b = ' + str((Pol_domain(a) * Pol_domain(b)).val) +'\n')
    endtime = time.clock()
    output_file.write('用时：' + str(endtime - starttime))
    print (endtime - starttime)
    output_file.close()
    return 
#乘法表方式
def mul_by_table():
    input_file = open('random.txt','r')
    all_data = input_file.read().split('\n')
    input_file.close()
    table = get_mul_table()
    output_file = open('test3.txt', 'w')
    starttime = time.clock()
    for i in all_data:
        j = i.split(',')
        a = string.atoi(j[0])
        b = string.atoi(j[1])
        output_file.write('a = ' + str(a) + ',' + 'b = ' + str(b) + ',' + 'a * b = ' + str(table[a][b]) +'\n')
    endtime = time.clock()
    output_file.write('用时：' + str(endtime - starttime))
    print (endtime - starttime)
    output_file.close()
    return
#归约异或
def reduce_xor(num):
    n = num
    n = (n&0x55555555) + ((n>>1)&0x55555555)
    n = (n&0x33333333) + ((n>>2)&0x33333333)
    n = (n&0x0f0f0f0f) + ((n>>4)&0x0f0f0f0f)
    n = (n&0x00ff00ff) + ((n>>8)&0x00ff00ff)
    n = (n&0x0000ffff) + ((n>>16)&0x0000ffff)
    return n % 2

#测试一个线性方程
#测试阶段
def test_one_fucntion(function,table = []):
    all_s = 0
    sucess = 0
    for i in range(256):
        for j in range(256):
            if(reduce_xor(((i << 8) + j) & function)):
                sucess = sucess + 1
            all_s = all_s + 1
    return sucess * 1.0 / all_s
    
#线性方程偏差
#测试阶段，只测试前8位，即对256*256循环即可
def linear_deviation():
    output_file = open('linear_deviation.txt', 'w')
    starttime = time.clock()
    i = 0
    while (i < 2**16):
        output_file.write(str(i) + " " + str(test_one_fucntion(i)) + '\n')
        output_file.write(str(time.clock() - starttime) + '\n')
        i = i + 1
    endtime = time.clock()
    output_file.write('用时：' + str(endtime - starttime))
    print (endtime - starttime)
    output_file.close()
    return

#全局变量table
m_table = get_mul_table()
#线性方程运算
def l_f(i,j,k,l):
    y3 = m_table[2][i] ^ m_table[1][j] ^ m_table[1][k] ^ m_table[3][l]
    y2 = m_table[3][i] ^ m_table[2][j] ^ m_table[1][k] ^ m_table[1][l]
    y1 = m_table[1][i] ^ m_table[3][j] ^ m_table[2][k] ^ m_table[1][l]
    y0 = m_table[1][i] ^ m_table[1][j] ^ m_table[3][k] ^ m_table[2][l]
    return str(y3) + '.' + str(y2) + '.' + str(y1) + '.' + str(y0) + '\n'
#计算一组2^24输入对应的输出打一个包
def cal_i_o_table(i_start):
    #i_start = 0#int (random.random() * (2**8))
    j_start = 0#int (random.random() * (2**8))
    k_start = 0#int (random.random() * (2**8))
    l_start = 0#int (random.random() * (2**8))   
    n = 2 << 7
    i_end = i_start + 1#n
    j_end = j_start + n
    k_end = k_start + n
    l_end = l_start + n

    #output_file = open('linear_deviation.txt', 'w')
    starttime = time.clock()
    i = i_start
    while (i < i_end):
        output_file = open('./linear_deviation/' + str(i) + '.txt', 'w')
        j = j_start
        while (j < j_end):
            k = k_start
            while (k < k_end):
                l = l_start
                while (l < l_end):
                    y = l_f(i,j,k,l)
                    output_file.write(str(i) + '.' + str(j) + '.' + str(k) + '.' + str(l) + ',' + y)
                    l = l +1
                k = k + 1
            j = j +1
        i = i +1
        output_file.close()
    endtime = time.clock()
    #output_file.write('用时：' + str(endtime - starttime))
    print (endtime - starttime)
    #output_file.close()
    return

def main():
    for i in range(256):
        cal_i_o_table(i)
    return
if   __name__  ==  '__main__':
    main()

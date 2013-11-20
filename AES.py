# -*- coding: utf-8 -*-
#!/usr/bin/python

import math,random

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

def get_num_len(num):
    num = int(num)
    i = 0
    if (num == 0):
        i = 1
    while (num > 0):
        i = i + 1
        num = num / 2
    return i
def main():
    file_object = open('test.txt', 'w+')
    i = 0
    while(i < 100000):
        a = int (random.random() * 256)
        b = int (random.random() * 256)
        file_object.write("a = " + str(a) + "," + "b = " + str(b) + "," + "a * b = " + str((Pol_domain(a) * Pol_domain(b)).val) +"\n")
        i = i + 1
    file_object.close()

import time
import random

class field:
	def __init__(self,val):
		self.val=val
	def mul(self,num):
		a=self.val
		b=num.val
		q=283 #x**8+x**4+x**3+x+1
		bit=1
		m=0
		i=0
		while i != 8:
			if b&bit != 0:
				m^=(a<<i)
			i+=1
			bit<<=1
		bit=2**7
		i=6
		while i >= 0:
			if m & (bit<<7) != 0:
				m^=(q<<i)
			i-=1
			bit>>=1
		return field(m)
	def add(self,num):
		return field(self.val ^ num.val)
		
def main():
	i=0
	t=time.time()
	while i<100000:
		i+=1
		a=field(random.randint(0,256))
		b=field(random.randint(0,256))
		c=a.mul(b)
	t=time.time()-t
	print t
	
if __name__ == '__main__':
	main()

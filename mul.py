def mul(a,b):
	q=283 #x**8+x**4+x**3+x+1
	bit=1
	m=0
	i=0
	while i != 8:
		if b&bit != 0:
			m+=(a<<i)
		i+=1
		bit<<=1
	bit=2**7
	i=6
	while i >= 0:
		if m & (bit<<7) != 0:
			m^=(q<<i)
		i-=1
		bit>>=1
	return m
	
def test():
	i=0
	t=time.time()
	while i<100000:
		i+=1
		mul(random.randint(0,256),random.randint(0,256))
	t=time.time()-t
	return t
import time
import random
class m:#multinomial
    __c_s = 0L #coefficient_sequence
    def __init__(self,c_s):
        self.__c_s = c_s
        self._m();        
    def _m(self):
        t = self.__c_s >> 8
        if ( t ):
            i = 1;
            while ( ( t >> i ) != 0 ):
                i+=1;
            self.__c_s ^= ( 283 << ( i -1 ) )
            self._m();
    def __add__(self,T):
        return m( self.__c_s ^ T.__c_s )    
    def __mul__(self,T):
        r = 0L
        t = self.__c_s
        T_t = T.__c_s
        while( t ):
            if( t & 1 ):
                r ^= T_t
            T_t <<= 1
            t >>= 1
        return m( r )  
    def __str__(self):
        s = ''
        t = self.__c_s
        while ( t ):
            if( t & 1 ):
                s = "1" + s
            else:
                s = "0" + s
            t >>= 1
        return s
starttime = time.time()
i=0
while (i<100000):
    i+=1
    a = m(random.randint(0,255))
    b = m(random.randint(0,255))
    a*b
    #print a,'\t\t',b,'\t\t',a*b
print time.time() - starttime

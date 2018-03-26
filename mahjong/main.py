import random
import define
def init():
    #for i in define.pai:
    #    print(i)
    random.shuffle(define.pai)
    #print('===random===')
    #for i in define.pai:
    #    print(i)
    

def app():
    init()
    A = define.player('un')
    C = define.player('deux')
    B = define.player('trois')
    D = define.player('quatre')
    j = 0
    for i in range(4):
        A.hand += define.pai[j:j+4]
        j +=4
        B.hand += (define.pai[j:j+4])
        j +=4
        C.hand += (define.pai[j:j+4])
        j +=4
        D.hand += (define.pai[j:j+4])
        j +=4
    for i in A.hand:
        print(i)
        
        
if __name__=='__main__':
    app()
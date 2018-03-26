#encoding: utf-8
soupai = ('manzu', 'pinzu', 'souzu')
routoupai = (1,9)
tsuhai = ('sangen', 'kazahai')
yaocyupai = tsuhai + routoupai
fon = ('東','南','西','北')
gen = ('紅中','發財','白板')
suu = ('一','二','三','四','伍','六','七','八','九')
class majan:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.id = 0
        self.state = 0
        self.dora = 0
        self.owner = 0
    def __str__(self):
        return self.name + "  " +str(self.index)
    
    def resetDora(self):
        self.dora = 0
    
    def addDora(self):
        self.dora +=1
    
    def setState(self, state):
        self.state = state

class manzu(majan):# 萬子
    pass

class pinzu(majan):# 筒子
    pass

class souzu(majan):# 索子
    pass

class sangen(majan):#三元
    pass
    
class kazahai(majan):#四風
    pass
    
class player:
    _counter = 0
    def __init__(self, name = ''):
        player._counter += 1
        self.id = player._counter
        self.name = name
        self.hand = []
    def sort(self):
        pass
pai = []
for i in range(9):
    for j in range(4):
        pai.append(manzu(suu[i]+'萬',i+1))
        pai.append(manzu(suu[i]+'筒',i+1))
        pai.append(manzu(suu[i]+'餅',i+1))

for i in range(4):
    for j in range(4):
        pai.append(manzu(fon[i]+'風',i+1))

for i in range(3):
    for j in range(4):
        pai.append(manzu(gen[i],i+1))
#print(pai)
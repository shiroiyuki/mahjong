# -*- coding: utf-8 -*-
class calculator(object):

    @staticmethod
    def str9_to_array34(man=[], pin=[], sou=[], honor=[]):
        '''
            conver origin hand model to 34 array
        '''
        tiles = []
        for i in range(len(man)):
            tiles.append(int(man[i]) - 1)
        for i in range(len(pin)):
            tiles.append(int(pin[i]) + 8)
        for i in range(len(sou)):
            tiles.append(int(sou[i]) + 17)
        for i in range(len(honor)):
            tiles.append(int(honor[i]) + 26)
        return tiles

    @staticmethod
    def agari(tiles, res={}):
        '''
        pair:將眼
        tri :刻子
        seq :順子
        '''
        data = []
        size = len(tiles)

        if not res:
            res['pair'] = 0
            res['tri'] = 0
            res['seq'] = 0

        if not res['pair']:
            for i in range(size):
                if not data:
                    data.append(tiles[i])
                elif tiles[i] == data[0]:
                    res['pair'] = 1
                    if calculator().agari(tiles[:i-1] + tiles[i+1:], res):
                        return True
                    else: 
                        res['pair'] = 0
                        data = []
                else:
                    data[0] = tiles[i]

        def fetch_meld(tiles, offset):
            size = len(tiles)
            head = None
            mid  = None
            tail = None
            meld = None # 0:nothing, 1:seq, 2: tri

            if size == 0:
                return True
            for i in range(size):
                if tiles[i] < offset:
                    if  None == head:
                        head = i
                        meld = 0
                        continue

                    if tiles[i] == tiles[head] + 1 and None == mid:
                        meld = 1
                        mid  = i
                        continue
                    elif tiles[i] == tiles[head] and None == mid:
                        meld = 2
                        mid  = i
                        continue
                    else:
                        pass

                    if  head != None and mid != None:
                        if 1 == meld:
                            if tiles[i] == tiles[mid] + 1:
                                tail = i
                                tiles.pop(tail)
                                tiles.pop(mid)
                                tiles.pop(head)
                                return fetch_meld(tiles, offset)
                        
                        if 2 == meld:
                            if tiles[i] == tiles[mid]:
                                tail = i
                                tiles.pop(tail)
                                tiles.pop(mid)
                                tiles.pop(head)
                                return fetch_meld(tiles, offset)
                elif offset < 27:
                    return fetch_meld(tiles, offset + 9)
                elif offset == 27:
                    return fetch_meld(tiles, offset + 7)
                else:
                    return False
            return False
        return fetch_meld(tiles, 9)



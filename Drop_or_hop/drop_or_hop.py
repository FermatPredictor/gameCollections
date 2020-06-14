# -*- coding: utf-8 -*-
"""
規則:
在一個n*m的棋盤上遊玩，棋子只有單色
初始盤面可以任意擺，玩nim game。
目前有兩種規則:
(1) drop or hop:
每次輪到己方時，可以選擇一個棋子，往右下方向k格跳躍，
或在任意格子上無中生有放一個棋子。
(2) breed or hop:
每次輪到己方時，可以選擇一個棋子，往右下方向k格跳躍，
或往上、下、左、右四個方向繁殖，
無法移動者敗

<目前成果> : 完解1D棋盤k=1時的nim value. 
找到一個計分公式，盤面分數值即 = 盤面nim value值
"""

import time

# 設計成單例，因為只會有一張表格
class generalNimTable(): 
    __instance = None
    __init_flag = False

    def __new__(cls, v):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self, tableSz):
        if not self.__init_flag:
            self.Table = [-1]*tableSz
            self.__init_flag = True
    

"""
此遊戲的盤面號碼與盤面的對應關係:
假設 盤面號碼 = 110100 (二進位表示)、height=2、width=3
則盤面為號碼從最右邊的位數依序填至棋盤上，
即 board = [0,0,1,
            0,1,1]

此類別設計成單例，避免因創建太多棋盤造成巨大開銷

<移動棋步>
move是一組4個數的陣列[x,y,rx,ry]，
繁殖棋步 以 [x, y, -1, -1]表示
跳躍棋步 以 [x,y,rx,ry]表示，從(rx,ry)跳至(x,y)
"""
class singleColorInfectionNim():
    
    __instance = None
    __init_flag = False

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self, height, width, ID = 1):
        if not self.__init_flag:
            self.height = height
            self.width = width
            self.table = generalNimTable(1<<(width*height))
            self.scores = self.score_arr() # 計分公式陣列
            self.pow2Table = [pow(2,i) for i in range(width*height)] #因為計算boardID會大量用到2的次方，先建表可以省時間
            self.__init_flag = True
        self.setBoard(ID)

    
    # 回傳自己這個board的盤面號碼
    def boardID(self)-> int:
        return sum(e * self.pow2Table[i] for i, e in enumerate(self.board))
    
    # 根據ID設定self.board
    def setBoard(self, ID)->None:
        self.board = [(ID >> i)&1 for i in range(self.width*self.height)]
        
    """
    <重要>
    函數功能: 回傳當前盤面的合法棋步
    規則主要寫在這邊，可以在此改許多變形的規則。
    """
    def nextMoves(self)-> list:
        moves = []
        
        # 繁殖棋步
        for x in range(self.width):
            for y in range(self.height):
                if self.at(x,y)==0:# and (self.at(x+1,y)==1 or self.at(x-1,y)==1 or self.at(x,y+1)==1 or self.at(x,y-1)==1):
                    moves.append((x,y,-1,-1))
        
        # 跳躍棋步
        for rx in range(self.width):
            for ry in range(self.height):
                if self.at(rx,ry)==1:
                    for dx, dy in [(1,0), (0,1)]:
                        if self.at(rx+dx, ry+dy)==0:
                            moves.append((rx+dx, ry+dy,rx,ry))
                            
        return moves
    
    # 回傳經過移動後會到達的盤面ID
    def move(self, gMove):
        
        if not (gMove[2]==-1 and gMove[3]==-1):
            self.set_value(gMove[2], gMove[3], 0)
        self.set_value(gMove[0], gMove[1], 1)   
        
        ans = self.boardID()
        
        # 還原棋步
        if not (gMove[2]==-1 and gMove[3]==-1):
            self.set_value(gMove[2], gMove[3], 1)
        self.set_value(gMove[0], gMove[1], 0)   
        return ans
    
    #計算當前盤面的分數值(by 計分array，計算空格的分數)
    # 例子:board = [0,0,1,
    #              0,1,1]
    #     計分陣列 = [1,-1,1,
    #               -1,1,-1]
    # 分數 = 1-1-1=-1
    def calculatescore(self):
        return sum((1-a)*b for a,b in zip(self.board, self.scores))
    
    
    """
    函數功能: 根據自身棋盤大小產生計分array,
    當前規則為[1,-1,1,-1,1,-1,1,-1,....
             -1,1,-1,1,-1,1,-1,+1,...
             1,-1,1,-1,...]循環
    目標是猜計分array使得能夠把勝、負盤面分開，
    1*n棋盤有成功找到計分公式，
    但對於2*n棋盤卻一直猜不中，
    可能2*n棋盤沒有簡單加法公式
    """
    def score_arr(self):
        result = list()
        mode = [1, -1, 1, -1]
        for i in range(self.height):
            result.extend(mode*(self.width // 4)+ mode[:self.width%4])
            mode = list(map(lambda x:-x, mode))
        return result
    
    #設定棋盤座標(x,y)的值，如果超界就報錯
    def set_value(self, x, y, val):
        if 0 <= x< self.width and 0<= y< self.height:
            self.board[x + y * self.width] = val
        else:
            raise RuntimeError('set value out of index')
            
    
    #回傳棋盤座標(x,y)的值，如果超界就回傳-1
    def at(self, x, y):
        return self.board[x + y * self.width] if 0 <= x< self.width and 0<= y< self.height else -1
     
    # 回傳當前盤面可以到達的所有盤面ID
    def nextStates(self)-> list:
        return [self.move(m) for m in self.nextMoves()]
    
    # 找出最小不出現在數字集合nums中的非負整數
    # 例如: mex([0,1])=2
    # mex([0,2,3])=1
    # mex([])=0
    # mex([1,2,3])=0
    def mex(self, nums):
        return min(filter(lambda n: n not in nums, range(len(nums)+1)))
    
    """
    函數功能:
    遞迴計算盤面的nim value
    """
    def nimValue(self)-> int:
        ID = self.boardID() #記住原本的棋盤ID，不然等一下棋盤會修改
        if self.table.Table[ID]!=-1:
            return self.table.Table[ID]
        board_nvs=[]
        for s in self.nextStates():
            # 如果能查表就直接查，省時間
            if self.table.Table[s]!=-1:
                board_nvs.append(self.table.Table[s])
            else:
                self.setBoard(s)
                board_nvs.append(self.nimValue())
        nv = self.mex(board_nvs)
        self.table.Table[ID] = nv
        return nv 


class nimSolver():
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.size =  height*width
        self.game = singleColorInfectionNim(height, width, 1)
        
        # nim值建表
        start = time.time()
        for i in reversed(range(1,pow(2,width*height))):
            self.game.setBoard(i)
            self.game.nimValue()
        end = time.time()
        print(f"建表時間: {end - start:.2f}")
        
    """
    函數功能: 驗證盤面勝負可否用一個簡單計分公式來計算，
    目前已知繁殖可在任意格子上繁殖，
    跳只能往右方或下方跳一格的情況下，公式非常漂亮
    """
    def show(self):
        start = time.time()
        D = {0:set(), 1: set()} #記錄輸盤面和贏盤面各有哪些分數
        Nim_D = {} #記錄每個nim值有哪些分數
        print("目前計分公式: ", self.game.scores)
        for i in reversed(range(1,pow(2,self.width*self.height))):
            nim, score =  self.query_nimVal(i), self.query_score(i)
            D[nim!=0].add(self.query_score(i))
            if nim not in Nim_D:
                Nim_D[nim] = {score}
            else:
                Nim_D[nim].add(score)

        print("輪、贏盤面對應的分數:",D) #利用這個字典檢查計分公式能否區分贏的盤面及輸的盤面
        print("每個nim值對應的分數:",Nim_D) #利用這個字典檢查計分公式能否區分不同的nim值
        end = time.time()
        print(f"計算時間: {end - start:.2f}")
        
        
    # 給你一些編號，表示哪些格子是空的，
    # 計算該棋盤的ID
    def makeID(self, emptyGirds):
        ID = (1 << self.size)-1
        for e in set(emptyGirds):
            ID ^= (1<<e)
        return ID
    
    # 給定一個盤面ID，詢問該盤面的nim value
    def query_nimVal(self, ID):
        return self.game.table.Table[ID]
    
    # 給定一個盤面ID，詢問該盤面的list表示
    def query_board(self, ID):
        return [(ID >> i)&1 for i in range(self.width*self.height)]
    
    # 給定一個盤面ID，並詢問該盤面的分數
    def query_score(self, ID):
        self.game.setBoard(ID)
        return self.game.calculatescore()
            
"""
debug資訊: 
在繁殖可以選擇一個棋子往相鄰方向繁殖，
跳可以往右、下2格、正右下方1格的規則下，
計算得到2*2棋盤的nim value Table 值 = [-1, 0, 1, 3, 1, 3, 0, 2, 1, 0, 0, 1, 0, 1, 1, 0]
後面的版本需維持這個一致性，否則就是有程式寫錯了
"""
solver = nimSolver(2,2)
solver.show()

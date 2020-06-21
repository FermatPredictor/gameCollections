"""
經典問題: 馬踏棋盤。
騎士要不重複的走過西洋棋盤上的64個格子。
這邊採用優先走邊、角的方法，
否則要搜到一組解的時間會爆炸。
"""
class HorseWalk:

    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.board = [[0]*c for i in range(r)] #二維列表表示一個西洋棋的棋盤
        self.dirs = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)] # 馬步的八個方向
        self.find = False #全域變數，當find=True時停止搜索

    # 判斷一個座標是否可走
    def valid(self, pos):
        return 0<=pos[0]<=self.r-1 and 0<=pos[1]<=self.c-1 and self.board[pos[0]][pos[1]]==0
        
    # 計算一個格子座標的「邊緣分數」
    def value(self, pos):
        return min(pos[0],self.r-pos[0]-1)+min(pos[1],self.c-pos[1]-1)

    # 默認參數curstep表示現在第幾步
    def Move(self, pos, curstep=1):
        self.board[pos[0]][pos[1]]=curstep  #設定棋步
        if curstep==self.r * self.c: #一旦找到一組解，印出解答並設find=True
            for i in range(self.r):
                print(' '.join([f"{self.board[i][j]:2d}" for j in range(self.c)]))
            self.find = True 
        else:
            #nextPos是下一步可以走的座標位置，依「邊緣分數」排序
            nextPos = [[pos[0]+d[0], pos[1]+d[1]] for d in self.dirs] 
            nextPos = sorted(filter(lambda x: self.valid(x), nextPos), key= lambda x: self.value(x))
            for p in nextPos: #檢查下一步我可以走的八個方向
                if not self.find:
                    self.Move(p, curstep+1)      
        self.board[pos[0]][pos[1]]=0 #撤銷棋步


iniPos = (0,0) #初始座標
solver = HorseWalk(6,6)
solver.Move(iniPos)

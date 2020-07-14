import random

# 寫黑白棋遊戲的基本邏輯，棋子共'X','O'兩種
class Reversi():
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.board = [[' ']*self.height for i in range(self.width)]
    
    # 初始化棋盤
    def iniBoard(self):
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j]=' '
        W, H = self.width//2 , self.height//2
        self.board[W-1][H-1]='X'
        self.board[W-1][H]='O'
        self.board[W][H-1]='O'
        self.board[W][H]='X'
        
    def drawBoard(self, hints = None) -> None:
        HLINE =  ' ' * 3 + '+---' * self.width  + '+'
        VLINE = (' ' * 3 +'|') *  (self.width +1)
        title = '     1'
        for i in range(1,self.width):
            title += ' ' * 3 +str(i+1)
        print(title)
        print(HLINE)
        for y in range(self.height):
            print(VLINE)
            print(y+1, end='  ')
            for x in range(self.width):
                if hints and [x,y] in hints:
                    print(f'| *', end=' ')
                else:
                    print(f'| {self.board[x][y]}', end=' ')
            print('|')
            print(VLINE)
            print(HLINE)
    
    def isOnBoard(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    #檢查tile放在某個座標是否為合法棋步，如果是則回傳被翻轉的棋子
    def isValidMove(self, tile, xstart, ystart):
        if not self.isOnBoard(xstart, ystart) or self.board[xstart][ystart]!=' ':
            return []
        self.board[xstart][ystart] = tile # 暫時放置棋子
        otherTile = 'O'  if tile == 'X' else 'X'
        tilesToFlip = [] # 合法棋步
        dirs = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]] # 定義八個方向
        for xdir, ydir in dirs:
            x, y = xstart+xdir, ystart+ydir
            while self.isOnBoard(x, y) and self.board[x][y] == otherTile:
                x += xdir
                y += ydir
                # 夾到對手的棋子了，回頭記錄被翻轉的對手棋子
                if self.isOnBoard(x, y) and self.board[x][y] == tile:
                    while True:
                        x -= xdir
                        y -= ydir
                        if x == xstart and y == ystart:
                            break
                        tilesToFlip.append([x, y])
                        
        self.board[xstart][ystart] = ' ' # 重設為空白
        return tilesToFlip

    # 若將tile放在xstart, ystart是合法行動，放置棋子
    # 回傳被翻轉的棋子(用來電腦算棋時可以把棋子翻回來)
    def makeMove(self, tile, xstart, ystart):
        tilesToFlip = self.isValidMove(tile, xstart, ystart)
        if tilesToFlip:
            self.board[xstart][ystart] = tile
            for x, y in tilesToFlip:
                self.board[x][y] = tile
        return tilesToFlip

    # 回傳現在盤面輪到tile走的所有合法棋步
    def getValidMoves(self, tile):
        return [[x, y] for x in range(self.width) for y in range(self.height) if self.isValidMove(tile, x, y)]
    
    # 計算當前比分
    def getScoreOfBoard(self)-> dict:
        scores = {'X':0, 'O':0}
        for x in range(self.width):
            for y in range(self.height):
                tile = self.board[x][y]
                if tile in scores:
                    scores[tile] += 1
        return scores

# 電腦ai下棋的邏輯
class ReversiAI(Reversi):
    def __init__(self, board, height, width):
        super().__init__(height, width)
        self.board = board

    def isOnCorner(self, x, y):
        return x in {0, self.width-1} and y in {0, self.height-1}
 
    # 給定盤面board，回傳電腦的選擇
    def getComputerMove(self, computerTile):
        possibleMoves = self.getValidMoves(computerTile)
        random.shuffle(possibleMoves) # 隨機性
        
        # 若能占角為優先
        for x, y in possibleMoves:
            if self.isOnCorner(x, y):
                return [x, y]
            
        # 找能夠吃子最多的棋步
        bestScore, bestMove = -1, None
        for x, y in possibleMoves:
            flips = self.makeMove(computerTile, x, y)
            score = self.getScoreOfBoard()[computerTile]
            if score > bestScore:
                bestScore, bestMove = score, [x, y]
            # 還原棋盤
            self.board[x][y] = ' '
            otherTile = 'O'  if computerTile == 'X' else 'X'
            for x, y in flips:
                self.board[x][y] = otherTile
        return bestMove

# 電腦ai下棋的邏輯
class alpha_beta_AI(Reversi):
    def __init__(self, board, height, width):
        super().__init__(height, width)
        self.board = board

    def isOnCorner(self, x, y):
        return x in {0, self.width-1} and y in {0, self.height-1}
    
    # 'X'愈多愈高分
    def valuef(self):
        scores = {'X':0, 'O':0}
        for x in range(self.width):
            for y in range(self.height):
                tile = self.board[x][y]
                #角落權重增加
                if tile in scores:
                    scores[tile] += 5 if self.isOnCorner(x,y) else 1
        return scores['X']-scores['O']

    def changeColor(self, tile):
        return 'O' if tile == 'X' else 'X'

    def ABmaxNode(self, alpha, beta, height, tile):
        bestop, bestScore = [-1,-1], alpha
        if height<=0:
            bestScore = self.valuef()
            return bestop, bestScore
	    #無人可走就pass
        elif not self.getValidMoves(tile):
            bestop, bestScore = self.ABminNode(alpha,beta,height-1,self.changeColor(tile))
            return  [-1,-1], bestScore
        m = alpha
        moves = self.getValidMoves(tile)
        random.shuffle(moves)
        for move in moves:
            
            flips = self.makeMove(tile, move[0], move[1])
            bestmove, score = self.ABminNode(m,beta,height-1,self.changeColor(tile))

            # 還原棋盤
            self.board[move[0]][move[1]] = ' '
            otherTile = 'O'  if tile == 'X' else 'X'
            for x, y in flips:
                self.board[x][y] = otherTile

            if score > m:
                m=score
                bestop = move[:]
                bestScore = m
            if m >= beta:
                return bestop, bestScore
            return bestop, bestScore
    
    def ABminNode(self, alpha, beta, height, tile):
        bestop, bestScore = [-1,-1], beta
        if height<=0:
            bestScore = self.valuef();
            return bestop, bestScore;
        #無人可走就pass
        elif not self.getValidMoves(tile):
            bestop, bestScore = self.ABmaxNode(alpha,beta,height-1,self.changeColor(tile))
            return [-1,-1], bestScore
        m = beta
        moves = self.getValidMoves(tile)
        random.shuffle(moves)
        for move in moves:
            
            flips = self.makeMove(tile, move[0], move[1]);
            bestmove, score = self.ABmaxNode(alpha,m,height-1,self.changeColor(tile))

            # 還原棋盤
            self.board[move[0]][move[1]] = ' '
            otherTile = 'O'  if tile == 'X' else 'X'
            for x, y in flips:
                self.board[x][y] = otherTile

            if score < m:
                m=score
                bestop = move[:]
                bestScore = m
            if m <= alpha:
                return bestop, bestScore
        return bestop, bestScore

    # 給定盤面board，回傳電腦的選擇
    def getComputerMove(self, computerTile):
        if computerTile == 'X':
            move, score = self.ABmaxNode(-99,99,3,computerTile)
        else:
            move, score = self.ABminNode(-99,99,3,computerTile)
        return move

# 讓不同ai互打多打，看勝率
class simulateGame(Reversi):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.turn = 'player'
        self.ai = ReversiAI(self.board,self.height, self.width)
        self.ai_two = alpha_beta_AI(self.board,self.height, self.width)

    # 顯示目前比分
    def showPoints(self, playerTile, computerTile):
        scores = self.getScoreOfBoard()
        print(f'You have {scores[playerTile]} points. The computer has {scores[computerTile]} points.')

    def gameloop(self):
        print('Welcome to Reversi!')

        xwins, owins, ties = 0, 0, 0
        numGames = int(input('Enter number of games to run: '))

        for i in range(numGames):
            print(f'Game #{i}:', end=' ')
            # 初始化棋盤，然後隨機決定先、後手
            self.iniBoard()
            self.turn = 'X' if random.randint(0,1)==0 else 'O'
                
            while True:
                xMoves = self.getValidMoves('X')
                oMoves = self.getValidMoves('O')

                # 若無人可行動，結束遊戲
                if not xMoves and not oMoves:
                    break

                if self.turn == 'X' and xMoves:
                    x, y = self.ai.getComputerMove('X')
                elif self.turn == 'O' and oMoves:
                    x, y = self.ai_two.getComputerMove('O')
                #self.drawBoard()
                #input('按enter看電腦的下一步')
                self.makeMove(self.turn, x, y)
                self.turn = 'O' if self.turn == 'X' else 'X'
            
            # 顯示最後結果
            scores = self.getScoreOfBoard()
            print(f"X scored {scores['X']} points. O scored {scores['O']} points.")
            if scores['X'] > scores['O']:
                xwins+=1
            elif scores['X'] < scores['O']:
                owins += 1
            else:
                ties+=1
                
        xpercent = round(((xwins / numGames) * 100), 2)
        opercent = round(((owins / numGames) * 100), 2)
        tiepercent = round(((ties / numGames) * 100), 2)
        print(f'X wins {xwins} games ({xpercent}%), O wins {owins} games ({opercent}%), ties for {ties} games ({tiepercent}%) of {numGames} games total.')

reversi = simulateGame(8,8)
reversi.gameloop()

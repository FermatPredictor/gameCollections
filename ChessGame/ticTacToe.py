import random
import sys

# 寫井字遊戲的基本邏輯，棋子共'X','O'兩種
class TicTacToe():
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.board = [[' ']*self.height for i in range(self.width)]
    
    # 初始化棋盤
    def iniBoard(self):
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j]=' '
        
        
    def drawBoard(self) -> None:
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
                print(f'| {self.board[x][y]}', end=' ')
            print('|')
            print(VLINE)
            print(HLINE)
    
    def isOnBoard(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    #檢查tile放在某個座標是否為合法棋步
    def isValidMove(self, tile, x, y):
        return self.isOnBoard(x, y) and self.board[x][y]==' '
    
    # 回傳現在盤面輪到tile走的所有合法棋步
    def getValidMoves(self, tile):
        return [[x, y] for x in range(self.width) for y in range(self.height) if self.isValidMove(tile, x, y)]
        

# 電腦ai下棋的邏輯 (這邊我偷懶直接讓電腦選擇隨機棋步)
class TicTacToeAI(TicTacToe):
    def __init__(self, board, height, width):
        super().__init__(height, width)
        self.board = board   
 
    # 給定盤面board，回傳電腦的選擇
    def getComputerMove(self, computerTile):
        possibleMoves = self.getValidMoves(computerTile)
        random.shuffle(possibleMoves) # 隨機性
        return possibleMoves[0]
        


# 寫互動程式的邏輯
class Game(TicTacToe):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.turn = 'player'
        self.ai = TicTacToeAI(self.board,self.height, self.width)

    # 詢問玩家是否再玩一次
    def playAgain(self)-> bool:
        return input('你想再玩一次嗎?(輸入y或n)').lower().startswith('y')

    # 取得玩家的行動，回傳棋步[x, y](或'hints', 'quit'))
    def getPlayerMove(self, playerTile):
        DIGITS = [str(i) for i in range(1,10)]
        while True:
            move = input('請輸入棋步(先輸入x座標再輸入y座標)，例如11是左上角。(或輸入quit)').lower()
            if move in {'quit'}:
                return move
            if len(move) == 2 and move[0] in DIGITS and move[1] in DIGITS:
                x = int(move[0]) - 1
                y = int(move[1]) - 1
                if self.isValidMove(playerTile, x, y):
                    break
            print('非合法棋步，請再試一次')
        return [x, y]
    
    # 判斷一個盤面是否有人贏了
    def check_TicTacToe(self):
        rows = self.board
        cols = list(map(''.join, zip(*rows)))
        diags = list(map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)])))
        lines = rows + cols + diags

        if 'XXX' in lines:
            return 'X'  
        if 'OOO' in lines:
            return 'O' 
        return 'D'


    def gameloop(self):
        print("歡迎玩井字遊戲(玩家的棋子為'X')")

        while True:
            # 初始化棋盤
            self.iniBoard()
            playerTile, computerTile = ['X', 'O']
            print('玩家先手' if self.turn == 'player' else '電腦先手')
            
            while True:
                playerValidMoves = self.getValidMoves(playerTile)
                computerValidMoves = self.getValidMoves(computerTile)
                # 若無人可行動，結束遊戲
                if not playerValidMoves and not computerValidMoves or self.check_TicTacToe()!='D':
                    break

                if self.turn == 'player' and playerValidMoves:
                    self.drawBoard()
                    move = self.getPlayerMove(playerTile)
                    if move == 'quit':
                        print('Thanks for playing!')
                        sys.exit() # terminate the program
                    else:
                        self.board[move[0]][move[1]] = playerTile
                elif self.turn == 'computer' and computerValidMoves:
                    self.drawBoard()
                    input('按enter看電腦的下一步')
                    x, y = self.ai.getComputerMove(computerTile)
                    self.board[x][y] = computerTile
                self.turn = 'player' if self.turn=='computer' else 'computer'
                        
            # 顯示最後結果
            self.drawBoard()
            result = self.check_TicTacToe()
            if result=='X':
                print("恭喜你贏電腦了")
            elif result=='O':
                print("你輸了")
            else:
                print('平手')
                
            if not self.playAgain():
                break

reversi = Game(3,3)
reversi.gameloop()

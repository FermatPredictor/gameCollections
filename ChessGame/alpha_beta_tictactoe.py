import random
import unittest

# 寫井字遊戲的基本邏輯，棋子共'X','O'兩種
class TicTacToe():
    def __init__(self):
        self.board = [[' ']*3 for i in range(3)]
    
    # 初始化棋盤
    def iniBoard(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j]=' '
        
    # 視覺化的把井字棋棋盤畫出來    
    def drawBoard(self) -> None:
        HLINE =  ' ' * 3 + '+---' * 3  + '+'
        VLINE = (' ' * 3 +'|') *  (3 +1)
        title = '     0'
        for i in range(1,3):
            title += ' ' * 3 +str(i)
        print(title)
        print(HLINE)
        for y in range(3):
            print(VLINE)
            print(y, end='  ')
            for x in range(3):
                print(f'| {self.board[x][y]}', end=' ')
            print('|')
            print(VLINE)
            print(HLINE)
    
    def isOnBoard(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3

    #檢查tile放在某個座標是否為合法棋步
    def isValidMove(self, x, y):
        return self.isOnBoard(x, y) and self.board[x][y]==' '

    # 把棋子下在座標x, y的地方
    def makeMove(self, tile, x, y):
        if self.isValidMove(x, y):
            self.board[x][y]=tile
    
    # 回傳現在盤面輪到tile走的所有合法棋步
    def getValidMoves(self):
        return [[x, y] for x in range(3) for y in range(3) if self.isValidMove(x, y)]

    # 判斷一個盤面是否有人贏了
    def check_TicTacToe(self):
        rows = list(map(''.join,self.board))
        cols = list(map(''.join, zip(*rows)))
        diags = list(map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)])))
        lines = rows + cols + diags
    
        if 'XXX' in lines:
            return 'X'  
        if 'OOO' in lines:
            return 'O' 
        return 'D' # draw(和棋)


# 電腦ai下棋的邏輯
class TicTacToeAI(TicTacToe):
    def __init__(self, board):
        super().__init__()
        self.board = board
        
    def ending(self):
        return self.check_TicTacToe()!='D' or not self.getValidMoves() 
 
    # 'X'贏的話得分
    def valuef(self):
        winTile = self.check_TicTacToe()
        if winTile == 'X':
            return 100
        elif winTile == 'O':
            return -100
        return 0
    
    def depthScore(self, value, depth, isMaxPlayer):
        if depth == 0 or value == 0:
            return 0
        if value>0:
            return depth * 2
        else:
            return depth * -2

    def alphabeta(self, depth, alpha, beta, isMaxPlayer):
        if depth==0 or self.ending():
            value = self.valuef()
            return [-1,-1], value + self.depthScore(value, depth, isMaxPlayer)

        if isMaxPlayer: # 'X'的回合
            bestop = [-1,-1]
            moves = self.getValidMoves()
            random.shuffle(moves)
            for move in moves:

                self.makeMove('X', move[0], move[1])

                M, score = self.alphabeta(depth-1, alpha,beta,False)
                
                # 還原棋盤
                self.board[move[0]][move[1]] = ' '
                
                if score> alpha:
                    bestop, alpha = move, score
                
                if beta <= alpha:
                    break
            return bestop, alpha
        
        else: # 'O'的回合
            bestop = [-1,-1]
            moves = self.getValidMoves()
            random.shuffle(moves)
            for move in moves:

                self.makeMove('O', move[0], move[1])
                
                M, score = self.alphabeta(depth-1, alpha,beta,True)
                
                # 還原棋盤
                self.board[move[0]][move[1]] = ' '

                if score< beta:
                    bestop, beta = move, score
                
                if beta <= alpha:
                    break
            return bestop, beta

    # 給定盤面board，回傳電腦的選擇
    def getComputerMove(self, computerTile):
        isMaxPlayer = (computerTile == 'X')
        move, score = self.alphabeta(8, -999,999, isMaxPlayer)
        return move

# 電腦ai下棋的邏輯 (這邊我偷懶直接讓電腦選擇隨機棋步)
class RandomAI(TicTacToe):
    def __init__(self, board):
        super().__init__()
        self.board = board   
 
    # 給定盤面board，回傳電腦的選擇
    def getComputerMove(self, computerTile):
        possibleMoves = self.getValidMoves()
        random.shuffle(possibleMoves) # 隨機性
        return possibleMoves[0]

class Test(unittest.TestCase):
    
        
    def test_basic(self):
        game = TicTacToe()
        game.makeMove('X',0,0)
        game.makeMove('X',0,1)
        game.makeMove('O',1,1)
        game.makeMove('O',0,2)
        ai = TicTacToeAI(game.board)
        move = ai.getComputerMove('X')
        ai.drawBoard()
        self.assertEqual(move, [2,0]) 

    def test_fixDatas(self):
        game = TicTacToe()
        game.makeMove('O',2,0)
        game.makeMove('O',0,1)
        game.makeMove('X',1,1)
        game.makeMove('X',0,2)
        ai = TicTacToeAI(game.board)
        move = ai.getComputerMove('X')
        ai.drawBoard()
        self.assertIn(move, [[1,2],[2,2]])
    
    def test_early_win(self):
        game = TicTacToe()
        game.makeMove('O',0,0)
        game.makeMove('O',0,1)
        game.makeMove('X',1,1)
        game.makeMove('X',0,2)
        ai = TicTacToeAI(game.board)
        move = ai.getComputerMove('X')
        ai.drawBoard()
        self.assertEqual(move, [2,0])
        
    def test_late_lose(self):
        game = TicTacToe()
        game.makeMove('O',0,1)
        game.makeMove('X',1,1)
        game.makeMove('X',0,2)
        ai = TicTacToeAI(game.board)
        move = ai.getComputerMove('O')
        ai.drawBoard()
        self.assertEqual(move, [2,0])
    
    def test_early_win_two(self):
        game = TicTacToe()
        game.makeMove('X',0,0)
        game.makeMove('X',0,1)
        game.makeMove('O',1,1)
        game.makeMove('O',0,2)
        ai = TicTacToeAI(game.board)
        move = ai.getComputerMove('O')
        ai.drawBoard()
        self.assertEqual(move, [2,0])
     
    def test_late_lose_two(self):
        game = TicTacToe()
        game.makeMove('X',0,1)
        game.makeMove('O',1,1)
        game.makeMove('O',0,2)
        ai = TicTacToeAI(game.board)
        move = ai.getComputerMove('X')
        ai.drawBoard()
        self.assertEqual(move, [2,0])
        
        
    def test_ending_case(self):
        game = TicTacToe()
        game.makeMove('X',0,0)
        game.makeMove('X',2,0)
        game.makeMove('X',1,2)
        game.makeMove('O',1,1)
        game.makeMove('O',1,0)
        game.makeMove('O',2,1)
        game.makeMove('O',0,2)
        ai = TicTacToeAI(game.board)
        move = ai.getComputerMove('X')
        ai.drawBoard()
        self.assertEqual(move, [0,1])
        
    def test_corner(self):
        game = TicTacToe()
        game.makeMove('X',0,0)
        ai = TicTacToeAI(game.board)
        move = ai.getComputerMove('O')
        ai.drawBoard()
        self.assertEqual(move, [1,1])
        
    def test_X_randomPlay(self):
        for i in range(10):
            game = TicTacToe()
            game.makeMove('O',random.randint(0,2),random.randint(0,2))
            ai = TicTacToeAI(game.board)
            random_ai = RandomAI(game.board)
            turn = 'X'
           # print(f"第{i}局遊戲:")
            while True:
                
                # 若無人可行動或有人贏了，結束遊戲
                if not game.getValidMoves() or game.check_TicTacToe()!='D':
                    break

                if turn == 'X':
                    x, y = ai.getComputerMove('X')
                elif turn == 'O':
                    x, y = random_ai.getComputerMove('O')
                
                #print(turn, x, y)
                game.makeMove(turn, x, y)
                #game.drawBoard()
                turn = 'O' if turn == 'X' else 'X'
             
            self.assertNotEqual(game.check_TicTacToe(), 'O')
            
    def test_O_randomPlay(self):
        for i in range(10):
            game = TicTacToe()
            game.makeMove('X',random.randint(0,2),random.randint(0,2))
            ai = TicTacToeAI(game.board)
            random_ai = RandomAI(game.board)
            turn = 'O'
            #print(f"第{i}局遊戲:")
            while True:
                
                # 若無人可行動或有人贏了，結束遊戲
                if not game.getValidMoves() or game.check_TicTacToe()!='D':
                    break

                if turn == 'O':
                    x, y = ai.getComputerMove('O')
                elif turn == 'X':
                    x, y = random_ai.getComputerMove('X')
                
                #print(turn, x, y)
                game.makeMove(turn, x, y)
                #game.drawBoard()
                turn = 'O' if turn == 'X' else 'X'
             
            self.assertNotEqual(game.check_TicTacToe(), 'X')
    
    # 雙方採用最佳策略一定和棋        
    def test_selfPlay(self):
        for i in range(10):
            game = TicTacToe()
            game.makeMove('X',random.randint(0,2),random.randint(0,2))
            ai = TicTacToeAI(game.board)
            turn = 'O'
            #print(f"第{i}局遊戲:")
            while True:
                
                # 若無人可行動或有人贏了，結束遊戲
                if not game.getValidMoves() or game.check_TicTacToe()!='D':
                    break

                if turn == 'X':
                    x, y = ai.getComputerMove('X')
                elif turn == 'O':
                    x, y = ai.getComputerMove('O')
                
                #print(turn, x, y)
                game.makeMove(turn, x, y)
                #game.drawBoard()
                turn = 'O' if turn == 'X' else 'X'
             
            self.assertEqual(game.check_TicTacToe(), 'D')


unittest.main()

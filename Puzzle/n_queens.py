# 視覺化的把一組答案印出來
def output(WeiZhi, num):
    print(f"第{num}種方案(■表示皇后):")
    sz = len(WeiZhi)
    HLINE =  ' ' * 3 + '+---' * sz + '+'
    VLINE = (' ' * 3 +'|') *  (sz+1)
    title = '     1'
    for i in range(1,sz):
        title += ' ' * 3 +str(i+1)
    print(title)
    print(HLINE)
    for y in range(sz):
        print(VLINE)
        print(y+1, end='  ')
        for x in range(sz):
            print('| ■' if WeiZhi[y]==x else '| 0', end=' ')
        print('|')
        print(VLINE)
        print(HLINE)
    
def conflict(state, nextX):    
    nextY = len(state)
    return any(abs(state[i] - nextX) in (0, nextY - i) for i in range(nextY))

def queens(n, state = ()): # 初始默認state是空棋盤
    if len(state) == n: 
        return [()]
    ans = []
    for pos in range(n):
        if not conflict(state, pos):
            ans += [(pos,)+ result for result in queens(n, state + (pos,))]
    return ans

queenNUM = 4
for i, q in enumerate(queens(queenNUM)):
    output(q, i+1)

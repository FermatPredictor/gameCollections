from itertools import combinations
import time

# Operators 
OP_ADD = 1  # Addition 
OP_SUB = 2  # Subtraction 
OP_MUL = 3  # Multiplication 
OP_DIV = 4  # Divition
OP_INVDIV = 5

ops=[OP_ADD,OP_SUB,OP_MUL,OP_DIV,OP_INVDIV]

def opFunc(a,b,op):
    #排除除以0的例外
    if (b==0 and op==OP_DIV) or (a==0 and op==OP_INVDIV):
        return None
    if op==OP_ADD: return a+b
    if op==OP_SUB: return abs(a-b)
    if op==OP_MUL: return a*b
    if op==OP_DIV: return a/b
    if op==OP_INVDIV: return b/a
    
def strOpFunc(list1,list2,op):
    if op==OP_ADD: return "("+str(list1[0])+'+'+str(list2[0])+ ")"
    if op==OP_SUB: 
        if list1[1]>list2[1]:
            return "("+str(list1[0])+'-'+str(list2[0])+")" 
        return "("+str(list2[0])+'-'+str(list1[0])+")" 
    if op==OP_MUL: return "("+str(list1[0])+'*'+str(list2[0])+")" 
    if op==OP_DIV: return "("+str(list1[0])+'/'+str(list2[0])+")" 
    if op==OP_INVDIV: return "("+str(list2[0])+'/'+str(list1[0])+")"

# nums 同時記錄字串的運算表達式與計算結果
def makeN(nums, targetNum=24):
    if len(nums)==1 and abs(nums[0][1]-targetNum)<=1e-6:
        return nums
    res = []
    for t1,t2 in combinations(nums,2):
        for op in ops:
            L = nums[:]
            L.remove(t1)
            L.remove(t2)
            if opFunc(t1[1],t2[1],op):
                L.append((strOpFunc(t1,t2,op), opFunc(t1[1],t2[1],op)))
                for expr in makeN(L, targetNum):
                    res.append(expr)
            if res: #若找到一組解就回傳答案，若把這兩行註解掉可找所有解
                return res
    return res
                
def makeNSolver(nums, targetNum=24):
    return makeN([(str(x),int(x)) for x in nums], targetNum)

if __name__ == '__main__':
    nums=[5,8,8,9]
    targetNum=24
    tStart = time.time()#計時開始
    print(makeNSolver(nums, targetNum))
    tEnd = time.time()#計時結束
    print(tEnd - tStart)

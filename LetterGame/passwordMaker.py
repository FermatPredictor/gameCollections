import random
import string

wordList = 'word.txt' # 單字庫
with open(wordList) as fileObj:
    words = fileObj.read().split()

print('Welcome to Password Maker!')

while True:
    L = []
    for _ in range(5):
        S = random.sample(words, 3)
        number =random.randrange(100)
        special_char = random.choice(string.punctuation)
        password = ''.join(S)+ str(number) + special_char
        L.append(password)
    print(L)
        
    if input("Would you like another password? Type y or n: ")!='y':
        break

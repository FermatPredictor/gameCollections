import random

wordList = 'word.txt' # 單字庫
with open(wordList) as fileObj:
    words = fileObj.read().split()


heart_symbol=u'\u2764' #紅心的utf-8碼 

# 更新clue這個單字，順便回傳單字是否猜完了
def update_clue(guessed_letter, secret_word, clue):
    for i, e in enumerate(secret_word):
        if guessed_letter == e:
            clue[i] = guessed_letter
    return '?' not in clue

while True:

    lives=9
    secret_word = random.choice(words)
    clue=list("?" * len(secret_word))
    guessed_word_correctly = False 

    while lives>0:
        print(clue)
        print('Lives left: '+heart_symbol *lives)
        
        guess = input('Guess a letter or the whole word:' ).strip()
          
        if guess == secret_word:
            guessed_word_correctly=True
            break
        
        if guess in clue:
            print('你已經猜過這個字了，換其它字猜吧~')
        elif guess in secret_word:
            if update_clue(guess,secret_word,clue):
                guessed_word_correctly=True
                break                
        else:
            print("Incorrect. You lose a life")
            lives = lives - 1
    
    if guessed_word_correctly:
        print('You won! The secret word was '+secret_word)
    else:
        print('You lost! The secret word was '+secret_word)

    s = input("Do you want to play again? (enter y or n)").lower()
    if s!='y':
        break

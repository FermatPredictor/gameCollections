import re
from collections import Counter

# 找純字母，避免把數字、底線一起讀進來
def words(text):
    return re.findall(r'[a-z]+', text.lower())

word_count = Counter(words(open('big.txt').read()))
N = sum(word_count.values())

# 計算單個單字出現機率
def P(word): 
    return word_count[word] / N # float

all_word = [word for word in word_count if len(word)>=2 and P(word) > 10 ** (-5)]
all_word.sort()
common_word =[word for word in word_count if len(word)>=2 and P(word) > 10 ** (-4)]
common_word.sort(key = P, reverse = True)

with open('word.txt', 'w') as fileObj:
    for w in all_word:
        fileObj.write(w+'\n')

with open('common_word.txt', 'w') as fileObj:
    for w in common_word:
        fileObj.write(w+'\n')

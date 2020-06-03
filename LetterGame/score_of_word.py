"""
如果26個英文字母 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
分別等於
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 

那麼 ~~~~~
Knowledge（知識）
K + N + O +W + L + E + D +G +E
11 +14 +15 +23+12 + 5 + 4 +7 +5
 = 96%
 
Workhard （努力工作）
W + O + R + K + H + A + R + D 
23 +15 +18 +11 + 8 + 1 +18 + 4
= 98%
 
也就是說知識和努力工作對我們人生的影響可以達到 96％ 和 98％
 
Luck（好運）
L + U + C+ K
12+21 + 3+11
= 47%
 
Love（愛情）
L + O+ V + E
12 +15+ 22+ 5
= 54%
 
看來，這些我們通常認為重要的東西卻並沒起到最重要的作用。
 
那麼，什麼可以決定我們 100％ 的人生呢？
 
是Money（金錢）嗎?
M + O + N + E + Y
13 +15 +14 + 5 + 25
= 72%
看來也不是
 
是Leadership（領導能力）嗎? 
L+ E+ A+ D+ E+ R+ S+ H+ I+ P
12+ 5+ 1+ 4+ 5+18+19+ 8+ 9+16
= 89%
還不是
 
金錢，權力也不能完全決定我們的生活。那是什麼呢？
其實，真正能使我們生活圓滿的東西就在我們自己身上！
 
ATTITUDE（心態）
A+ T + T + I+ T + U + D+ E
1+ 20+ 20+ 9+ 20+ 21+ 4+ 5
= 100%
 
我們對待人生的態度才能夠 100％ 的影響我們的生活，
或者說能夠使我們的生活達到 100% 的圓滿！
 
用什麼樣的態度去看待人生，就會得到什麼樣的人生！

(所以這隻程式便是利用單字庫計算哪些單字可以是100%)
"""

wordList = 'word.txt' # 單字庫
with open(wordList) as fileObj:
    words = fileObj.read().split()
    
def score_of_word(s):
    return sum(map(lambda c:ord(c)-ord('a')+1, s.lower()))
    
for word in words:
    if score_of_word(word)==100:
        print(word)

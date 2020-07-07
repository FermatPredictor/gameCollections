# gameCollections

目標: 收集自己寫過的遊戲程式

## 英文單字遊戲
首先，先在網路上收集一篇很長的英文文章，隨意找，把它存成文字檔。(範例: [big.txt](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/big.txt))<br>
然後寫一支程式，將裡面的英文單字截取出來，可以設定合理的機率值使得出現的單字不要太過罕見<br>
截取英文文章單字的程式: [selectWord](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/selectWord.py)
(目前設定是出現比率>1/10000算常用字; 出現比率>1/100000算可收集字，條件放很鬆)<br>
截取完英文單字後的文件: [common_word.txt](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/common_word.txt), [word.txt](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/word.txt)

| 簡介 | 主程式 | 需要的檔案|
| --- | --- | --- |
|猜英文單字的小遊戲|[nineLive](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/nineLive.py)|[word.txt](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/word.txt) (如果有自己的單字庫，亦可換成自己的)|
|利用單字庫的單字隨機生成密碼|[passwordMaker](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/passwordMaker.py)|[word.txt](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/word.txt) (如果有自己的單字庫，亦可換成自己的)|
|如果a-z對應到1-26，哪些單字的分數為100|[score_of_word](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/score_of_word.py)|[word.txt](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/word.txt) (如果有自己的單字庫，亦可換成自己的)|


## Drop or hop
nim game的一種，在一個n\*m的棋盤上遊玩，棋子只有單色<br>
目前有兩種規則:<br>
(1) drop or hop:<br>
每次輪到己方時，可以選擇一個棋子，往右下方向k格跳躍，<br>
或在任意格子上無中生有放一個棋子。<br>
(2) breed or hop:<br>
每次輪到己方時，可以選擇一個棋子，往右下方向k格跳躍，<br>
或往上、下、左、右四個方向繁殖，<br>
無法移動者敗<br>
程式: [drop_or_hop](https://github.com/FermatPredictor/gameCollections/blob/master/Drop_or_hop/drop_or_hop.py)

## 單人解謎益智遊戲
| 簡介 | c++ | python |
| --- | --- | --- |
|n皇后問題，如何在西洋棋盤擺n個皇后而不會互相攻擊?|[Code](https://github.com/FermatPredictor/gameCollections/blob/master/Puzzle/n_queens.cpp)|[Code](https://github.com/FermatPredictor/gameCollections/blob/master/Puzzle/n_queens.py)|
|馬踏棋盤(又稱騎士漫步)|[Code](https://github.com/FermatPredictor/gameCollections/blob/master/HorseWalk/horsewalk.cpp)|[Code](https://github.com/FermatPredictor/gameCollections/blob/master/HorseWalk/horsewalk.py)|

## 下棋遊戲
| 簡介 | c++ | python |
| --- | --- | --- |
|黑白棋||[Code](https://github.com/FermatPredictor/gameCollections/blob/master/ChessGame/reversi.py)|

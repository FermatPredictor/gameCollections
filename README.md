# gameCollections

目標: 收集自己寫過的遊戲程式

## 英文單字遊戲
首先，先在網路上收集一篇很長的英文文章，隨意找，把它存成文字檔。(範例: [big.txt](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/big.txt))<br>
然後寫一支程式，將裡面的英文單字截取出來，可以設定合理的機率值使得出現的單字不要太過罕見<br>
截取英文文章單字的程式: [selectWord](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/selectWord.py)
(目前設定是出現比率>1/10000算常用字; 出現比率>1/100000算可收集字，條件放很鬆)

| 簡介 | 主程式 | 需要的檔案|
| --- | --- | --- |
|猜英文單字的小遊戲|[nineLive](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/nineLive.py)|[word.txt](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/word.txt) (如果有自己的單字庫，亦可換成自己的)|
|利用單字庫的單字隨機生成密碼|[passwordMaker](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/passwordMaker.py)|[word.txt](https://github.com/FermatPredictor/gameCollections/blob/master/LetterGame/word.txt) (如果有自己的單字庫，亦可換成自己的)|

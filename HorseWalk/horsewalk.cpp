#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class HorseWalk
{
private:
    vector<vector<int>> board;
    bool find; //全域變數，當find=True時停止搜索
    vector<vector<int>> dirs;

    // 判斷一個座標是否可走
    bool valid(vector<int> &pos){
        int R = board.size(), C= board[0].size();
        return 0<=pos[0] && pos[0]<R && 0<=pos[1] && pos[1] <C && board[pos[0]][pos[1]]==0;
    }

    // 計算一個格子座標的「邊緣分數」
    int value(vector<int> &pos){
        int R = board.size(), C= board[0].size();
        return min(pos[0],R-pos[0]-1)+min(pos[1],C-pos[1]-1);
    }
        
public:
    HorseWalk(int r, int c){
        board = vector(r, vector<int>(c, 0));
        find = false;
        dirs = {
            {1, 2}, 
            {2, 1}, 
            {-1, 2},
            {-2, 1},
            {1, -2}, 
            {2, -1},
            {-1, -2}, 
            {-2, -1}
        };
    };
        
    // 默認參數curstep表示現在第幾步
    void Move(vector<int> &pos, int curstep=1){
        int R = board.size(), C= board[0].size();
        board[pos[0]][pos[1]]=curstep;  //設定棋步
    
        //一旦找到一組解，印出解答並設find=True
        if (curstep== R * C){
            for(int i=0 ; i< R; i++){
                for(int j=0 ; j< C; j++){
                    printf("%2d ", board[i][j]);
                }
                cout << endl;
            }
            cout<<endl;
            find = true; 
        } 
        else{
            //nextPos是下一步可以走的座標位置，依「邊緣分數」排序
            vector<vector<int>> nextPos;
            for (auto d:dirs){
                vector<int> next{pos[0]+d[0], pos[1]+d[1]};
                if(valid(next)){
                    nextPos.push_back({pos[0]+d[0], pos[1]+d[1]});
                }
            }
            sort(nextPos.begin(), nextPos.end(), [this](vector<int> &p1, vector<int> &p2){return (value(p1) < value(p2));});

            // 檢查下一步可以走的八個方向
            for (auto p:nextPos){
                if (!find){
                    Move(p, curstep+1);
                }
            }          
        }
        board[pos[0]][pos[1]]=0; //撤銷棋步  
    }
};

int main()
{
    vector<int> iniPos = {0,0}; //初始座標
    HorseWalk solver(9,10);
    solver.Move(iniPos);
    return 0;
}

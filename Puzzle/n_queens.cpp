#include <iostream>
#include <string>
using namespace std;
#define QUEENNUM 4

int WeiZhi[QUEENNUM]; //記錄每列的皇后放在第幾行

// 視覺化的把一組答案印出來
void Output()
{
    static int iCount = 0;
    printf("第%2d種方案(★表示皇后):\n",++iCount);
    cout <<" "<< string(QUEENNUM, '-') <<endl;
    for(int i=0;i<QUEENNUM;i++)
    {
        printf(" |");
        for(int j=0;j<QUEENNUM;j++)
        {
            if(WeiZhi[i]==j)
            {
                printf("★");
            }
            else
            {
                printf((i^j)%2?"□":"■");
            }
        }
        printf("|\n");
    }
    cout <<" "<< string(QUEENNUM, '-') <<endl;
}

//參數n表示目前有幾個皇后擺好了
void Queens(int n)
{
    if(n==QUEENNUM)
    {
        Output();
        return;
    }
    for(int i=0; i<QUEENNUM;i++)
    {
        WeiZhi[n]=i;
        bool conflict = false;
        for(int j=0;j<n;j++)
        {
            //跟前面放好的皇后位置比，若任何一個位置衝突
            if(WeiZhi[j]==WeiZhi[n]|| abs(WeiZhi[j]-WeiZhi[n])==(n-j))
            {
                conflict = true;
                break;
            }
        }
        if(!conflict)
            Queens(n+1);
    }
}
int main()
{
    cout << "八后問題求解排列方案!" << endl;
    Queens(0);
    return 0;
}

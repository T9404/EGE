#include <iostream>
#include <conio.h>
#include <math.h>//для функции pow

using namespace std;

int start = 174457;
int en = 174505;
int divs[3]{};
int cnt = 0;
int sq = 1;

int main() {
	for (int i = start; i <= en; i++) {
		sq = pow(i, 0.5) / 1;
		if(pow(sq, 2)==i)
            continue;
        for(int d=2;  d<sq; d++){
            if(i%d==0){
                if(cnt>2)
                    break;
                divs[cnt]=d;
                cnt++;
                if(cnt>2)
                    break;
                divs[cnt]=i/d;
                cnt++;
            }
        }
        if(cnt==2){
            for(int j=0;j<2;j++)
                cout<<divs[j]<<" ";
            cout<<"\n";
        }
        cnt=0;
	}
	cout<<"Program ending. Press any key for close console...";
	getch();
}


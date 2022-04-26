#include<bits/stdc++.h>

#define pb push_back
#define sum(a) accumulate(a.begin(), a.end(), 0)
using namespace std;

//+1 +3 *2
// 1  2  3
int f(int s, int p, int c, int m){
    if(s>=55) return c%2==m%2;
    if(c==m) return 0;
    vector<int> h;
    if(p!=1) h.pb(f(s+1, 1, c+1, m));
    if(p!=2) h.pb(f(s+3, 2, c+1, m));
    if(p!=3) h.pb(f(s*2, 3, c+1, m));
    return (c%2!=m%2) ? sum(h)>0 : sum(h)==h.size();
}

int main(){
    for(int s=1; s<55; s++){
        for(int m=1; m<10; m++){
            if(f(s, 0, 0, m)){
                //if(m==2) cout << s << " " << m << "\n";
                //if(m==3) cout << s << " " << m << "\n";
                //if(m==4) cout << s << " " << m << "\n";
                break;
            }
        }
    }
}
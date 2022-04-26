#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define sum(a) accumulate(h.begin(), h.end(), 0)
int f(int a, int b, int c, int m){
    if(a+b>=63 && a+b<=74) return c%2==m%2;
    if(c==m) return 0;
    vector<int>h;
    if(a+2+b<=74) h.pb(f(a+2, b, c+1, m)), h.pb(f(a, b+2, c+1, m));
    if(a*2+b<=74) h.pb(f(a*2, b, c+1, m));
    if(a+b*2<=74) h.pb(f(a, b*2, c+1, m));
    if(h.size()) return (c%2!=m%2)? sum(h)>0 : sum(h)==h.size();
}
int main(){
    for(int s=1; s<=47; s++){
        for(int m=1; m<8; m++){
            if(f(15, s, 0, m)){
                //if(m==3) cout << s << " " << m << "\n"; пишем в else sum(h)>0 (т.к неудачный ход)
                //if(m==3) cout << s << " " << m << "\n";
                //if(m==4) cout << s << " " <<  m << "\n";
                cout << s << " " << m << "\n";
                break;
            }
        }
    }
}

//3
//2 30
//14

#include<bits/stdc++.h>
using namespace std;
#define sum(a) accumulate(a.begin(), a.end(), 0)
int f(int a, int b, int s, int c, int m){
    if(a+b+s>=71) return c%2==m%2;
    if(c==m) return 0;
    vector<int>h{f(a*2, b, s, c+1, m), f(a, b*2, s, c+1, m), f(a, b, s*2, c+1, m),
                 f(a+3, b, s, c+1, m), f(a, b+3, s, c+1, m), f(a, b, s+3, c+1, m)};
    return (c%2!=m%2)? sum(h)>0 : sum(h)==h.size();
}
int main(){
    for(int s=58; s>=1; s--){
        for(int m=1; m<10; m++){
            if(f(7, 5, s, 0, m)){
                if(m==4) cout << s << " " << m << "\n";
                break;
            }
        }
    }
}
#include<bits/stdc++.h>
using namespace std;
#define pos [](int p){return p>0;}
//пусть +1, +2, *3 
//будут иметь коды  соответственно: 1, 2, 3 
int f(int s, int p, int c, int m){
    if(s>=140) return c%2==m%2;
    if(c==m) return 0;
    vector<int>h;
    if(p!=1) h.push_back(f(s+1, 1, c+1, m));
    if(p!=2) h.push_back(f(s+2, 2, c+1, m));
    if(p!=2) h.push_back(f(s*3, 3, c+1, m));
    return (c%2!=m%2)? any_of(h.begin(), h.end(), pos) : all_of(h.begin(), h.end(), pos);
}
int main(){
    for(int s=1; s<=139; s++){
        for(int m=1; m<10; m++){
            if(f(s, 0, 0, m)){
                if(m==2) cout << s << "\n";
                break;
            }
        }
    }
}
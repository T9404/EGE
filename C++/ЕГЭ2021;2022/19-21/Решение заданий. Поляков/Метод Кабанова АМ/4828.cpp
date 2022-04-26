#include<bits/stdc++.h>
// +1, +3 *3
//   1     2   3
#define pb push_back
#define pos [](int p){return p>0; }
using namespace std;
int f(int s, int p0, int p1, int c, int m){
    if(s>=76) return c%2==m%2;  
    vector<int>h; 
    if(p0!=1) h.pb(f(s+1, 1, p0, c+1, m));
    if(p0!=2) h.pb(f(s+3, 3, p0, c+1, m));
    if(p0!=3) h.pb(f(s*3, 3, p0, c+1, m));
    if(c==m) return 0;
    return (c%2!=m%2)? any_of(h.begin(), h.end(), pos) : all_of(h.begin(), h.end(), pos);
}
int main(){
    for(int s=1; s<=75; s++){
        for(int m=1; m<5; m++){
            if(f(s, 0, 0, 0, m)){
                if(m==2) cout << s << " " << m << "\n";
                break;
            }
        }
    }
}
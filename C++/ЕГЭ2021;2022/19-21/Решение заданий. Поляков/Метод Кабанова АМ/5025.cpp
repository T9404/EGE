#include<bits/stdc++.h>

using namespace std;
#define pos [](int p){return p>0;}

int f(int s, int sp, int c, int m){
    if(s>=20) return c%2==m%2;
    if(c==m) return 0;
    vector<int> h{f(s+2, sp, c+1, m), f(s*2, sp, c+1, m)};
    if(!sp) h.push_back(f(s, 1, c+1, m));
    return (c%2!=m%2) ? any_of(h.begin(), h.end(), pos) : all_of(h.begin(), h.end(), pos);
}

int main(){
    for(int s=1; s<=19; s++){
        for(int m=1; m<7; m++){
            if(f(s, 0, 0, m)){
                //if(m==2) cout << s << " " <<  m << "\n"; //№19
                // для №19 в тернарном операторе в else нужно any_of, 
                //т.к подходит любой случай победы

                //if(m==3) cout << s << " " << m << "\n"; //№20
                //if(m%2==0) cout << s << " " << m << "\n"; //№21
                break;
            }
        }
    }
}
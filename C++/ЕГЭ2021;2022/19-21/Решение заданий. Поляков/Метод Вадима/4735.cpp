#include<bits/stdc++.h>

#define pii pair<int, int>
#define x first
#define y second
#define pb push_back
using namespace std;
map<pii, string> mp;

string g(pii p){
    if(mp.count(p)==0){
        if(p.x+p.y>=63 && p.x+p.y<=74) mp[p]="w";
        else{
            vector<pii> h;
            if(p.x+p.y+2<=74) h.pb({p.x+2, p.y}), h.pb({p.x, p.y+2});
            if(p.x*2+p.y<=74) h.pb({p.x*2, p.y});
            if(p.x+p.y*2<=74) h.pb({p.x, p.y*2});

            if(any_of(h.begin(), h.end(), [](pii r){ return g(r)=="w"; })) mp[p]="p1";
            else if(all_of(h.begin(), h.end(), [](pii r){ return g(r)=="p1"; })) mp[p]="v1";
            else if(any_of(h.begin(), h.end(), [](pii r){ return g(r)=="v1"; })) mp[p]="p2";
            else if(all_of(h.begin(), h.end(), [](pii r){ return g(r)=="p2" || g(r)=="p1"; })) mp[p]="v2";
            else if(any_of(h.begin(), h.end(), [](pii r){ return g(r)=="v2"; })) mp[p]="p3";
            else if(all_of(h.begin(), h.end(), [](pii r){ return g(r)=="p1" || g(r)=="p2" || g(r)=="p3"; })) mp[p]="v3";
        }
    }
    return mp[p];
}

int main(){
    for(int s=1; s<=47; s++){
        //if(g({15, s})=="v1") cout << s << "\n";
        //if(g({15, s})=="p2") cout << s << "\n";
        //if(g({15, s})=="v2") cout << s << "\n";
    }
}
//3 //меняем all на any когда присваиваем mp[p]=v1
//2 30
//14
#include<bits/stdc++.h>
using namespace std;
#define pii pair<int, int>
#define x first
#define y second
#define pb push_back
// +1, +2, *3
//  1   2   3
vector<pii>m(pii p){
    vector<pii>h;
    if(p.y!=1) h.pb({p.x+1, 1});
    if(p.y!=2) h.pb({p.x+2, 2});
    if(p.y!=3) h.pb({p.x*3, 3});
    return h;
}
map<pii, string>mp;
string g(pii p){
    if(mp.count(p)==0){
        if(p.x>=140) mp[p]="w";
        else{
            vector<pii>h=m(p);
            if(any_of(h.begin(), h.end(), [](pii p){return g(p)=="w";})) mp[p]="p1";
            else if(all_of(h.begin(), h.end(), [](pii p){return g(p)=="p1";})) mp[p]="v1";
            else if(any_of(h.begin(), h.end(), [](pii p){return g(p)=="v1";})) mp[p]="p2";
            else if(all_of(h.begin(), h.end(), [](pii p){return g(p)=="p1" || g(p)=="p2";})) mp[p]="v2";
            else if(any_of(h.begin(), h.end(), [](pii p){return g(p)=="v2";})) mp[p]="p3";
            else if(all_of(h.begin(), h.end(), [](pii p){return g(p)=="p1" || g(p)=="p2" || g(p)=="p3";})) mp[p]="v4";
            else if(any_of(h.begin(), h.end(), [](pii p){return g(p)=="v4";})) mp[p]="p4";
            else if(all_of(h.begin(), h.end(), [](pii p){return g(p)=="p1" || g(p)=="p2" || g(p)=="p3" || g(p)=="p4";})) mp[p]="v5";
            else if(any_of(h.begin(), h.end(), [](pii p){return g(p)=="v5";})) mp[p]="p5";
        }
    } return mp[p];
}
int main(){
    for(int s=1; s<=139; s++){ 
        //if(g{s, 0}=="v1") cout << s << " " << g({s, 0}) << "\n"; //№19
        //if(g({s, 0})=="p2") cout << s << " " << g({s, 0}) << "\n"; //№20
        //if(g({s, 0})=="v2") cout << s << " " << g({s, 0}) << "\n"; //№21
        
    }
}

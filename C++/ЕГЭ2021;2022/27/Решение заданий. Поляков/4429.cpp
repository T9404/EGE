#include<bits/stdc++.h>

#define pb push_back
using namespace std;

int gcd(int a, int b){
    while(b){
        a%=b;
        swap(a, b);
    }
    return a;
}

int lcm(int a, int b){
    return a/gcd(a, b)*b;
}

int main(){
    fstream f;
    f.open("4429B.txt");
    vector<int> s{0};
    int n;
    f>>n;
    while(n--){
        int k;
        f>>k;
        vector<int> a(k), t;
        for(auto &e:a) f>>e;
        for(int i=0; i<k; i++){
            for(int j=i+1; j<k; j++){
                for(auto &e:s){
                    t.pb(e+lcm(a[i], a[j]));
                }
            }
        }
        sort(t.begin(), t.end());
        map<int, int> mp;
        for(auto &e:t) mp[e%35]=e;
        s.clear(), s.reserve(mp.size());
        transform(mp.begin(), mp.end(), back_inserter(s), [](pair<int, int> p){ return p.second; });
    }
    int res=0;
    for(auto &e:s) if(e%5==0 || e%7==0) res=max(res, e);
    cout<<res;
}

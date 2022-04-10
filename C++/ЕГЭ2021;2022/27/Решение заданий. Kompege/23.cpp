#include <bits/stdc++.h>

using namespace std;
using ll=long long;

int main(){
    fstream f;
    f.open();
    int n;
    f>>n;
    vector<int> s={0};
    while(n--){
        pair<int, int> p;
        f>>p.first>>p.second;
        vector<int> t;
        t.reserve(2*s.size());
        for(auto &e : s)
            t.push_back(e+p.first), t.push_back(e+p.second);
        sort(t.begin(), t.end());
        map<int, int> mp;
        for(auto &e : t)
            mp[e%3]=e;
        s.clear();
        s.reserve(mp.size());
        transform(mp.begin(), mp.end(), back_inserter(s), [](pair<int, int> h){ return h.second; });
    }
    int maxres=0;
    for(auto &e : s)
        if(e%3)
            maxres=max(maxres, e);
    cout << maxres;
}
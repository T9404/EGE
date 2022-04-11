#include <bits/stdc++.h>
using namespace std;
int main()
{
    fstream f;
    f.open("2904B.txt");
    int n;
    f >> n;
    vector<pair<int, int>> s = {{0, 0}}, res;
    while (n--)
    {
        int x;
        f >> x;
        vector<pair<int, int>> f;
        f.reserve(s.size() + 1);
        for (auto &e : s)
            f.push_back({e.first + x, e.second + 1});
        f.push_back({x, 1});
        sort(f.rbegin(), f.rend(), [](const pair<int, int> &l, const pair<int, int> &r)
             {
            if(l.first==r.first) return l.second>r.second;
            return l.first<r.first; });
        unordered_map<int, pair<int, int>> mp;
        for (auto &e : f)
            mp[e.first % 2077] = e;
        if (mp.count(0))
            res.push_back(mp[0]);
        s.clear();
        s.reserve(mp.size());
        transform(mp.begin(), mp.end(), back_inserter(s), [](const pair<int, pair<int, int>> &h)
                  { return h.second; });
    }
    sort(res.begin(), res.end(), [](const pair<int, int> &l, const pair<int, int> &r)
         {
        if(l.first==r.first) return l.second>r.second;
        return l.first<r.first; });
    cout << res[0].second;
}
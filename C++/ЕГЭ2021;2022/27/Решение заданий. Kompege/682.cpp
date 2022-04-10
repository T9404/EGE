#include <bits/stdc++.h>

using namespace std;

int main()
{
    fstream f;
    f.open("682B.txt");
    int n;
    f >> n;
    vector<int> s = {0};
    while (n--)
    {
        int a, b, c;
        f >> a >> b >> c;
        vector<int> t;
        t.reserve(3 * s.size());
        for (auto &e : s)
            t.push_back(e + a + b), t.push_back(e + a + c), t.push_back(e + b + c);
        sort(t.begin(), t.end());
        map<int, int> mp;
        for (auto &e : t)
            mp[e % 4] = e;
        s.clear(), s.reserve(mp.size());
        transform(mp.begin(), mp.end(), back_inserter(s), [](pair<int, int> h)
                  { return h.second; });
    }
    int mxres = 0;
    for (auto &e : s)
        if (e % 4 == 0)
            mxres = max(mxres, e);
    cout << mxres;
}

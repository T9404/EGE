#include <bits/stdc++.h>
using namespace std;
#define x first.first
#define y first.second
#define z second
vector<int> delta = {3, 13, 23};
vector<pair<pair<int, int>, int>> m(pair<pair<int, int>, int> h)
{
    vector<pair<pair<int, int>, int>> res;
    for (auto &e : delta)
    {
        res.push_back({{h.x + e, h.y}, h.z});
        res.push_back({{h.x, h.y + e}, h.z});
        res.push_back({{h.x, h.y}, h.z + e});
    }
    return res;
}
map<pair<pair<int, int>, int>, string> mp;
string g(pair<pair<int, int>, int> h)
{
    if (mp.count(h) == 0)
    {
        if (h.x + h.y + h.z >= 73)
            mp[h] = "w";
        else
        {
            vector<pair<pair<int, int>, int>> M = m(h);
            if (any_of(M.begin(), M.end(), [](pair<pair<int, int>, int> p)
                       { return g(p) == "w"; }))
                mp[h] = "p1";
            else if (all_of(M.begin(), M.end(), [](pair<pair<int, int>, int> p)
                            { return g(p) == "p1"; }))
                mp[h] = "v1";
            else if (any_of(M.begin(), M.end(), [](pair<pair<int, int>, int> p)
                            { return g(p) == "v1"; }))
                mp[h] = "p2";
            else if (all_of(M.begin(), M.end(), [](pair<pair<int, int>, int> p)
                            { return g(p) == "p1" or g(p) == "p2"; }))
                mp[h] = "v2";
        }
    }
    return mp[h];
}
int main()
{
    for (int i = 1; i <= 23; i++) //№19 - проверка с any_of: строка 31; запускать отдельно
    {
        pair<pair<int, int>, int> p = {{2, i}, 2 * i};
        if (g(p) == "v1")
        {
            cout << i << ": " << g(p) << "\n";
        }
    }
    for (int i = 1; i <= 23; i++) //№20
    {
        pair<pair<int, int>, int> p = {{2, i}, 2 * i};
        if (g(p) == "p2")
        {
            cout << i << ": " << g(p) << "\n";
        }
    }
    for (int i = 1; i <= 23; i++) //№21
    {
        pair<pair<int, int>, int> p = {{2, i}, 2 * i};
        if (g(p) == "v2")
        {
            cout << i << ": " << g(p) << "\n";
        }
    }
}
#include <bits/stdc++.h>
using namespace std;

map<pair<int, int>, string> mp;

vector<pair<int, int>> m(pair<int, int> h)
{
    return {{h.first + 1, h.second}, {h.first * 4, h.second}, {h.first, h.second + 1}, {h.first, h.second * 4}};
}

string g(pair<int, int> h)
{
    if (mp.count(h) == 0)
    {
        if (h.first + h.second >= 95)
            mp[h] = "w";
        else
        {
            vector<pair<int, int>> M = m(h);

            if (any_of(M.begin(), M.end(), [](pair<int, int> p)
                       { return g(p) == "w"; }))
                mp[h] = "p1";

            else if (all_of(M.begin(), M.end(), [](pair<int, int> p)
                            { return g(p) == "p1"; }))
                mp[h] = "v1"; // для 19-ого вопроса any_of

            else if (any_of(M.begin(), M.end(), [](pair<int, int> p)
                            { return g(p) == "v1"; }))
                mp[h] = "p2";

            else if (all_of(M.begin(), M.end(), [](pair<int, int> p)
                            { return g(p) == "p1" || g(p) == "p2"; }))
                mp[h] = "v2";
        }
    }
    return mp[h];
}

int main()
{
    for (int s = 1; s <= 89; s++) //№19
    {
        if (g({5, s}) == "v1")
        { // v1 проверка с any (строка 20, т.к Петя сделал неудачный ход)
            cout << s << ": " << g({5, s}) << "\n";
        }
    }

    for (int s = 1; s <= 89; s++) //№20
    {
        if (g({5, s}) == "p2")
        {
            cout << s << ": " << g({5, s}) << "\n";
        }
    }

    for (int s = 1; s <= 89; s++) //№21
    {
        if (g({5, s}) == "v2")
        {
            cout << s << ": " << g({5, s}) << "\n";
        }
    }

    return 0;
}
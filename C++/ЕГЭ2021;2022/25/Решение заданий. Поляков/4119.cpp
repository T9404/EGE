#include <bits/stdc++.h>
using namespace std;
vector<int> dels(int n)
{
    set<int> res;
    int i = 2;
    while (i * i <= n)
    {
        if (n % i == 0)
            res.insert({i, n / i});
        i++;
    }
    return {res.begin(), res.end()};
}
int main()
{
    vector<pair<int, int>> vec;
    for (int i = 550001; vec.size() < 5; i++)
    {
        auto rf = dels(i);
        if (rf.size())
        {
            int sr = (1.0 * accumulate(rf.begin(), rf.end(), 0) / rf.size());
            if (sr % 31 == 13)
                vec.push_back({i, sr});
        }
    }
    for (auto &e : vec)
        cout << e.first << " " << e.second << "\n";
}
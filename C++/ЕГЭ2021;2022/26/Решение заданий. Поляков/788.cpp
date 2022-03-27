#include <bits/stdc++.h>
using namespace std;
pair<int, int> func(int maxsize, vector<int> &a)
{
    vector<int> pref(a.size() + 1);
    pref[1] = a[0];
    for (int i = 2; i <= a.size(); i++)
        pref[i] = pref[i - 1] + a[i - 1];
    int sum, ind;
    for (int i = 1; i <= a.size(); i++)
    {
        if (pref[i] > maxsize)
        {
            ind = i - 1, sum = maxsize - pref[i];
            break;
        }
    }
    for (int i = a.size() - 1; i >= 0; i--)
    {
        if (sum + a[i] <= maxsize)
        {
            return {ind, a[i]};
        }
    }
}
int main()
{
    fstream f;
    f.open("788.txt");
    int d, e, n;
    f >> d >> e >> n;
    vector<int> mi, bi;
    int x;
    while (n--)
    {
        f >> x;
        if (x <= 500)
            mi.push_back(x);
        else
            bi.push_back(x);
    }

    sort(mi.begin(), mi.end());
    auto m = func(e, mi);

    sort(bi.begin(), bi.end());
    auto b = func(d, bi);

    cout << b.first + m.first << " " << b.second + m.second;
}
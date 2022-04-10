#include <bits/stdc++.h>
using namespace std;

int main()
{
    fstream f;
    f.open();
    int n;
    f >> n;
    vector<pair<int, int>> s, res;; //нужна сумма+кол-во чисел кратынх5
    while (n--)
    {
        int v;
        f >> v;
        vector<pair<int, int>> t;
        for (auto &e : s)
            t.push_back({e.first + v, e.second + (v % 5 == 0)}); //получаем подпоследовательность на основе старой
        t.push_back({v, (v % 5 == 0)});                            //начинаем новую подпоследовательность

        sort(t.begin(), t.end(), [](pair<int, int> l, pair<int, int> r){
            if(l.first==r.first) return l.second<r.second;
            return l.first<r.first; }); //сортировка сначала по сумме, затем по кол-ву кратных 5
        map<int, pair<int, int>> mp; //сгруппируем по остаткам на 3 от кол-ва кратных5
        for (auto &e : t)
            mp[e.second % 3] = e;
        s.clear(), s.reserve(mp.size());
        if (mp.count(0))
            res.push_back(mp[0]); //записываем в массив итоговый
        transform(mp.begin(), mp.end(), back_inserter(s), [](pair<int, pair<int, int>> h){ return h.second; }); //получаем из map->ключи
    }
    int mx = 0;
    for (auto &e : res)
    {
        if (e.second % 3 == 0)
            mx = max(mx, e.first);
    }
    cout << mx;
}
#include <bits/stdc++.h>

#define pb push_back
using namespace std;

struct point // структура для точки
{
    int x, y;
};

double s(point A, point B, point C)
{
    double ab = hypot(B.x - A.x, B.y - A.y); //вычисляем стороны треугольника
    double ac = hypot(C.x - A.x, C.y - A.y);
    double cb = hypot(C.x - B.x, C.y - B.y);

    vector<double> vec = {ab, ac, cb};
    sort(vec.begin(), vec.end());

    if (vec[0] + vec[1] > vec[2]) // проверяем, что треуг. невырожденный
    {
        double p = (ab + ac + cb) / 2;
        return (sqrt(p * (p - ab) * (p - ac) * (p - cb))); // формула герона
    }

    return 0.0;
}

int main()
{
    fstream f;
    f.open("2731B.txt");

    int n;
    f >> n;

    vector<point> ay0, ost;

    for (int i = 0; i < n; i++)
    {
        point p;
        f >> p.x >> p.y;
        if (p.y == 0)
            ay0.pb(p);
        else
            ost.pb(p);
    }

    //сортируем точки с ординатой=0 по X,
    sort(ay0.begin(), ay0.end(), [](point l, point r)
         { return l.x < r.x; });

    point a = ay0[0], b = ay0.back(); // фиксируем две точки, максимально удаленные друг от друга

    double maxs = 0;
    for (auto &c : ost)
    { // перебираем 3-ю и обновляем макс.площадь
        maxs = max(maxs, s(a, b, c));
    }
    
    cout << maxs;
}
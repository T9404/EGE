#include <bits/stdc++.h>
using namespace std;

int main()
{
    fstream f;
    f.open("17-2017.txt");
    vector<int> a;
    int x;
    while (f >> x)
    {
        if (x % 16 == 11 and x % 7 == 0 and x % 6 != 0 and x % 13 != 0 and x % 19 != 0)
            a.push_back(x);
    }
    cout << accumulate(a.begin(), a.end(), 0) << " " << a.size();
    // accumulate(a.begin(), a.end(), x): 
    // функция, которая считает сумму в контейнере 
    // в пределах [begin; end) с начальной суммой, равной x
    // заменяемо цикл, но смысл теряется: проще считать сумму и кол-во отдельно
}
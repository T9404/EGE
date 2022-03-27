#include <bits/stdc++.h>
using namespace std;

string bin(int n)
{
    string s = "";
    while (n)
    {
        s += (n % 2 + '0');
        n /= 2;
    }
    reverse(s.begin(), s.end());
    return s;
}

int ten(string s)
{
    int res = 0;
    for (int i = 0; i < s.size(); i++)
        res += (s[i] - '0') * pow(2, s.size() - i - 1);
    return res;
}

int f(int n)
{
    string s = bin(n);
    s.push_back(s.back());
    s += (count(s.begin(), s.end(), '1') % 2 == 0) ? "0" : "1"; // добавляем бит четности
    s += (count(s.begin(), s.end(), '1') % 2 == 0) ? "0" : "1";
    return ten(s);
}

int main()
{
    for (int i = 1; i < 1000; i++)
    {
        if (f(i) > 130)
        {
            cout << i;
            break;
        }
    }
}
/*
    Примечание: бит четности можно добавить таким образом:
    if(count(s.begin(), s.end(), '1')%2==0) s+='0';
    else s+='1';
    Здесь же применен тернарный оператор, если условие в скобочках выполняется, то добавится "0", иначе "1"

*/
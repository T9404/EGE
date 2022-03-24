#include <bits/stdc++.h>
using namespace std;

vector<string> split(string &s, char d)
{
    vector<string> res;
    string t;
    istringstream istr(s);

    while (getline(istr, t, d))
        res.push_back(t);

    return res;
}

int main()
{
    fstream f;
    f.open("4524.txt");
    string s;
    f >> s;

    vector<string> res = split(s, '.');
    string m = "";

    for (int i = 1; i < res.size(); i++)
    {
        if (res[i - 1].size() + 1 + res[i].size() > m.size())
            m = res[i - 1] + '.' + res[i];
    }

    cout << m << "\n"
         << m.size();
}
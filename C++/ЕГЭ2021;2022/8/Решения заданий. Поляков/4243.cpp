#include <bits/stdc++.h>

#define npos string::npos
using namespace std;

bool check(string s)
{
    set<char> c;
    for (auto &i : s)
        c.insert(i);
    return (c.size() == s.size() && s[0] != 'I' && s.find("VF") == npos && s.find("FV") == npos);
}

int main()
{
    int c = 0;
    string s = "VAIFU";
    for (int i1 = 0; i1 < 5; i1++)
        for (int i2 = 0; i2 < 5; i2++)
            for (int i3 = 0; i3 < 5; i3++)
                for (int i4 = 0; i4 < 5; i4++)
                {
                    string p = {s[i1], s[i2], s[i3], s[i4]};
                    if (check(p))
                        c++;
                }
    cout << c;
}

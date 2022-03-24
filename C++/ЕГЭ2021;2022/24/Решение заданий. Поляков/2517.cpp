#include <bits/stdc++.h>

using namespace std;
#define npos string::npos

// 1 способ со сплитами

int main()
{
    fstream f;
    f.open("2420.txt");

    string s;
    f >> s;

    replace(s.begin(), s.end(), 'C', ' ');
    replace(s.begin(), s.end(), 'D', ' '); // убираем ненужные символы

    istringstream iss(s);
    vector<string> res(istream_iterator<string>{iss}, istream_iterator<string>()); //разбиваем по пробелам
    //если есть необходимость разбивать не по пробелам,
    //то нужно перегружать istream_iterator<...> по нужному знаку

    string m = *max_element(res.begin(), res.end(), [](string l, string r)
                            { return l.size() < r.size(); });

    cout << m << " " << m.size();
}

// 2 способ - дп

int main()
{
    fstream f;
    f.open("2420.txt");

    string s;
    f >> s;

    string check = "ABEF";
    vector<int> dp(s.size());

    if (check.find(s[0]) != npos)
        dp[0] = 1;

    for (int i = 1; i < s.size(); i++)
    {
        if (check.find(s[i]) != npos)
            dp[i] = dp[i - 1] + 1;

        else
            dp[i] = 0;
    }

    cout << *max_element(dp.begin(), dp.end());
}
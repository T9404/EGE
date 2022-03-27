#include <bits/stdc++.h>
using namespace std;

int main()
{
    fstream f;
    f.open("1395.txt");
    
    int s, n;
    
    vector<int> a(n);
    
    f >> s >> n;
    
    for (auto &e : a)
        f >> e;
    
    sort(a.begin(), a.end());
    
    int sum = 0, count = 0;
    
    for (int i = 0; i < a.size(); i++)
    {
        if (sum + a[i] <= s)
        {
            sum += a[i], count++;
        }
        else
            break;
    }
    
    cout << n - count << " " << accumulate(a.begin(), a.end(), -sum);
}

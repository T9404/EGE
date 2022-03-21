#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;


bool check(int x)
{
    for (int j = 2; j <= x / 2; j++)
    {
        if (x % j == 0)
            return false;
    }
    return true;
}


int main()
{

    long long int k = 0, ans = 0, s = 0, n, x;

    vector<long long> prefix(9, 2e15);

    ifstream f("27-82b.txt");
    f >> n;

    for (int i = 0; i < n; i++)
    {
        f >> x;
        s += x;

        if (check(x))
            k++;

        if (k % 9 == 0)
            ans = s;

        if (prefix[k % 9] != 2e15)
            ans = max(ans, s - prefix[k % 9]);

        prefix[k % 9] = min(prefix[k % 9], s);
    }


    cout << ans;

    return 0;
}
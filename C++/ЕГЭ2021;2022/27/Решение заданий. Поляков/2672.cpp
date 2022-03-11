#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int n, x, count_6 = 0, count_2 = 0, count_3 = 0, ans = 0;

    ifstream f("27-12b.txt");
    f >> n;

    for (int i = 0; i < n; i++)
    {
        f >> x;
        if (x % 6 == 0)
        {
            count_6++;
        }
        else if (x % 2 == 0)
        {
            count_2++;
        }
        else if (x % 3 == 0)
        {
            count_3++;
        }
    }

    int other = n - count_6 - count_2 - count_3;

    cout << (count_6 * (count_6 - 1) / 2) + count_6 * (n - count_6) + count_2 * count_3;

    return 0;
}
#include <iostream>
using namespace std;

int main()
{

    int m;

    for (long long int i = 0; i < 300000000; i++)
    {
        int x, a, b, d, w;
        x = i;
        a = 5;
        b = 13;
        w = 7;

        while (x > 0)
        {
            d = x % w;
            a *= d;
            if (d < 5)
                b += d;
            x /= w;
            w = 12 - w;
        }

        if ((a == 225) && (b == 27))
            m = i;
    }

    cout << m;

    return 0;
}
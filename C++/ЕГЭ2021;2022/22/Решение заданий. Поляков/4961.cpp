#include <iostream>
using namespace std;

int main()
{

    int x, m;

    for (int i = 0; i < 100000; i++)
    {
        int a = 18, b = 432;
        x = i;

        while (x > 0)
        {
            a++;

            if (x % 2 == 1)
                b -= (x % 100);

            x /= 10;
        }
        if (a == 22 && b == 246)
            m = i;
    }

    cout << m;

    return 0;
}
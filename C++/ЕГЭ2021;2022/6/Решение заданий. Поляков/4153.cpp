#include <iostream>
using namespace std;

int main()
{
    for (int i = 6000; i >= 1; i--)
    {

        int n, s;
        n = 1;
        s = i;
        while (s > 200)
        {
            s = s - 15;
            n = n + 3;
        }

        if (n == 46)
        {
            cout << i << endl;
            break;
        }
    }

    return 0;
}
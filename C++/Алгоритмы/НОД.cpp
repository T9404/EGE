#include <iostream>
using namespace std;

int GCD(int a, int b) { //способ 1

    while ((a != 0) && (b != 0))
    {
        if (a > b)
            a = a % b;
        else
            b = b % a;
    }

    return (a + b);
}
int gcd(int a, int b) // способ 2
{
    while (b)
    {
        a %= b;
        swap(a, b);
    }
    return a;
}
int main() {

    cout << GCD(15, 5);
    cout << gcd(15, 5);
    return 0;
}
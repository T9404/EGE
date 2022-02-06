#include <iostream>

int GCD(int a, int b) {

    while ((a != 0) && (b != 0))
    {
        if (a > b)
            a = a % b;
        else
            b = b % a;
    }

    return (a + b);
}

int main() {

    std::cout << GCD(15, 5);
    return 0;
}
#include <iostream>
using namespace std;
int main() {
    for (int i = 0; i <= 1000; i++) {
        int s;
        s = i;
        int n = 11;
        while (s < 224) {
            s = s + 15;
            n = n + 8;
        }

        if (n == 115) {
            cout << i;
            break;
        }
    }

    return 0;
}
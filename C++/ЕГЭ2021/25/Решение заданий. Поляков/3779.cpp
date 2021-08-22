#include <iostream>  
#include <cmath>
#include <algorithm>
using namespace std;



int f(int x) {

    int sqr = sqrt(x); int k = 0; // счетчик
    int  del = 0; // макс делитель

    for (int i = 1; i <= sqr; i++) {
        if (x % i == 0) {
            if ((i % 2) != 0) {
                k++;
                del = max(del, i);
            }
            if ((x / i) % 2 != 0) {
                k++;
                del = max(del, x / i);
            }
        }
    }

    if (k == 5) 
        return del;
    else
        return false;
}


int main()  // за 2.5 мин нашел предпоследний делитель, 4.5 мин отработал полностью) 
{
    for (int i = 78000000; i <= 85000000; i++) {
        if (f(i)) {
            cout << i << " " << f(i) << endl;
        }
    }

    return 0;
}
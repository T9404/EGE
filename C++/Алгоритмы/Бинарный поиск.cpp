#include <iostream>
#include <algorithm>

int bin_search(int x, int v[], int n)
{
    int low, high, mid;
 
    low = 0;
    high = n;
    while(low <= high) {
        mid = (low + high) / 2; 
        if(x < v[mid])              
            high = mid - 1;
        else if(x > v[mid])
            low = mid + 1;
        else
            return mid;
    }
    return -1;
}
 

int main() {

    int a[5] = {1, 2, 3, 4, 5};

    int value = bin_search(12, a, 5);

    if (value != -1)
        std::cout << "Index: " << value;
    else
        std::cout << "Nothing found";

    return 0;
}

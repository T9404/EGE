#include <iostream>
#include <algorithm>

void bubble_sort(int *a, int n) {
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n-1; i++) 
        {
            if (a[i] > a[i+1])
                std::swap(a[i], a[i+1]);
        }
    }
}

int main() {

    int a[5] = {50, 22, 10, 3, 11};

    bubble_sort(a, 5);

    for (auto elem : a) 
    {
        std::cout << elem << " ";
    }
    
    return 0;
}

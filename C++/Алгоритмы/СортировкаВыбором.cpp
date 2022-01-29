#include <iostream>
#include <algorithm>

void selection_sort(int *a, int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = i+1; j < n; j++) 
        {
            if (a[i] > a[j]) 
                std::swap(a[i], a[j]);
        }
    }

}

int main() {

    int a[5] = {5, 52, 11, 3, 1};

    selection_sort(a, 5);

    for (int i = 0; i < 5; i++)
        std::cout << a[i] << " ";

    return 0;
}

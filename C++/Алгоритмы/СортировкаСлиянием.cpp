#include <iostream>


void merge(int* first, int* middle, int* last)
{
    int n = last - first;
    std::cout << "merge part, n= " << n << "\n";
    std::cout << "merge part, middle= " << *middle << "\n";
    std::cout << "merge part, last= " << *last << "\n";
    int* deck = new int[n];

    int* left = first;
    std::cout << "merge part, left = first " << *left << "\n";
    int* right = middle;
    std::cout << "merge part, right = middle " << *right << "\n";
    for (int* d = deck; d != deck + n; ++d) {
        if (left == middle) *d = *right++;
        else if (right == last) *d = *left++;
        else if (*left < *right) *d = *left++;
        else *d = *right++;
    }

    int* d = deck;
    while (first != middle) *first++ = *d++;
    while (middle != last) *middle++ = *d++;

    delete[] deck;
}


void mergesort(int* first, int* last)
{
    int n = last - first;
    if (n <= 1) return;
    std::cout << "n= " << n;
    int* middle = first + n / 2;
    std::cout << "first = " << *first << "middle = " << *middle << "\n";
    mergesort(first, middle);
    mergesort(middle, last);
    merge(first, middle, last);
}



int main()
{
    int a[4] = { 6,2,1,3 };
    int* first = a;
    int* last = a + 4;
    mergesort(first, last);
    std::cout << a[0] << a[1] << a[2] << a[3] << "\n";
    return 0;
}

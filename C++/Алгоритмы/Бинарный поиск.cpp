#include <iostream>

int binsearch(int x, int v[], int n)
{
    int low, high, mid;

    low = 0;
    high = n;
    while (low <= high) {
        mid = (low + high) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else
            return mid;
    }
    return -1;
}

int main()
{
    int i, ret, num, nsize = 6, a[6];

    /* заполнение массива */
    for (i = 0; i < nsize; i++) {
        a[i] = i;
        printf("%d ", a[i]);
    }

    num = 1;

    /* поиск числа num в массиве a */
    if ((ret = binsearch(num, a, nsize)) < 0)
        printf("\n Not found ", num);
    else
        printf("\n %d in array \n", num, ret);
    return 0;
}

#include <iostream>
using namespace std;

void Output(int* a, int n)
{
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
}

void InsertSort(int* a, int n)
{
    int tmp;
    for (int i = 1, j; i < n; ++i)
    {
        tmp = a[i];
        for (j = i - 1; j >= 0 && a[j] > tmp; --j)
            a[j + 1] = a[j];
        a[j + 1] = tmp;
       
    }
    Output(a, n);
}

int main()
{
    int* a = new int[5];

    for (int i = 0; i < 5; i++)
        cin >> a[i];

    InsertSort(a, 5);

    delete[]a;

    return 0;
}

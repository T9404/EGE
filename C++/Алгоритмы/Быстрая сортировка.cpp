#include <iostream>

void quickSort(int* array, int low, int high)
{
    int i = low;
    int j = high;
    int pivot = array[(i + j) / 2];
    int temp;

    while (i <= j)
    {
        while (array[i] < pivot)
            i++;
        while (array[j] > pivot)
            j--;
        if (i <= j)
        {
            temp = array[i];
            array[i] = array[j];
            array[j] = temp;
            i++;
            j--;
        }
    }
    if (j > low)
        quickSort(array, low, j);
    if (i < high)
        quickSort(array, i, high);
}

int main()
{
    int array[] = { 95, 45, 48, 98, 1, 485, 65, 478, 1, 2325 };
    int n = sizeof(array) / sizeof(array[0]);
    
    for (int i = 0; i < n; ++i)
        std::cout << array[i] << std::endl;

    quickSort(array, 0, n);

    std::cout << "####################" << std::endl;

    for (int i = 0; i < n; ++i)
        std::cout << array[i] << std::endl;


    return (0);
}

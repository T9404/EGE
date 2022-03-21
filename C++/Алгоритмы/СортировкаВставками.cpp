#include <iostream>
#include <algorithm>

void insertion_sort(int *array, int size) {
   int key, j;

   for(int i = 1; i<size; i++) 
   {
      key = array[i];
      j = i;
      while(j > 0 and array[j-1]>key) 
      {
         array[j] = array[j-1];
         j--;
      }
      array[j] = key;   
   }
}

int main() {

    int a[5] = {5, 0, 100, 3, 1};

    insertion_sort(a, 5);

    for (int i = 0; i < 5; i++)
        std::cout << a[i] << " ";

    return 0;
}

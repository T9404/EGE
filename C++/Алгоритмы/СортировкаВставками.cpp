#include <iostream>

void insertSort(int a[], int n) {
	for (int i = 1; i < n; i++) {
		for (int j = i; ((j > 0) and (a[j - 1] > a[j])); j--) {
			std::swap(a[j - 1], a[j]);
		}
	}
}


int main() {

	int arr[] = { 100, 12, 11, 0, 1, 22, 101 };
	int size = sizeof(arr) / sizeof(int);

	insertSort(arr, size);

	for (int i = 0; i < size; i++) {
		std::cout << arr[i] << std::endl;
	}
	return 0;
}

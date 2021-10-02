#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {

	fstream f("C:\\Users\\admin\\Downloads\\17-1.txt");

	int n = 10000, k = 0, mina = 10000000000;
	vector<int> array_numbers;


	for (int i = 0; i < n; i++) {
		int number;
		f >> number;
		array_numbers.push_back(number);
	}


	for (int i = 1; i < n; i++) {

		int a = abs(array_numbers[i - 1]);
		int b = abs(array_numbers[i]);

		if (((a % 7 == 0) && (b % 17 != 0)) || ((a % 17 != 0) && (b % 7 == 0))) {
			k++;
			mina = min(mina, array_numbers[i - 1] + array_numbers[i]);
		}
	}


	cout << k << " " << mina;

	return 0;
}



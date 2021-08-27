#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
	int n, x;
	fstream f("C:\\Users\\admin\\Downloads\\27-59b.txt");
	f >> n;

	vector<int> count = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

	for (int i = 0; i < n; i++) {
		f >> x;
		vector<int> neww = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };



		for (int j = 0; j < 10; j++) {
			neww[(x + j) % 10] += count[(j)]; // суммируем кол-во пар с этим числом
		}
		neww[x % 10] ++; // суммируем само число



		for (int j = 0; j < 10; j++) { // запись в главный массив
			count[j] += neww[j];
		}




	}
	cout << count[5];

	return 0;
}
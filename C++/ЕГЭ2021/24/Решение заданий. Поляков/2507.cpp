#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("k8.txt");

int main() {
	char left, right; // два элемента для их сравнения

	int cnt(1), maxcnt(1);
	char symb;

	fin.get(left);
	while (fin.get(right)) {
		if (left == right) cnt++;
		else {
			if (cnt > maxcnt) { maxcnt = cnt; symb = left; }
			cnt = 1;
		}
		left = right;
	}

	cout << symb << " " << maxcnt;
	fin.close();

	return 0;
}

#include <iostream>
#include <cmath>
using namespace std;

bool F(int x) {
	for (int i = 2; i <= sqrt(x); i++)
		if (x % i == 0)
			return false;
	return true;
}

int main() {
	int k = 0, medium;
	for (int i = 3000000; i <= 10000000; i++) {
		if (F(i) and F(i + 2)) {
			k++;
			medium = (i + i + 2) / 2;

		}
	}

	cout << k << " " << medium;
	
	return 0;
}

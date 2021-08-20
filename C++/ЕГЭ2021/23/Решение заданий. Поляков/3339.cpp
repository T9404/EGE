#include <iostream>
using namespace std;

int F(int x, int y) {
	int k;
	if (y < x || y == 10 || y == 11) return 0;
	if (x == y) return 1;
	k = F(x, y - 1) + F(x, y - 2);
	if (y % 3 == 0) k += F(x, y / 3);
	return k;
}

int main() {
	cout << F(1, 8) * F(8, 28) << endl;
	return 0;
}

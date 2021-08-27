#include <iostream>
using namespace std;
int main() {
	int a, x, y;
	bool flag;

	for (a = 0; a <= 100; a++) {
		flag = true;

		for (y = 0; y <= 1000; y++)
			for (x = 0; x <= 1000; x++)
				if (!(((pow(x, 2) - 10 * x + 16) > 0) || ((pow(y, 2) - 10 * y + 21) > 0) || ((x * y) < (2 * a))))
					flag = false;
		if (flag) {
			cout << a;
			break;
		};
	};
};
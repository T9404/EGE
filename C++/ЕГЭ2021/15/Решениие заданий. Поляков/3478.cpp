#include <iostream>
using namespace std;
int main() {
	int a, x, y;
	bool fl;
	for (a = 0; a <= 100; a++) {
		fl = true;
		for (x = 0; x <= 1000; x++)
			for (y = 0; y <= 1000; y++)
				if ((((x * y) > a) and (x > y) and (x < 8)))
					fl = false;
		if (fl) {
			cout << a; break;
		};
	};
};
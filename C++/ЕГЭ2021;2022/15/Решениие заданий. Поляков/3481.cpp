#include <iostream>
using namespace std;

int main() {
	for (int a = 0; a < 100; a++) {
		bool flag = true;
		for (int x = 1; x < 1000; x++) {
			for (int y = 1; y < 1000; y++) {
				if (!((((x - 20) < a) and ((10 - y) < a)) || (((x + 4) * y) > 45))) {
					flag = false; break;
				}

			}
		}
		if (flag == true) {
			cout << a; break;
		}
	}

	return 0;
}
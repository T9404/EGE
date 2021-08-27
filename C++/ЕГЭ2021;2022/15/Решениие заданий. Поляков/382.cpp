#include <iostream>
using namespace std;

int main() {
	for (int a = 1; a <= 100; a++) {
		bool flag = true;
		for (int x = 1; x <= 10000; x++) {
			if (!(((x & 29) != 0) <= (((x & 9) == 0) <= ((x & a) != 0)))) {
				flag = false; break;
			}
		}
		if (flag == true) {
			cout << a; break;
		}
	}
			
	return 0;
}

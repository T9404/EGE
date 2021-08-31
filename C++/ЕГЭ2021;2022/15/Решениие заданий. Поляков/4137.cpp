#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	vector <int> v;
	for (int i = 29; i < 48; i++) {
		v.push_back(i);
	}
	for (int a = 1; a < 100; a++) {
		bool flag = true;
		for (int x = -1000; x < 1000; x++) {
			if (!((x % 3 != 0 and x != 48 and x != 52 and x != 56) <= ((abs(x - 50) <= 7) <= (find(v.begin(), v.end(), x) != v.end())) || ((x & a) == 0))){
				flag = false; break;

			}
		}
		if (flag == true) {
			cout << a; break;
		}
	}

	return 0;
}
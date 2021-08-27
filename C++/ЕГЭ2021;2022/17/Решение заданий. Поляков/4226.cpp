#include <iostream>
using namespace std;


int main() {
	int count = 0, mik = 10000000, mak = 0;
	for (int x = 2048; x <= 8192; x++) {
		if ((x % 7 == 0) and (x % 11 != 0) and (x % 23 != 0) and (x % 10 != 8)) {
			count += 1;
			mik = min(mik, x);
			mak = max(mak, x);
		}
	}
	for (int x = 12048; x <= 18192; x++) {
		if ((x % 7 == 0) and (x % 11 != 0) and (x % 23 != 0) and (x % 10 != 8)) {
			count += 1;
			mik = min(mik, x);
			mak = max(mak, x);
		}
	}
	cout << count << " " << mak - mik;


	return 0;
}
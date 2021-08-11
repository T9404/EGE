#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
int f(int x) {
	int mina = 1000000;
	vector<int> div;
	int sqr = round(sqrt(x));
	for (int i = 2; i <= sqr; i++) {
		if (x % i == 0) {
			div.push_back(i);
			div.push_back(x / i);
		}
		for (int j = 0; j < div.size(); j++) {
			if ((div[j] % 10 == 8) and (div[j] != 8) and (div[j] != x)) {
				mina = min(div[j], mina);
			}
		}
	}
	if (mina != 1000000)
		return mina;
	else
		return false;
}


int main() {


	int count = 0;

	for (int i = 500001; i <= 510020; i++) {
		if (count == 5)
			break;
		if (f(i) != false) {
			cout << i << " " << f(i) << endl;
			count++;
		}
	}


	return 0;
}
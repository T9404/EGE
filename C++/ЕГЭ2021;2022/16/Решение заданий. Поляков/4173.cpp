#include <iostream>
using namespace std;

int f(int n) {
	if (n == 0) {
		return 1;
	}
	else if (n == 1) {
		return 3;
	}
	else if (n > 1) {
		return f(n - 1) - f(n - 2) + 3 * n;

	}
};

int main() { cout << f(40); }
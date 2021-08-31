#include <iostream>
#include <cmath>
using namespace std;
int main() {
	int c = 0;
	for (long int i = 500000; i < 10000000; i++) {
		int md = 0;
		for (int d = 2; d <= round(sqrt(i)); d++)
			if (i % d == 0) {
				if (d != 8 && d % 10 == 8) {
					md = d;
					break;
				}
				if ((i / d) % 10 == 8)
					md = i / d;
			}
		if (md > 0) {
			std::cout << i << " " << md << std::endl;
			c = c + 1;
			if (c == 5) break;
		}
	}
}
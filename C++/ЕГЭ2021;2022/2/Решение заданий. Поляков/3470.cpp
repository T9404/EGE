#include <iostream>
using namespace std;

int main() {
	cout << "x y z w" << endl;
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 2; y++) {
			for (int z = 0; z < 2; z++) {
				for (int w = 0; w < 2; w++) {
					if ((x and (y || !z) and w) == (x <= !y and z)) {
						cout << x << ' ' << y << ' ' << z << ' ' << w << endl;

					}

				}

			}

		}
	}

	return 0;
}
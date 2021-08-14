#include <iostream>
using namespace std;



int main() {

	cout << "a b c d" << endl;
	for (int a = 0; a <= 1; a++)
		for (int b = 0; b < 2; b++)
			for (int c = 0; c < 2; c++)
				for (int d = 0; d <= 1; d++)
					if ((a <= d) & (!(b <= c)))
						cout << a << " " << b << " " << c << " " << d << endl;
	
	return 0;
}
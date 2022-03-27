#include <iostream>
using namespace std;

int main()
{
	cout << "x y z" << endl;
	for (int x = 0; x <= 1; x++)
		for (int y = 0; y <= 1; y++)
			for (int z = 0; z <= 1; z++)
				if ((!x and y and z) || (!x and !z))
					cout << x << ' ' << y << ' ' << z << ' ' << endl;
	return 0;
}

#include <iostream>
#include <vector>
using namespace std;

bool func(int x, int y, int z, int w)
{
	return (x and z) or ((w <= x) == (z <= y));
}

int main()
{
	cout << "x y z w F" << endl;

	vector<int> number = {0, 1};

	for (auto &x : number)
		for (auto &y : number)
			for (auto &z : number)
				for (auto &w : number)
					if (func(x, y, z, w) == false)
						cout << x << " " << y << " " << z << " " << w << " "
							 << "0" << endl;
	return 0;
}
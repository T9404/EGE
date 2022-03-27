#include <iostream>
using namespace std;

bool f(int a, int x)
{
	return ((a % 7 == 0) and (240 % x == 0) <= ((a % x != 0) <= (780 % x != 0)));
};

int main()
{
	bool ok;
	int a, x;
	int count_a = 0;

	for (a = 1; a <= 1000; a++)
	{
		ok = true;
		for (x = 1; x <= 1000; x++)
			if (!(f(a, x)))
			{
				ok = false;
			};

		if (ok)
		{
			count_a += 1;
		};
	};

	cout << count_a;
}
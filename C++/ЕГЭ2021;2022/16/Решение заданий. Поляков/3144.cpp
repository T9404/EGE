#include <iostream>
using namespace std;

int F(int n, int m)
{
	if (m == 0)
		return 1;
	else
		return n * F(n, m - 1);
}

int main()
{

	int count = 0;

	for (int n = 1; n <= 100000; n++)
	{
		if ((F(n, 2) >= 100) and (F(n, 2) <= 1000))
			count++;
	}

	cout << count;

	return 0;
}
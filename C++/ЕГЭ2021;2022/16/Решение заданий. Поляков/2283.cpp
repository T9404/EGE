#include <iostream>
using namespace std;

int F(int n)
{
	if (n > 25)
		return (n * n + 4 * n + 3);
	if (n <= 25 && n % 3 == 0)
		return (F(n + 1) + 2 * F(n + 4));
	if (n <= 25 && n % 3 != 0)
		return (F(n + 2) + 3 * F(n + 5));
}

int main()
{
	int count = 0;

	for (int n = 1; n <= 1000; n++)
	{
		int a = F(n);
		int count1 = 0;
		while (a > 0)
		{
			count1 += a % 10;
			a /= 10;
		}
		if (count1 == 24)
			count += 1;
	}
	cout << count;
	
	return 0;
}

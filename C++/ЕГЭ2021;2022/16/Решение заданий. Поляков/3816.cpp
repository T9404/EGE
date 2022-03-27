#include <iostream>
using namespace std;


int f(int n)
{
	if (n < 2)
	{
		return 1;
	}
	else if ((n >= 2) and (n % 3 == 0))
	{
		return f(n / 3) - 1;
	}
	else if ((n >= 2) and (n % 3 != 0))
	{
		return f(n - 1) + 17;
	}
}

int main()
{

	int count = 0;

	for (int n = 1; n <= 100000; n++)
	{
		if (f(n) == 43)
			count++;
	}

	cout << count;
	
	return 0;
}
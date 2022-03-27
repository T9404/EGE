#include <iostream>

int sum(int x)
{
	int s = 0;

	while (x > 0)
	{
		s += (x % 10);
		x = x / 10;
	}

	return s;
}

int pr(int y)
{
	int p = 1;

	while (y > 0)
	{
		p *= (y % 10);
		y = y / 10;
	}

	return p;
}

int main()
{
	int c = 0, min = 1000000;

	for (int x = 4616; x <= 52311; x++)
		if (sum(x) == 10 && pr(x) == 0)
		{
			c += 1;
			if (x < min)
				min = x;
		}

	std::cout << c << " " << min;
}
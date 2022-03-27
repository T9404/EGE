#include <iostream>

int main()
{
	int max = 0, c = 0;
	for (int i = 3399; i <= 225599; i++)
		if (i % 5 == 3)
		{
			int k = i;
			int c7 = 0;
			while (k > 0)
			{
				if (k % 7 == 0)
					c7 += 1;
				k = k / 7;
			}
			if (c7 == 0)
			{
				c += 1;
				if (i > max)
					max = i;
			}
		}
	std::cout << c << ' ' << max;
}

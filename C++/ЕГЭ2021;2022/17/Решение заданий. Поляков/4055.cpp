#include <iostream>

int main()
{
	int c = 0, sum = 0, max = 0, min = 1000000;

	for (int i = 4855; i <= 7856; i++)
		if (i % 6 == 0 && i % 15 == 0 && i % 7 != 0 && i % 16 != 0 && (((i / 100) % 10) + ((i % 100) / 10)) % 2 == 0)
		{
			c += 1;
			sum += i;
			if (i > max)
				max = i;
			if (i < min)
				min = i;
		}
		
	std::cout << (sum / c) + max + min;
}
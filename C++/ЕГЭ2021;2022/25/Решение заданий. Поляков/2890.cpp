#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int count = 1;

	for (size_t i = 6638225; i <= 6638322; i++)
	{
		bool flag = true;

		for (int j = 2; j <= ceil(sqrt(i)); j++)
		{
			if (i % j == 0)
			{
				flag = false;
				break;
			}
		}

		if (flag == true)
		{
			cout << count << ' ' << i << endl;
			count++;
		}
	}

	return 0;
}

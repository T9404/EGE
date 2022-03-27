#include <iostream>
using namespace std;

int main()
{
	int count = 0, max;

	for (int i = 1221; i <= 9763; i++)
	{
		if (i % 7 == 0 && i % 2 != 0 && i % 5 != 0 && i % 11 != 0 && i % 49 != 0)
		{
			count += 1;
			max = i;
		}
	}

	cout << count << ' ' << max << endl;
	
	return 0;
}

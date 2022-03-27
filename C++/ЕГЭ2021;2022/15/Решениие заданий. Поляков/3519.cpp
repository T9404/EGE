#include <iostream>
using namespace std;

int main()
{
	for (int a = 1; a < 100; a++)
	{
		bool flag = true;
		for (int x = 1; x < 1000; x++)
		{
			if (!(((((x & 13) != 0 || (x & a) == 0)) <= (x & 13) != 0) || ((x & a) != 0) || ((x & 39) == 0)))
			{
				flag = false;
				break;
			}
		}
		if (flag == true)
		{
			cout << a;
			break;
		}
	}

	return 0;
}
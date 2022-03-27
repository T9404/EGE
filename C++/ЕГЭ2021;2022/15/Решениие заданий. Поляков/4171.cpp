#include <iostream>
using namespace std;

int main()
{
	for (int a = 1; a < 100; a++)
	{
		bool flag = true;
		for (int x = 1; x < 1000; x++)
		{
			if (!((x / 50 > 3) || !(x / 13 > 3) || (x / a > 6)))
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
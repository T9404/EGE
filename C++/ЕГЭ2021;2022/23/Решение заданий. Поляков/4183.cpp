#include <iostream>
using namespace std;

int recursion(int start, int end)
{
	if (start == end)
	{
		return 1;
	}
	else if (start < end)
	{
		return 0;
	}
	else
	{
		return recursion(start - 8, end) + recursion(start / 2, end);
	}
}

int main()
{
	cout << (recursion(102, 43) * recursion(43, 5));
	return 0;
}
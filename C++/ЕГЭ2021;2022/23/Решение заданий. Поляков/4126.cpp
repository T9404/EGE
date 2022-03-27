#include <iostream>
using namespace std;

int recursion17(int start, int end)
{
	if (start == end)
	{
		return 1;
	}
	else if ((start > end))
	{
		return 0;
	}
	else
	{
		return recursion17(start + 1, end) + recursion17(start + 2, end);
	}
}

int recursion23(int start, int end)
{
	if (start == end)
	{
		return 1;
	}
	else if ((start > end))
	{
		return 0;
	}
	else
	{
		return recursion17(start + 1, end) + recursion17(start + 2, end);
	}
}

int recursion1723(int start, int end)
{
	if (start == end)
	{
		return 1;
	}
	else if ((start > end))
	{
		return 0;
	}
	else
	{
		return recursion17(start + 1, end) + recursion17(start + 2, end);
	}
}

int main()
{
	cout << (recursion17(11, 17) * recursion17(17, 29)) + (recursion23(11, 23) * recursion23(23, 29) - (recursion1723(11, 17) * recursion1723(17, 23) * recursion1723(23, 29))) << endl;
	return 0;
}
#include <iostream>

int f(int s, int e) {
	if (s > e) 
	{
		return 0;
	}
	else if (s == e)
	{
		return 1;
	}
	else 
	{
		return f(s + 1, e) + f(s + 5, e) + f(s * 3, e);
	}
}

int main() {
	for (int i = 0; i < 100000; i++) 
	{
		if (f(1, i) == 175) 
		{
			std::cout << i;
			break;
		}
	}
	return 0;
}

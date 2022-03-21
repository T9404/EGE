#include <iostream>
#include <algorithm>
using namespace std;

bool f(int a1, int a2, int x) {
	return ((a1 <= x <= a2) <= (10 <= x <= 29)) || (13 <= x <= 18);
}

bool f_x(int a1, int a2) {
	for (int x = 0; x <= 100; x++) {
		if (f(a1, a2, x) == 0) {
			return 0;
		}
	}
	return 1;
}

int main() {
	int m = 0, start, end;
	for (int a1 = 10; a1 <= 29; a1++) 
	{
		for (int a2 = a1 + 1; a2 <= 29; a2++) 
		{
			if (f_x(a1, a2)) 
			{
				if (a2 - a1 > m) 
				{
					m = a2 - a1;
					start = a1;
					end = a2;
				}
			}
		}
	}

	cout << m << endl;
	cout << start << " " << end;

	return 0;
}
#include <iostream>
#include <fstream>
using namespace std;

int main() {
	string s;
	ifstream f("24-j7.txt");
	f >> s;

	int max_len = 1; int len = 1;

	for (int i = 0; i < s.length(); i++) {
		int s_1 = s[i];
		int s_2 = s[i + 1];

		if ((s_1 % 2) == (s_2 % 2))
		{
			len++;
			max_len = max(len, max_len);
		}
		else {
			len = 1;
		}
	}
	cout << max_len;
	return 0;
}

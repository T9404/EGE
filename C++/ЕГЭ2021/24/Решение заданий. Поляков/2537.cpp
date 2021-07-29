#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream f("24-5.txt");
	string s;
	f >> s;
	int count = 0;

	for (int i = 1; i < s.length(); i++) {
		if ((s[i - 1] == '(') && (s[i] == ')')) {
			count++;
			i++;
		}

	}

	cout << count;

	f.close();

	return 0;

}



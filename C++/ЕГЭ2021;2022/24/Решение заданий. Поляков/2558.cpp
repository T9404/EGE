#include <iostream>
#include <fstream>
using namespace std;

int main() {
	string s;
	ifstream f("24-s1.txt");

	int count = 0;

	while (f >> s) {
		
		for (int i = 1; i < s.length(); i++) {
			if ((s[i - 1] == 'A') && (s[i + 1] == 'R')) {
				count++;
				break;
			}
		}

	}
	cout << count;
	f.close();

	return 0;

}


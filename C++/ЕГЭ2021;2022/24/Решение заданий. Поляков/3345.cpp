#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int countBOSS(string s, string s1) {
	int count = 0;
	for (size_t i = s.find(s1); i != string::npos; i = s.find(s1, i + s1.size())) {
		if (s[i - 1] != 'J' && s[i + 4] != 'J') count++;
	}
	return count;
}

int main() {
	ifstream f("24-j4.txt");
	string s, s1 = "BOSS";
	f >> s;
	cout << countBOSS(s, s1) << endl;
	return 0;
}

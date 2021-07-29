#include <iostream>
#include <fstream>
using namespace std;

int main() { //Решение Евгения Джобса
		ifstream f("24.txt");
		string s;
		f >> s;
		int c = 1, m = 0;
		for (int i = 1; i < s.length(); i++) {
			if (!(s[i - 1] == 'd' && s[i] == 'a' || s[i - 1] == 'a' && s[i] == 'd'))
				c = c + 1;
			else
				c = 1;
			if (m < c) 
				m = c;
		}
		cout << m;
	
	return 0;
}

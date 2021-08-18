
//הכÿ פאיכא A

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{

	int kol_ch, a, min_pr = 100000000;
	ifstream f("27-A.txt");
	vector <int> v;
	f >> kol_ch;
	for (int i = 0; i < kol_ch; i++)
	{
		f >> a;
		v.push_back(a);
	}

	for (int g = 0; g < v.size() - 6; g++)
	{
		for (int j = g + 6; j < v.size(); j++)
		{
			if (v[g] % 2 == 1 && v[j] % 2 == 1)
			{
				if (v[g] * v[j] < min_pr) min_pr = v[g] * v[j];
			}
			else continue;
		}

	}

	f.close();

	if (min_pr != 100000000) cout << min_pr;
	else cout << -1;

	return 0;
}
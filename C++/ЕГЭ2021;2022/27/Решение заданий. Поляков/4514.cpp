#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	int s = 0;
	int k = 0;
	int answer = 0;
	vector<int> arr(13, 100000);

	fstream f("C:\\Users\\admin\\Downloads\\27-81bb.txt");
	f >> n;

	for (int i = 0; i < n; i++)
	{
		int x;
		f >> x;
		s += x;
		if (x % 2 != 0)
			k++;
		if (k % 13 == 0)
		{
			answer = s;

		}
		else if (arr[k % 13] != 0) {
			answer = max(answer, s - arr[k % 13]);
		}

		arr[k % 13] = min(arr[k % 13], s);
	}

	cout << answer;


	return 0;
}
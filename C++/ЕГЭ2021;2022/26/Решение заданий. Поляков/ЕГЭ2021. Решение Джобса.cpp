#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
using namespace std;
int main() {
	ifstream f("26.txt");
	int n, a, b, r, m;
	f >> n;
	vector <vector <int>> nums;
	for (int i = 1; i <= n; i++) {
		f >> a >> b;
		vector<int> temp = { a, -b };
		nums.push_back(temp);
	}
	sort(nums.begin(), nums.end());
	r = 0; m = 0;
	for (int i = 1; i < nums.size(); i++)
		if (nums[i][0] == nums[i - 1][0])
			if (nums[i][1] - nums[i - 1][1] == 3) {
				r = nums[i][0];
				m = -nums[i][1] + 1;
			}
	f.close();
	cout << r << " " << m;
	return 0;
}

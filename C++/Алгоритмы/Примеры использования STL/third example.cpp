#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;


int main() {

	vector<int> vec{ 1, 2, 3, 4, 6, 5, 5, 5 };
	cout << count(vec.begin(), vec.end(), 5) << endl; // amount 5



	vector<int>::iterator p = find_if(vec.begin(), vec.end(), [](int i)
		{
			return i > 4; // ...4, 6, 5...
		});
	cout << "First number greater than 4 is : " << *p << endl; // check output
	cout << endl << endl;




	cout << "min and max: ";

	auto i1 = max_element(vec.begin(), vec.end()); // max value
	cout << *i1 << " ";

	auto i2 = min_element(vec.begin(), vec.end()); // min value
	cout << *i2 << endl;



	cout << "min and max: ";
	cout << min({ 12, 13, 16 }) << " " << max({ 12, 13, 16 }) << endl;



	return 0;
}
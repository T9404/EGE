#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool value3(int value) {
	return value == 5;
}


int main() {

	vector<int> arr(10, 2);  // 2222...2
	if (all_of(arr.begin(), arr.end(), [](int i) {return i % 2 == 0; })) // all in c++
	{
		cout << "good \n";
	}



	if (std::any_of(arr.cbegin(), arr.cend(), value3)) // any in c++
	{
		cout << "yes" << endl;
	}
	else {
		cout << "no" << endl;
	}
	cout << endl;




	int ar[6] = { 1, 2, 3, 4, 5, 6 };
	int ar1[6]; // new array

	// Using copy_n() to copy contents
	copy_n(ar, 6, ar1);

	cout << "new array after copying is : ";
	for (int i = 0; i < 6; i++)
		cout << ar1[i] << " ";

	cout << endl << endl;



	vector<int> vec = { 1, 2, 3, 4, 5 };
	for_each(vec.begin(), vec.end(), [](int a) {cout << a << " "; }); // old vector
	cout << endl;

	for_each(vec.begin(), vec.end(), [](int& a) {a += 5; }); // write briefly

	for_each(vec.begin(), vec.end(), [](int a) {cout << a << " "; }); // new vector

	return 0;
}
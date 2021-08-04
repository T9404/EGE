#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void bubble_sort(vector<int>& arr) {
    int n = (int)arr.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }

}

int main() {
    vector<int> array = { 789, 45, 6, 8, 0, 131, 1444, 157, 63 };
    bubble_sort(array);
    for (auto elem : array) {
        cout << elem << " ";
    }
    return 0;
}
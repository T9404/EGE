#include <iostream>
#include <algorithm>
using namespace std;



int main() {

    string s = "abc"; // can have repeat values, but need do sort or reverse
    sort(s.begin(), s.end(), greater<char>());

    while (prev_permutation(s.begin(), s.end()))
    {
        cout << s << endl;
    };


    cout << endl << endl;


    string s1 = "aab";  // repeat letters in word
    while (next_permutation(s1.begin(), s1.end()))
    {
        cout << s1 << endl;
    }



    return 0;
}

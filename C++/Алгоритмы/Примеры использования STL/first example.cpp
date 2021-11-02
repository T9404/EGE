#include <iostream>
#include<string>
#include <iterator>
#include <vector>
#include <set>
#include <map>
using namespace std;

int main() {
    string str = "helloworld";
    string::iterator it;

    cout << "The string using forward iterators is : ";
    for (it = str.begin(); it != str.end(); it++)
        cout << *it;
    cout << endl << endl;




    vector<int> arr = { 1, 3, 5, 7, 9 };
    vector<int>::iterator elem;

    for (elem = arr.begin(); elem != arr.end(); elem++)
    {
        cout << *elem << ' ';
    }
    cout << endl;

    for (int& em : arr)
        cout << em << ' ';
    cout << endl << endl;



    cout << "use set: " << endl;
    set <int> s1;
    s1.insert(40); // add
    s1.insert(200); // add
    s1.erase(40); // del

    set<int>::iterator itra;

    for (itra = s1.begin(); itra != s1.end(); itra++)
    {
        cout << *itra << ' ';
    }

    cout << endl << endl;



    cout << "use multiset: ";
    multiset <int> news;

    news.insert(12);
    news.insert(122);
    news.insert(12);

    news.erase(news.find(12)); // del 1 element
    for (auto& a : news)
    {
        cout << '\t' << a;
    }

    cout << endl << endl;



    cout << "use map: ";
    map<int, int> dict;

    dict.insert(pair<int, int>(1, 40));
    dict.insert(pair<int, int>(12, 1100));

    map<int, int>::iterator cred;

    for (cred = dict.begin(); cred != dict.end(); cred++)
    {
        cout << '\n' << cred->first << " " << cred->second;
    }



    return 0;
}

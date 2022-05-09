#include<bits/stdc++.h>
#include<regex>
#define istr istream_iterator
using namespace std;
int main(){
    fstream f; f.open("181.txt");
    string s; f >> s;
    vector<string> p{"A", "E", "I", "O", "U", "Y"};
    for(auto&c:p){
        s=regex_replace(s, regex(c), " ");
    }
    istringstream iss(s);
    vector<string>sub(istr<string>{iss}, istr<string>());
    int res=0;
    for(auto&s:sub){
        if(count(s.begin(), s.end(), '.')>=6) res=max(res, int(s.size())); 
    }
    cout << res;
}
#include<bits/stdc++.h>
#include<regex>
using namespace std;
int main(){
    fstream f; f.open("191.txt");
    string s; f >> s; 
    s=regex_replace(s, regex("B"), "B B");
    s=regex_replace(s, regex("A"), "A A");
    istringstream iss(s);

    vector<string>str(istream_iterator<string>{iss}, istream_iterator<string>());
    int res=0;
    for(auto&e:str){
        if(count(e.begin(), e.end(), 'F')==2 && e.size()>=20 && e[0]=='A' && e.back()=='B'){
            res++;
        }
    }
    cout << res;
}
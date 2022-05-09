#include<bits/stdc++.h>
#include<regex>
using namespace std;
int main(){
    fstream f; f.open("196.txt");
    string s; f >> s;
    s=regex_replace(s, regex("ZX"), "*");
    s=regex_replace(s, regex("ZY"), "*");
    int mx=0, res=0;
    for(int i=0; i<s.size(); i++){
        if(s[i]=='*'){
            res++;
        }else{
            mx=max(mx, res);
            res=0;
        }
    }
    cout << mx;
}
#include<bits/stdc++.h>
using namespace std;
string hex(int n){
    stringstream ss;
    ss << hex << n;
    string res=string(ss.str());
    return res;
}
string shex(int n){
    string s;
    while(n){
        switch (n%16){
        case 10: s+="a"; break;
        case 11: s+="b"; break;
        case 12: s+="c"; break;
        case 13: s+="d"; break;
        case 14: s+="e"; break;
        case 15: s+="f"; break;
        default: s+=(n%16+'0'); break;
        }
        n/=16;
    } return{s.rbegin(), s.rend()};
}
int count(string s, string t){
    int res=0;
    for(int i=0; i<=s.size()-t.size(); i++){
        int j=0;
        for(; j<t.size(); j++){
            if(s[i+j]!=t[j]) break;
        }
        if(j==t.size()) res++;
    }
    return res;
}
bool check(string s){
    return (s[0]=='f' && s.back()=='a' && count(s, "3b")==1);
}
//используем либо hex()[работает совсем немного дольше], 
//либо shex()[нужно писать для каждого остатка свое значение]
int main(){
    int st=15*pow(16, 4), end=pow(16, 5)-1, res=0;
    for(int i=st; i<=end; i++){
        if(check(shex(i))) res++;
    }
    cout << res;
}
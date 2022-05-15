#include<bits/stdc++.h>
using namespace std;
//{0, a}, {1, p}, {2, r}, {3, c}, {4, u}
#define npos string::npos
string fiv(int n){
    string s; 
    while(n){
        s+=(n%5+'0');
        n/=5; 
    } return {s.rbegin(), s.rend()};
}
bool check(const string& s){
    for(int i=1; i<s.size(); i++) if(s[i]=='0' && s[i-1]=='0') return false;
    return s[0]=='4';
}
int main(){
    for(int i=4*pow(5, 4); i<pow(5, 5); i++){
        if(check(fiv(i))){
            cout << i+1 << "\n";
            break;
        }
    }
}
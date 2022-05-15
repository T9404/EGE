#include<bits/stdc++.h>
using namespace std;
#define npos string::npos
string oct(int n){
    string s;
    while(n){
        s+=(n%8+'0');
        n/=8;
    } return{s.rbegin(), s.rend()};
}
bool check(string s){
    return ((s.back()-'0')%2==0 && s[0]=='7' && ((s.find("56")!=npos) ^ (s.find("65")!=npos)));
    // ^ - XOR, нам нужно чтобы встречалось только 56 или только 65
}
int main(){
    int res=0;
    int end=pow(8, 5)-1, st=7*pow(8, 4);
    for(int i=st; i<=end; i++){
        if(check(oct(i))) res++;
    }
    cout << res;
}
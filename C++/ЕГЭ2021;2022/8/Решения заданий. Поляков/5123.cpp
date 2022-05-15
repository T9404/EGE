#include<bits/stdc++.h>
using namespace std;
#define npos string::npos
int main(){
    string s="zboestv";
    int res=0;
    for(int i1=2; i1<7; i1++)
    for(int i2=0; i2<7; i2++)
    for(int i3=0; i3<7; i3++){
        string t{s[i1], s[i2], s[i3], 'v', 'v'};
        if(t.find("ev")==npos && t.find("ve")==npos && t.find("tb")!=npos) res++;
    }
    cout << res;
}
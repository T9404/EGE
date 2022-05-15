#include<bits/stdc++.h>
using namespace std;
#define npos string::npos
int main(){
    string s="oenfgi";
    int res=0;
    for(int i1=0; i1<6; i1++)
    for(int i2=0; i2<6; i2++)
    for(int i3=0; i3<6; i3++)
    for(int i4=0; i4<6; i4++){
        string t{s[i1], s[i2], s[i3], s[i4]};
        if( (t[0]=='e' || t[0]=='o')&& t.find("oge")==npos && t.find("ig")!=npos){
            res++;
        }
    }
    cout << res;
}
#include<bits/stdc++.h>
using namespace std;
#define npos string::npos 
bool check(string s){
    if((s.back()=='u' || s.back()=='i') && s.find("egu")==npos){
        int countfi=0;
        for(int i=1; i<s.size(); i++){
            if(s[i]=='i' && s[i-1]=='f') countfi++;
        }
        return countfi>=2;
    } return false;
}
int main(){
    string s="eguinf";
    int res=0;
    for(int i2=0; i2<6; i2++)
    for(int i3=0; i3<6; i3++)
    for(int i4=0; i4<6; i4++)
    for(int i5=0; i5<6; i5++)
    for(int i6=0; i6<6; i6++){
        string t{s[i2], s[i3], s[i4], s[i5], s[i6]};
        if(check(t)) res++;
    } 
    cout << res;
}
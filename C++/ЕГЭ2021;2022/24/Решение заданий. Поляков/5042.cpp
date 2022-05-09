#include<bits/stdc++.h>
using namespace std;
int main(){
    fstream f; f.open("5042.txt");
    string s; f >> s;
    int mx=0, res=0;
    for(int i=2; i<s.size(); i+=3){ //рассматриваем подстроки с 1 элемента
        if((s[i]=='X' && s[i-2]=='X') || (s[i]=='Y' && s[i-2]=='Y')){
            res++;
        }else{
            mx=max(mx, res);
            res=0;
        }
    }
    for(int i=3; i<s.size(); i+=3){ //со 2 элемента
        if((s[i]=='X' && s[i-2]=='X') || (s[i]=='Y' && s[i-2]=='Y')){
            res++;
        }else{
            mx=max(mx, res);
            res=0;
        }
    }
    for(int i=4; i<s.size(); i+=3){ //с 3 элемента
        if((s[i]=='X' && s[i-2]=='X') || (s[i]=='Y' && s[i-2]=='Y')){
            res++;
        }else{
            mx=max(mx, res);
            res=0;
        }
    }
    cout << mx;
}
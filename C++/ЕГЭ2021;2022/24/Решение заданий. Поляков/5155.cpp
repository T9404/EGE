#include<bits/stdc++.h>
using namespace std;
int main(){
  fstream f; f.open("5155.txt");
  string s; f >> s;
  int mx=0, res=0;
  //проверка подстрок с нечетным индексом 
  for(int i=1; i<s.size(); i+=2){
    string t{s[i-1], s[i]};
    if(t=="AA" || t=="CC") res++;
    else{
      mx=max(mx, res);
      res=0;
    } 
  }
  //проверка подстрок четным индексом
  for(int i=2; i<s.size(); i+=2){
    string t{s[i-1], s[i]};
    if(t=="AA" || t=="CC") res++;
    else{
      mx=max(mx, res);
      res=0;
      }
  }
  cout << mx;
}

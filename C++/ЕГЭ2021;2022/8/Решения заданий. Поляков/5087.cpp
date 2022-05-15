#include<bits/stdc++.h>
using namespace std;
#define npos string::npos
//{0, 'e'}, {1, 'k'}, {2, 'l'}, {3, 'o'}, {4, 'c'}, {5, 't'}
string six(int n){
    string s;
    while(n){
        s+=(n%6+'0');
        n/=6;
    } 
    while(s.size()<5) s.push_back('0'); //добавление незначащих нулей
    return{s.rbegin(), s.rend()};
}
int main(){
    for(int i=4*pow(6, 4); i<pow(6, 7); i++){
        string s=six(i);
        if(s.find("33")!=npos){
            cout << i+1;
            break;
        }
    }    
}
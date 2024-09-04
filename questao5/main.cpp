#include<bits/stdc++.h>
using namespace std;
string invert(string s){
    string aux = "";
    for(int i=s.size();i>=0;i--){
        aux+=s[i];
    }
    return aux;
}
int main(){
    string s;
    cout << "digite uma linha, que será invertida incluindo os espacos";
    getline(cin, s);
    cout << "Aqui estah a string invertida: ";
    cout << invert(s) << endl;
    
}
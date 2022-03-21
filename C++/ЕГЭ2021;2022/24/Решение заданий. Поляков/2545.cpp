#include <iostream>
#include <fstream>

using namespace std;

int main()
{

    string s;
    int k = 0;

    ifstream f("C:/Users/admin/Downloads/Prog/24-j5.txt");
    f >> s;

    for (int i = 0; i < s.length() - 2; i++)
    {
        if ((s[i] == 'K') && (s[i + 1] == 'O') && (s[i + 2] == 'T'))
            k++;
    }

    cout << k;

    return 0;
}
#include <iostream>
#include <fstream>

using namespace std;

int main()
{

    string s;
    int k = 0;

    ifstream f("C:/Users/admin/Downloads/Prog/24-5.txt");
    f >> s;

    for (int i = 0; i < s.length() + 1; i++)
    {
        if (s[i] == ')')
        {
            k++;
            if (k == 10000)
            {
                cout << i + 1;
                break;
            }
        }
    }

    return 0;
}
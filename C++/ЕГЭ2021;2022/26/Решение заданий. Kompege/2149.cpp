#include <bits/stdc++.h>
using namespace std;

int main()
{
    fstream f;
    f.open("2149.txt");

    int n, m, x;

    vector<int> img, vid;

    f >> n >> m;

    while (f >> x)
    {
        if (x <= 100)
            img.push_back(x);
        else
            vid.push_back(x);
    }

    sort(img.begin(), img.end()), sort(vid.begin(), vid.end());

    vector<int> vpr(vid.size() + 1);

    vpr[1] = vid[0];

    for (int i = 2; i <= vid.size(); i++)
        vpr[i] = vpr[i - 1] + vid[i - 1];

    vector<int> mpr(img.size() + 1);

    mpr[1] = img[0];

    for (int i = 2; i <= img.size(); i++)
        mpr[i] = mpr[i - 1] + img[i - 1];

    int count = 0;

    for (int i = 1; i <= vid.size(); i++)
    {
        if (vpr[i] >= (m / 2))
        {
            m -= vpr[i];
            count += i;
            break;
        }
    }

    int sumimg;

    for (int i = 1; i <= img.size(); i++)
    {
        if (mpr[i] > m)
        {
            count += (i - 1);
            sumimg = mpr[i - 2];
            break;
        }
    }

    for (int i = img.size() - 1; i >= 0; i--)
    {
        if (sumimg + img[i] <= m)
        {
            m -= (sumimg + img[i]);
            break;
        }
    }

    cout << m << " " << count;
}

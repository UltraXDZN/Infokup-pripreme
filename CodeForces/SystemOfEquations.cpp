//
// Created by UltraXDZN on 8/4/2022.00
//

#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, c = 0, s;
    cin >> n >> m;
    s = n + m;
    for(int a=0; a < s; a++){
        for(int b=0; b < s; b++) {
            if ((a * a + b) == n && (a + b * b) == m) {
                c++;
            }
        }
    }
    cout << c;

    return 0;
}
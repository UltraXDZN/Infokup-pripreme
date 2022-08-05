//
// Created by UltraXDZN on 8/5/2022.
//
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        long long s, s_sum = 0;

        cin >> s;


        for (int i = 9; i > 0; i--) {
            if ((s - i) <= 0) {
                s_sum += pow(10, 9 - i) * s;
                break;
            } else if ((s - i) > 0) {
                s -= i;
                s_sum += pow(10, 9 - i) * i;
            }
        }

        cout << s_sum << "\n";
    }

    return 0;
}
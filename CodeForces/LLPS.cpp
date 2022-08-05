//
// Created by UltraXDZN on 8/5/2022.
//
#include <bits/stdc++.h>

using namespace std;

int count_chars(const string& search, char lf) {
    int c = 0;
    for (char i : search) {
        if (i == lf) {
            c++;
        }
    }
    return c;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    string seq;
    char bc;
    int repeat;
    cin >> seq;
    bc = seq[0];
    for (int i = 0; i < seq.size() - 1; i++) {
        if (bc < seq[i + 1]) {
            bc = seq[i + 1];
        }
    }
    repeat = count_chars(seq, bc);
    for (int i = 0; i < repeat; i++) {
        cout << bc;
    }
    return 0;
}

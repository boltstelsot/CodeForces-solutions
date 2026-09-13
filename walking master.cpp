#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long a, b, c, d;
        cin >> a >> b >> c >> d;
        long long count = (d-b);
        a = a + count;
        if (a-c >= 0 && d-b >= 0) {
            cout << (count + a-c);
        }
        else {
            cout << -1;
        }
        cout << endl;
    }
}
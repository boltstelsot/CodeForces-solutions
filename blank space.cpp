#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        int ans = 0;
        int max_sequence = 0;

        for ( int i=0; i<n; i++) {
            int k;
            cin >> k;

            if (k == 0) {
                max_sequence += 1;
            }
            else {
                max_sequence = 0;
            }
            ans = max(max_sequence,ans);
        }
        cout << ans << endl;
    }
    return 0;
} 
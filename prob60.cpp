#include <iostream>

using namespace std;

const int N = 1e9 + 9;
const int S = 10000;

bool nprime[N + 1];

void sieve() {
  nprime[0] = nprime[1] = true;
  for (int i = 2; i * i <= N; ++i) {
    if (nprime[i]) continue;
    for (int j = i * i; j <= N; j += i) {
      nprime[j] = true;
    }
  }
}

int shift(int a) {
  int res = 1;
  while (a) {
    res *= 10;
    a /= 10;
  }
  return res;
}

int concat(const int& a, const int& b) {
  return a * shift(b) + b; 
}

int main() {
  sieve();

  cout << "sieve done" << endl;

  for (int a = 2; a <= S; ++a) {
    if (nprime[a]) continue;
    for (int b = a + 1; b <= S; ++b) {
      if (nprime[b]) continue;
      if (nprime[concat(a, b)] || nprime[concat(b, a)])
        continue;
      
      for (int c = b + 1; c <= S; ++c) {  
        if (nprime[c]) continue;
        if (nprime[concat(b, c)] || nprime[concat(c, b)])
          continue;
        if (nprime[concat(a, c)] || nprime[concat(c, a)])
          continue;

        for (int d = c + 1; d <= S; ++d) {
          if (nprime[d]) continue;
          if (nprime[concat(d, c)] || nprime[concat(c, d)])
            continue;
          if (nprime[concat(d, a)] || nprime[concat(a, d)])
            continue;
          if (nprime[concat(d, b)] || nprime[concat(b, d)])
            continue;

          for (int e = d + 1; e <= S; ++e) {
            if (nprime[e]) continue;
            if (nprime[concat(e, d)] || nprime[concat(d, e)])
              continue;
            if (nprime[concat(e, c)] || nprime[concat(c, e)])
              continue;
            if (nprime[concat(e, a)] || nprime[concat(a, e)])
              continue;
            if (nprime[concat(e, b)] || nprime[concat(b, e)])
              continue;

            cout << a << " ";
            cout << b << " ";
            cout << c << " ";
            cout << d << " ";
            cout << e << " ";
            cout << a + b + c + d + e << endl;

            return 0;
          }
        }
      } 
    }
  }

  return 0;
}
#include <iostream>
#include <set>
#include <vector>

using namespace std;

const int N = 1e6;

int ftors[N + 1];

void sieve() {
  for (int i = 2; i * i <= N; ++i) {
    if (ftors[i])
      continue;
    for (int j = i * i; j <= N; j += i) {
      ftors[j] = i;
    }
  }
}

int phi(const int& n) {
  set<int> fset;

  int tmp = n;
  while (tmp != 1) {
    if (ftors[tmp]) {
      fset.insert(ftors[tmp]);
      tmp /= ftors[tmp];
    } else {
      fset.insert(tmp);
      break;
    }
  }

  int sol = n - 1;
  set<int>::iterator it;
  vector<int> d;
  for (it = fset.begin(); it != fset.end(); ++it) {
    d.push_back(*it);
  }

  int mask = 1 << (d.size());

  for (int msk = 1; msk < mask; ++msk) {
    int cf = 1;
    for (int j = 0; j < d.size(); ++j) {
      if (msk & (1 << j)) {
        cf *= d[j];
      }
    }

    if (__builtin_popcount(msk) % 2) {
      sol -= (n - 1) / cf;
    } else {
      sol += (n - 1) / cf;
    }
  }

  return sol;
}


int main() {
  sieve();

  /*
  int tnum;
  while (cin >> tnum) {
    cout << "phi(" << tnum << ") = ";
    cout << phi(tnum) << endl;
  }
  */

  double val = 0;
  int sol = -1;

  for (int i = 2; i < 1000000; ++i) {
    double ratio = (double) i / (double)phi(i);
    //cout << i << " " << ratio << endl;
    if (ratio > val) {
      val = ratio;
      sol = i;
    }
  }
  cout << sol << " " << val << endl;

  return 0;
}
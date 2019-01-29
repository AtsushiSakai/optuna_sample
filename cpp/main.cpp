#include <iostream>
using namespace std;

double himmelblau_function(double x, double y) {
  double t1 = (x * x + y - 11.0);
  double t2 = (x + y * y - 7.0);
  return t1 * t1 + t2 * t2;
}

int main(int argc, char* argv[]) {
  if (argc >= 3) {
    double x = std::stod(argv[1]);
    double y = std::stod(argv[2]);
    double ans = himmelblau_function(x, y);
    cout << ans << endl;
  }
}


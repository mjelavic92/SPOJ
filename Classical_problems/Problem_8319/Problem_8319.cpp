#include <iostream>
#include <list>
#include <stdlib.h>
using namespace std;

// main() is where program execution begins.
int main() {


   int a;
   int sum = 0;
   for (int i = 0; i < 10; i++) {
    cin >> a;
    if (abs(sum - 100) >= abs(sum + a - 100)) {
        sum+=a;
    }
   }
   cout << sum;

   return 0;
}

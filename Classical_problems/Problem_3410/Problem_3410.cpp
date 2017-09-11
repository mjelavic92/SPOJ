#include <iostream>
#include <list>
using namespace std;

// main() is where program execution begins.
int main() {

   list<int> lista;
   list<int>::iterator it;
   int a;
   cin >> a; // prints Hello World
   while(a!=0){
    int sumSquares = 0;
    for(int i = 0; i < a+1; i++){
        it = lista.begin();
        
        sumSquares+=i*i;
        it++;
    }
    lista.insert(lista.end(), sumSquares);
    cin >> a;
    }
   for (it=lista.begin(); it!=lista.end(); ++it){
    cout << *it;
    cout << "\n";
    }

   return 0;
}

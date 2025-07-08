#include <iostream>

#define LIMITE 10 

using namespace std;

int main() {
    int numero;

    cout << "Ingrese un número para mostrar su tabla de multiplicar: ";
    cin >> numero;

    cout << "\nTabla de multiplicar del " << numero << " hasta " << LIMITE << ":" << endl;
    for (int i = 1; i <= LIMITE; i++) {
        cout << numero << " x " << i << " = " << numero * i << endl;
    }

    return 0;
}
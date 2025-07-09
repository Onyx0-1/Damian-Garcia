#include <iostream>
using namespace std;

void modificarPorValor(int numero) {
    numero += 10;
    cout << "Dentro de modificarPorValor, numero = " << numero << endl;
}

void modificarPorReferencia(int& numero) {
    numero += 10;
    cout << "Dentro de modificarPorReferencia, numero = " << numero << endl;
}

int main() {
    int numero = 20;

    cout << "Valor inicial de numero: " << numero << endl;

    modificarPorValor(numero);
    cout << "Después de modificarPorValor, numero = " << numero << endl;

    modificarPorReferencia(numero);
    cout << "Después de modificarPorReferencia, numero = " << numero << endl;

    return 0;
}
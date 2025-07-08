#include <iostream>

using namespace std;

int main() {
    int numeroSecreto = 42;
    int intento;

    cout << "Bienvenido al juego de adivinanza" << endl;

    while (true) {
        cout << "Adivina el número secreto: ";
        cin >> intento;

        if (intento == numeroSecreto) {
            cout << "Adivinaste el numero." << endl;
            break;
        } else if (intento < numeroSecreto) {
            cout << "Demasiado bajo. Intenta con un numero mas alto." << endl;
        } else {
            cout << "Demasiado alto. Intenta con un numero mas bajo." << endl;
        }
    }

    return 0;
}
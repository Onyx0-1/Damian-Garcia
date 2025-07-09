#include <iostream>
using namespace std;

int main() {
    int opcion;

    do {
        cout << "MENÚ PRINCIPAL" << endl;
        cout << "1. Saludar" << endl;
        cout << "2. Despedirse" << endl;
        cout << "3. Salir" << endl;
        cout << "Seleccione una opción: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                cout << "Que fue chamo :D" << endl;
                break;
            case 2:
                cout << "Chao manito :v" << endl;
                break;
            case 3:
                cout << "Saliste del programa" << endl;
                break;
       
        }
    } while (opcion != 3); 

    return 0;
}
#include <iostream>
#include <cmath> // Librería para funciones matemáticas

using namespace std;

int main() {
    double num1, num2;
    
    cout << "Ingrese el primer número: ";
    cin >> num1;

    cout << "Ingrese el segundo número: ";
    cin >> num2;

    cout << "\nResultados de las operaciones:" << endl;
    cout << "Suma: " << num1 + num2 << endl;
    cout << "Resta: " << num1 - num2 << endl;
    cout << "Multiplicación: " << num1 * num2 << endl;

    if (num2 != 0)
        cout << "División: " << num1 / num2 << endl;
    else
        cout << "División: Error - No se puede dividir por cero." << endl;

    cout << "\nOperaciones con la librería <cmath>:" << endl;
    cout << "Potencia (" << num1 << "^" << num2 << "): " << pow(num1, num2) << endl;

    if (num1 >= 0)
        cout << "Raíz cuadrada del primer número: " << sqrt(num1) << endl;
    else
        cout << "Raíz cuadrada: Error - No se puede calcular la raíz de un número negativo." << endl;

    return 0;
}
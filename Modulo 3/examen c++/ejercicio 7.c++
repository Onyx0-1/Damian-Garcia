#include <iostream>
using namespace std;

float calcularAreaRectangulo(float base, float altura);

int main() {
    float base, altura;

    cout << "Ingrese la base del rectángulo: ";
    cin >> base;

    cout << "Ingrese la altura del rectángulo: ";
    cin >> altura;

    float area = calcularAreaRectangulo(base, altura);

    cout << "El área del rectángulo es: " << area << endl;

    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    return base * altura;
}
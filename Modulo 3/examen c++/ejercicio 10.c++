#include <iostream>
using namespace std;

const double pi = 3.14;

void calcularPerimetro(double radio);

int main() {
    double radio;

    cout << "Dame el radio del circulo: ";
    cin >> radio;

    calcularPerimetro(radio);

    return 0;
}

void calcularPerimetro(double radio) {
    double perimetro = 2 * pi * radio;
    cout << "El perimetro del circulo es: " << perimetro << endl;
}
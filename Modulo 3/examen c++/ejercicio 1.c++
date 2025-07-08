#include <iostream> 

int main(){
    std::cout << "hoola mundo" <<std::endl;
    
    int numeroEntero = 10;
    std::cout << "Entero: " << numeroEntero << std::endl;
     float numeroDecimalCorto = 9.81f;
    std::cout << "Float: " << numeroDecimalCorto << std::endl;
    char letra = 'A';
    std::cout << "Char: " << letra << std::endl;
     bool esVerdadero = true;
    std::cout << "Bool (true): " << esVerdadero << std::endl;
    esVerdadero = false;
    std::cout << "Bool (false): " << esVerdadero << std::endl;


    int edad; 
    std::cout << "Introduce tu edad";
    
    std::cin >> edad;
    
    std::cout << "tienes " << edad << " años. " << std::endl;
    return 0;
}
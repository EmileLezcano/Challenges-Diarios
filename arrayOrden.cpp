#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    /* Declaramos e inicializamos un array de 5 enteros. */

    int numeros[5] = {3,4,2,5,1};

    /*Recorremos el array usando un bucle for basado en rango (C++11 en adelante)*/
    
    for (int numero : numeros){
        cout << numero << " ";
    }

    /*Imprimimos el contenido del array*/
    
    cout << "Array original";
    cout << endl;

    /* Utilizamos en metodo sort para ordenar el contenido del array */
    sort(begin(numeros), end(numeros));

    /*Recorremos el array usando un bucle for basado en rango (C++11 en adelante)*/

    for (int numero : numeros){
        cout << numero << " ";
    }

    /*Imprimimos el contenido del array*/
    cout << "Array ordenado";
    cout << endl;
    
    

    return 0;
}

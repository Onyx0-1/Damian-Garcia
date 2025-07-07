<?php
$sumaImpares = 0;

for ($i = 1; $i <= 100; $i += 2) {
    $sumaImpares += $i;
}

echo "La suma de los numeros impares del 1 al 100 es: $sumaImpares\n";
?>
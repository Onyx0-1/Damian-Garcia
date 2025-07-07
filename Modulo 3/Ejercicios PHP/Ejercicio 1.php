<?php
$pares = 0;
$impares = 0;

for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 == 0) {
        $pares++;
    } else {
        $impares++;
    }
}

echo "Cantidad de numeros pares entre 1 y 50: $pares\n";
echo "Cantidad de numeros impares entre 1 y 50: $impares\n";
?>
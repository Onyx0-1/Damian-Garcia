<?php


$metodopago = "transferencia";
switch ($metodopago) {
    case 'pago movil': 
        echo "Datos del pago movil: 31194277, 04146067604, Ivan Torrealba, BDV";
        break;
    case 'tranferencia':
        echo "datos: 0134559986230598, 90876555, Banesco";

    default: 
        
        break;
}

?>
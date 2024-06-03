function limpiar(){
    document.getElementsByClassName('.formulario').reset();
}

function sumar(){
    var num1 = parseInt(document.getElementById('valor1').value);
    var num2 = parseInt(document.getElementById('valor2').value);
    //alert(num1+num2);
    document.getElementById('resultado').innerHTML = num1+num2;
}

function restar(){
    var num1 = parseInt(document.getElementById('valor1').value);
    var num2 = parseInt(document.getElementById('valor2').value);
    //alert(num1+num2);
    document.getElementById('resultado').innerHTML = num1-num2;
}

function multiplicar(){
    var num1 = parseInt(document.getElementById('valor1').value);
    var num2 = parseInt(document.getElementById('valor2').value);
    //alert(num1+num2);
    document.getElementById('resultado').innerHTML = num1*num2;
}

function dividir(){
    var num1 = parseInt(document.getElementById('valor1').value);
    var num2 = parseInt(document.getElementById('valor2').value);
    //alert(num1+num2);
    document.getElementById('resultado').innerHTML = num1/num2;
}
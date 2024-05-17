const calcularSuma = () => {
  var num1 = parseFloat(document.getElementById('num1').value);
  var num2 = parseFloat(document.getElementById('num2').value);
  var resultado = num1 + num2;
  document.getElementById('resultado').innerHTML = "La suma es: " + resultado;
}

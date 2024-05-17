/**querySelector es un método que acepta el 
 * selector exacto del CSS en una cadena y 
 * retorna un elemento. Puedes usarlo para 
 * seleccionar los colores rojo y negro así 
 * como la tarjeta de imagen, usando sus nombres 
 * de clase. 
 * */
const redColor = document.querySelector(".red");
const blackColor = document.querySelector(".black");
const imageCard = document.querySelector(".product-image");
const feedbackBtn = document.querySelector(".feedback");

const grayColor = document.getElementsByClassName("gray");
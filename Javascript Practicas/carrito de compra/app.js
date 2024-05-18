/**querySelector 
 * es un método que acepta el 
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

/**
 * getElementsByClassName
 * Puedes usar este selector para seleccionar el color gris. Es muy similar 
 * al querySelector. La única diferencia es que este método acepta solo el 
 * nombre de la clase, sin el punto anterior (.)
 */
const grayColor = document.getElementsByClassName("gray");

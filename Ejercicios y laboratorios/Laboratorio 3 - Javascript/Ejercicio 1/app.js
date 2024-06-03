
const formulario = document.getElementById("miFormulario");

formulario.addEventListener("submit", function(event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    const nombre = document.getElementById("nombre").value;
    const email = document.getElementById("email").value;
    const precio = document.getElementById("precio").value;

    // Validación de campos
    if (!/^[a-zA-ZÀ-ÿ\s]{1,40}$/.test(nombre)) {
        alert("Por favor, ingresa tu nombre.");
        return;
    }

    if (!/^[\w.-]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,}$/.test(email)) {
        alert("Por favor, ingresa un correo electrónico válido.");
        return;
    }

    if (isNaN(precio) || parseFloat(precio) <= 0) {
        alert("Por favor, ingresa un precio válido.");
        return;
    }
    
    alert("Formulario enviado correctamente.");
    
});
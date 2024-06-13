const user = JSON.parse(localStorage.getItem('login_success')) || false
if (!user) {
    window.location.href = 'login.html'
}

const logout = document.querySelector('#logout')

logout.addEventListener('click', () => {
    alert('Hasta pronto!')
    localStorage.removeItem('login_success')
    window.location.href = 'login.html'
})


const url='http://127.0.0.1:5000/clientes'

const formulario = document.querySelector('#formulario');
formulario.addEventListener('submit', validarFormulario);

function validarFormulario(e){
    e.preventDefault()

    const Nombre = document.querySelector('#nombres').value;
    const apellidos= document.querySelector('#apellido').value;
    const empresa = document.querySelector('#empresa').value;
    const puesto = document.querySelector('#puesto').value;
    const CP = document.querySelector('#cp').value;
    const provincia = document.querySelector('#provincia').value;
    const telefono = document.querySelector('#telefono').value;
    const fechaNacimiento = document.querySelector('#fechaNacimiento').value;

    const data={
        Nombre,
        apellidos,
        empresa,
        puesto,
        CP,
        provincia,
        telefono,
        fechaNacimiento
    }

    console.log(data)
    fetch('http://127.0.0.1:5000/clientes',{
        method:'POST',
        body:JSON.stringify(data),
        headers:{
            'Content-Type':'application/json'
        }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));
    formulario.reset();
}
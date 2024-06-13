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



let url = 'http://127.0.0.1:5000/clientes';
fetch(url)
    .then(response => response.json())
    .then(data => mostrarData(data))
    .catch(error => console.log(error))

//creamos la funcion mostrarData
const mostrarData = (data) => {
    console.log(data.clientes)
    let body = ''
    //let clientes = data.clientes;

    data.clientes.forEach(row => {
        body += `
            <tr><td>${row.codCliente}</td><td>${row.Nombre}</td><td>${row.apellidos}</td><td>${row.empresa}</td><td>${row.puesto}</td><td>${row.CP}</td><td>${row.provincia}</td><td>${row.telefono}</td><td>${row.fechaNacimiento}</td><td><button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@mdo">Editar</button></td><td><button type="button" class="btn btn-danger">Eliminar</button></td></tr>`
    });


    //for(let i = 0 ; i<data.clientes.length; i++){
    //    body+=`
    //   <tr><td>${data.codArticulo}</td><td>${data.Nombre}</td><td>${data.Descripcion}</td><td>${data.imagen}</td><td>${data.precioUnidad}</td><td>${data.stockSeguridad}</td><td>${data.unidadesStock}</td></tr>`
    //}
    document.getElementById('data').innerHTML = body
}

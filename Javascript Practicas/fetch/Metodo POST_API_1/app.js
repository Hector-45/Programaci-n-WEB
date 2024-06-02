// const formulario = document.querySelector('.formulario');

// formulario.addEventListener('submit',evento =>{
//     evento.preventDefault();

//     // const nombre = document.getElementById('nombre').value;
//     // const contrasena = document.getElementById('password').value;
  
//     // // Crear objeto con los datos del formulario
//     // const data = {
//     //   nombre,
//     //   contrasena
//     // };

//     const formData = new FormData(formulario);
//     //Mostrara en la consola el nombre ingresado en el formulario 
//     console.log(formData.get('nombre'));

//     const data = Object.fromEntries(formData);

//     console.log(data)

//     fetch('http://127.0.0.1:5000/usuarios',{
//         method:'POST',
//         headers:{
//             'Content-Type':'application/json'
//         },
//         body:JSON.stringify(data)
//     }).then(response => response.json())
//       .then(data => console.log(data))
//       .catch(error => console.log(error));
// });

// const formulario = document.querySelector('.formulario');
// formulario.addEventListener('submit', validarFormulario);

// function validarFormulario(event){
//     event.preventDefault();

//     const formData = new FormData(formulario);
//     const data = Object.fromEntries(formData);
//     const jsonData = JSON.stringify(data);

//     console.log(data)

//     fetch('http://127.0.0.1:5000/usuarios',{
//         method: 'POST',
//         headers:{
//             'Content-Type':'application/json'
//         },
//         body:jsonData
//     }
//     ).then(res => res.json())
//     .then(data => console.log(data))
//     .catch(error => console.log(error))
// }


const formulario = document.querySelector('#formulario');
formulario.addEventListener('submit',validarUsuario); 

 function validarUsuario(e){
    e.preventDefault()

    //const datosFormulario = new FormData(formulario)
    const nombre = document.querySelector('#nombre').value;
    const contrasena = document.querySelector('#contrasena').value;

    const data= {
        //"nombre":nombre,
        //"contrasena":contrasena
        nombre,
        contrasena
    }
    //const data = Object.fromEntries(datosFormulario)
    console.log(data)
    
    
    fetch('http://127.0.0.1:5000/usuarios',{
        method:'POST',
        body:JSON.stringify(data),
        headers:{
            'Content-Type':'application/json'
        }
    })
    .then(response => response.json())
    // .then(usuario =>{
    //     document.querySelector('#resultado').innerHTML=`
    //     Se resgistraron los datos en el servidor. <br>
    //     Nombre: ${usuario.nombre}</br>
    //     clave:${usuario.contrasena}
    //     `
    // })
    .then(data => console.log(data))
    .catch(error => console.log(error));
}
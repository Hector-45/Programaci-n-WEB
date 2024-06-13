const signupForm = document.querySelector('#signupForm')
signupForm.addEventListener('submit', (e)=>{
    e.preventDefault()
    const name = document.querySelector('#name').value
    const email = document.querySelector('#email').value
    const password = document.querySelector('#password').value

    //creando una variable que seria un array de objetos siendo
    //nuestra base de datos, va guardar los usuarios
    const Users = JSON.parse(localStorage.getItem('users')) || []
    const usuarioRegistrado = Users.find(user => user.email === email)
    if(usuarioRegistrado){
        return alert('El usuario ya esta registado!')
    }

    //Vamos a guardar el objeto
    Users.push({name: name, email: email, password: password})
    localStorage.setItem('users', JSON.stringify(Users))
    alert('Registro Exitoso!')
    //redireccion al login
    window.location.href = 'login.html'
})
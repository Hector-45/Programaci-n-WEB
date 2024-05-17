// Fetch API desde una API

const obtenerDatos = () =>  {
    fetch('https://picsum.photos/list?limit=100') 
        .then( respuesta => {
            return respuesta.json()
        }) 
        .then(resultado => {
            mostrarHTML(resultado);
            console.log(resultado)
        })
}

const mostrarHTML = (datos) => {
    
    const contenido = document.querySelector('#contenido');
    var tableHtml = `<table>
                <thead>
                    <tr>
                        <th>Autor</th>
                        <th>Imagen</th>
                    </tr>
                </thead>
                <tbody>`;
            
              datos.forEach(item => {
                tableHtml += `
                    <tr>
                        <td>${item.author}</td>
                        <td><a href="${item.post_url}" target="_blank">Ver Imagen</a></td>
                    </tr>`;
            });

            tableHtml += `</tbody></table>`;

    contenido.innerHTML = tableHtml;
    
}
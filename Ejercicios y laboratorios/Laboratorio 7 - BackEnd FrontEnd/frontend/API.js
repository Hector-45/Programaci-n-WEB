const url = 'http://127.0.0.1:5000/articulos';

export const nuevoArticulo = async articulos => {
    try {
        await fetch(url, {
            method: 'POST', 
            body: JSON.stringify(articulos), // data puede ser string o un objeto
            headers:{
              'Content-Type': 'application/json' // Y le decimos que los datos se enviaran como JSON
            }
        });
    } catch (error) {
        console.log(error);
    }
}
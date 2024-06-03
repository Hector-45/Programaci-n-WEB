/*const objCarrito = [
    {nombre: 'Monitor 20 pulgadas', precio: 500},
    {nombre: 'Television 20 pulgadas',precio: 700},
    {nombre: 'Table', precio: 300},
    {nombre: 'Audifonos', precio: 200},
    {nombre: 'Teclado', precio: 50},
    {nombre: 'Celular', precio: 500},
]

function obtenerPrecio(){
    return 
}

for(const iterador in objCarrito.precio){
    console.log(objCarrito.precio())
}*/

function Carrito() {
    const productos = [
        {nombre: 'Monitor 20 pulgadas', precio: 500},
        {nombre: 'Television 20 pulgadas',precio: 700},
        {nombre: 'Table', precio: 300},
        {nombre: 'Audifonos', precio: 200},
        {nombre: 'Teclado', precio: 50},
        {nombre: 'Celular', precio: 500},
    ];
    
    /*function agregarProducto(producto){
      productos.push(producto);
    }*/

    function mostrarDatos(){
        /*for(const iterador in productos){
            console.log(productos)
        }*/
        console.log(productos)
    }
    
    function obtenerPrecioTotal(){
      return productos.reduce((total, p) => total + p.precio, 0);
    }

    
    return {
     obtenerPrecioTotal,
     mostrarDatos
    }
  }
  //Instancia y llamada de funciones
  const carrito = Carrito();
  console.log(carrito.mostrarDatos());
  console.log("La suma total de los precios es: "+carrito.obtenerPrecioTotal());
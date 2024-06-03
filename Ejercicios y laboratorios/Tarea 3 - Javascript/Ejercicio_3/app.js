
const parrafo = document.querySelector('body');
const p = document.createElement('P');
parrafo.textContent = 'Etiqueta creada desde Javascript';
parrafo.style.color = "green";

parrafo.classList.add('nuevaClase');
const claseNueva = document.querySelector('.nuevaClase')
claseNueva.style.color = "red";

const buscarInput = document.getElementById('buscarInput');

function scrollAElemento(elemento) {
  elemento.scrollIntoView({ behavior: "smooth" });
}

function buscarElementoYMostrar() {
  const busqueda = buscarInput.value.toLowerCase();
  const elementos = document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, li, span, div');

  elementos.forEach(elemento => {
    const contenido = elemento.textContent.toLowerCase();
    if (contenido.includes(busqueda)) {
      scrollAElemento(elemento);
      return;
    }
  });
}

function manejarKeyPress(event) {
  if (event.key === 'Enter') {
    buscarElementoYMostrar();
  }
}

buscarInput.addEventListener('input', buscarElementoYMostrar);
buscarInput.addEventListener('keypress', manejarKeyPress);
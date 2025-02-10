document.addEventListener("DOMContentLoaded", function() {
  const botonValidar = document.querySelector("input[type='button']");
  const claveInput = document.getElementById("clave");
  const nivelSeguridadSpan = document.getElementById("nivel-seguridad");

  // Agregar evento input para evaluar seguridad mientras se escribe la contraseña
  claveInput.addEventListener("input", function() {
    const nivelSeguridad = obtenerNivelSeguridad(claveInput.value);
    if (nivelSeguridad < 3) {
      nivelSeguridadSpan.textContent = "Débil";
      nivelSeguridadSpan.style.color = "red"; // Establecer el color rojo para "Débil"
    } else {
      nivelSeguridadSpan.textContent = "Fuerte";
      nivelSeguridadSpan.style.color = "green"; // Establecer el color verde para "Fuerte"
    }
  });  

  botonValidar.addEventListener("click", function() {
    const edadInput = document.querySelector("input[type='number']");
    const checkboxAutorizar = document.querySelector("input[type='checkbox']");

    const edad = parseInt(edadInput.value);
    const esMayorDeEdad = edad >= 18;
    const estaAutorizado = checkboxAutorizar.checked;
    const nivelSeguridad = obtenerNivelSeguridad(claveInput.value);

    if (!esMayorDeEdad || !estaAutorizado || nivelSeguridad < 3) {
      if (!esMayorDeEdad && !estaAutorizado) {
        alert("Debes tener más de 18 años y autorizar el uso de datos.");
      } else if (!esMayorDeEdad) {
        alert("Debes tener más de 18 años.");
      } else if (!estaAutorizado) {
        alert("Debes autorizar el uso de datos.");
      }
    } else {
      alert("Formulario válido. Enviando datos al servidor...");
      // Código DB
    }
  });

  function obtenerNivelSeguridad(clave) {
    return clave.length >= 8 ? 3 : 1;
  }
});
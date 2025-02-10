// Función para validar la contraseña
function validarContraseña() {
    var contraseña = document.getElementById("id_Contraseña").value;
    var mensaje = document.getElementById("message");
    var expresionRegular = /^(?=.*[A-Z])(?=.*\d).{6,}$/;

    if (!contraseña.match(expresionRegular)) {
        mensaje.innerHTML = "Seguridad baja";
        mensaje.style.color = "red";
    } else if (contraseña.length >= 6 && contraseña.length < 8) {
        mensaje.innerHTML = "Seguridad media";
        mensaje.style.color = "orange";
    } else {
        mensaje.innerHTML = "Seguridad alta";
        mensaje.style.color = "green";
    }
}

// Agregar un event listener al campo de contraseña
document.getElementById("id_Contraseña").addEventListener("keyup", validarContraseña);
// Lista de nombres y contraseñas válidos
const usuariosValidos = [
    { nombre: "daniel", contrasenia: "12345" },
    { nombre: "alejandro", contrasenia: "abcde" },
    { nombre: "messi", contrasenia: "ronaldo" },
  ];
  
  document.getElementById('validarButton').addEventListener('click', function () {
    const nombreInput = document.getElementById('nombreInput').value.trim();
    const contraseniaInput = document.getElementById('contraseniaInput').value.trim();
  
    // Buscar el usuario ingresado en la lista de usuarios válidos
    const usuarioValido = usuariosValidos.find(usuario => usuario.nombre === nombreInput && usuario.contrasenia === contraseniaInput);
  
    if (usuarioValido) {
      alert('¡Usuario válido! Acceso permitido.');
    } else {
      alert('Usuario no válido o contraseña incorrecta. Acceso denegado.');
    }
  });
  
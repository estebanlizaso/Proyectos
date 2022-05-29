document.getElementById("reserva").addEventListener('submit', validarReserva);

function validarReserva(evento){
    evento.preventDefault();
    var nombre = document.getElementById("nombre").value;
    if (nombre.length == 0) {
        alert('Por favor, escriba su nombre')
        document.reserva.nombre.focus();
        return;
    }

    var email = document.getElementById("email").value;


    var personas = document.getElementById("personas").value;
    if (0 < personas) {
        alert('La cantidad de personas asitentes debe ser mayor a 1')
        document.reserva.personas.focus();
        return
    } else if (personas > 12) {
        alert('La cantidad de personas que ha marcado supera la capacidad de nuestro local. Por favor pongáse en contacto con nosotros por teléfono o mail para que podamos ofrecerle alguna otra opción acorde a sus necesidades.')
        return
    }
}
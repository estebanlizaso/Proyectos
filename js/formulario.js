document.addEventListener("DOMContentLoaded",function(){document.getElementById("reserva").addEventListener('submit', validarReserva);})

function validarReserva(evento){
    evento.preventDefault();
    var nombre = document.getElementById("nombre").value;
    if (nombre.length == 0) {
        alert('Por favor, escriba su nombre')
        document.reserva.nombre.focus();
        return;
    }

    var email = document.getElementById("email").value;
    if (email.length == 0) {
        alert('Por favor, ingrese un email de contacto.')
        document.reserva.email.focus();
        return;
    }

    var telefono = document.getElementById("telefono").value;
    if (telefono.length == 0) {
        alert('Por favor, ingrese un teléfono de contacto.')
        document.reserva.telefono.focus();
        return;
    } else if (isNaN(parseInt(telefono))){
        alert('Por favor, ingrese un teléfono válido.')
        document.reserva.telefono.focus();
        return;
    }
    
    var personas = document.getElementById("personas").value;
    if (personas < 1) {
        alert('La cantidad de personas asitentes debe ser mayor a 1')
        document.reserva.personas.focus();
        return;
    } else if (personas > 50) {
        alert('La cantidad de personas que ha marcado supera la capacidad de nuestro local. Por favor pongáse en contacto con nosotros por teléfono o mail para que podamos ofrecerle alguna otra opción acorde a sus necesidades.')
        return;
    }

    var fecha = document.getElementById("fecha").value;
    var dia = new Date(fecha).getDay();
    if (fecha.length == 0) {
        alert('Debe seleccionar un día para la reserva.')
        document.reserva.fecha.focus();
        return;
    } else if (dia == 6) {
        alert('Los domingos La Taberna de Marduk se encuentra cerrada. Debe seleccionar otro día.')
        document.reserva.fecha.focus();
        return;
    }

    var hora = document.getElementById("hora").value;
    //if 





    alert("Muchas gracias por su reserva.")
    this.submit();
}
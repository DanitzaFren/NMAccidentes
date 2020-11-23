
$("#btn1").click(function(){
    Swal.fire({
        icon: 'error',
        title: 'Algo salio mal...',
        text: 'No tiene privilegios para administrar este sitio',
        footer: '<a href="/servicios" >¿Volver a la seccion de servicios?</a>'
    });
});


$("#btn2").click(function(){
    Swal.fire({
        icon: 'error',
        title: 'Algo salio mal...',
        text: 'No tiene privilegios para administrar este sitio o no ha iniciado sesion',
        footer: '<a href="/accounts/login/" >¿Desea iniciar sesion?</a>'
    });
});


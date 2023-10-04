var contenedor = $('#caja');

var anterior = $('#btn-adelante');
var siguiente = $('#btn-atras');

$('#caja .section_caja:last').insertBefore
('#caja .section_caja:firs');

contenedor.css('margin-left','-'+100+'%');

function derecha(){
    contenedor.animate({
        marginleft: '-'+200+'%'
    } ,700, function(){
        $('#caja .section_caja:firs').insertAfter
        ('#caja .section_caja:last');
        contenedor.css('margin-left','-'+100+'%');
    });
}

function izquierda(){
    contenedor.animate({
        marginleft: 0
    } ,700, function(){
        $('#caja .section_caja:last').insertBefore
        ('#caja .section_caja:firs');
        contenedor.css('margin-left','-'+100+'%');
    });
}

// funcion  para mover la imagenes automaticamente a la derecha cada 5 segundos

function automatico(){
    interval = setInterval(function(){
        derecha();
    }, 5000);
}

// funcion para mover las imagenes a la derecha a traves del boton 

siguiente.on('click',function(){
    derecha();
    clearInterval(interval);
    automatico();
});

// funcion para mover las imagenes a la izquierda a traves del boton 

siguiente.on('click',function(){
    izquierda();
    clearInterval(interval);
    automatico();
});

// ejecucion automatica
automatico();

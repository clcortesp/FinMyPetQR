function eliminarMascota(){
    var idMascota = document.getElementById('mascota_id');    
    Swal.fire({
        "title" :"¿Estas seguro?",
        "text": "esta acción no se puede deshacer",
        "icon": "question",
        "showCancelButton":true,
        "cancelButtonText": "No, Cancelar",
        "confirmButtonText":"Si, Eliminar",
        "reverseButtons": true,
        "confirmButtonColor":"#dc3545"
    })
    .then(function(result){
        if(result.isConfirmed){
            window.location.href = "/deletePet/"+idMascota.value+"/"
        }
    })
}
function declararPerdida(){

    var idMascota = document.getElementById('mascota_id');
    Swal.fire({
        "title" :"¿Estas seguro?",
        "text": "vas a declarar a tu mascota como perdida",
        "icon": "question",
        "showCancelButton":true,
        "cancelButtonText": "No, Cancelar",
        "confirmButtonText":"Si, Declarar",
        "reverseButtons": true,
        "confirmButtonColor":"#dc3545"
    })
    .then(function(result){
        if(result.isConfirmed){
            window.location.href = "/reportar_perdida/"+idMascota.value+"/"
        }
    })
}

function declararEncontrada(){
    var idMascota = document.getElementById('mascota_id')
    Swal.fire({
        "title" :"¿Estas seguro?",
        "text": "vas a declarar a tu mascota como encontrada",
        "icon": "question",
        "showCancelButton":true,
        "cancelButtonText": "No, Cancelar",
        "confirmButtonText":"Si, Declarar",
        "reverseButtons": true,
        "confirmButtonColor":"#dc3545"
    })
    .then(function(result){
        if(result.isConfirmed){
            window.location.href = "/reportar_encontrada/"+idMascota.value+"/"
        }
    })
}
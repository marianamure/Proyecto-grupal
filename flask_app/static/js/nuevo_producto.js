var formulario = document.getElementById('nuevo_producto_js');
formulario.onsubmit = function(e){
    e.preventDefault();
    var formData = new FormData(formulario)
    fetch("/crear_producto", {method: 'POST', body: formData})
    .then(response => response.json())
    .then(data => {
        if (data.message == 'Correcto'){
            window.location.href = '/perfil_cultivador';
        }
        var alertMessage = document.getElementById('alertMessage');
        alertMessage.innerText = data.message;
        alertMessage.classList.add('alert');
        alertMessage.classList.add('alert-danger');
    })
}

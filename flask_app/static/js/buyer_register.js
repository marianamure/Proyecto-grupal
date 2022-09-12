var formulario = document.getElementById('buyer_registrer_js');
formulario.onsubmit = function(e){
    e.preventDefault();
    var formData = new FormData(formulario)
    fetch("/registro_comprador", {method: 'POST', body: formData})
    .then(response => response.json())
    .then(data => {
        if (data.message == 'Correcto'){
            window.location.href = '/muro_comprador';
        }
        var alertMessage = document.getElementById('alertMessage');
        alertMessage.innerText = data.message;
        alertMessage.classList.add('alert');
        alertMessage.classList.add('alert-danger');
    })
}



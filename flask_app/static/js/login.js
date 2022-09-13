var formulario = document.getElementById('login_js');
formulario.onsubmit = function(e){
    e.preventDefault();
    var formData = new FormData(formulario)
    fetch("/login", {method: 'POST', body: formData})
    .then(response => response.json())
    .then(data => {

        if (data.message == 'Correcto'){
            window.location.href = '/perfil_cultivador';
            console.log(data.message)
        }
        else if (data.message == 'Correcto1'){
            window.location.href = '/muro_comprador';
            console.log(data.message)
        }
        var alertMessage = document.getElementById('alertMessage');
        alertMessage.innerText = data.message;
        alertMessage.classList.add('alert');
        alertMessage.classList.add('alert-danger');
    })
}



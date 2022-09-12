var formulario = document.getElementById('login_js');
formulario.onsubmit = function(e){
    e.preventDefault();
    var formData = new FormData(formulario)
    fetch("/login", {method: 'POST', body: formData})
    .then(response => response.json())
    .then(data => {
        if (data.message == 'Correcto'){
            window.location.href = '/perfil_cultivador';
        }
        else (data.message == 'Correcto1');{
            window.location.href = '/muro_comprador';
        }
        var alertMessage = document.getElementById('alertMessage');
        alertMessage.innerText = data.message;
        alertMessage.classList.add('alert');
        alertMessage.classList.add('alert-danger');
    })
}


/*var formulario1 = document.getElementById('login_js');
formulario1.onsubmit = function(ev){
    ev.preventDefault();
    var formData1 = new FormData(formulario1)
    fetch("/login", {method: 'POST', body: formData1})
    .then(response1 => response1.json())
    .then(data1 => {
        if (data1.message1 == 'Correcto1'){
            window.location.href = '/muro_comprador';
        }
        var alertMessage1 = document.getElementById('alertMessage');
        alertMessage1.innerText = data1.message1;
        alertMessage1.classList.add('alert');
        alertMessage1.classList.add('alert-danger');
    })
}
*/

from flask import render_template, redirect, session, request, jsonify
from flask_app import app


from flask_app.models.cultivators import Cultivator
from flask_app.models.crops import Crop


@app.route('/muro_cultivador')
def muro_cultivador():
    if 'cultivator_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['cultivator_id']
    }

    cultivator = Cultivator.get_by_id(formulario) #Usuario que inicio sesión
    crop = Crop.get_crops()

    return render_template('muro_cultivador.html', cultivator=cultivator)

@app.route('/send_comment', methods=['POST'])
def send_comentario():
    if 'user_id' not in session:
        return redirect('/')
    
    #Guardar el mensaje. request.form = Diccionario con todos los campos del formulario
    Comentario.save(request.form)
    return redirect('/view/publicacion/'+request.form["publicacion_id"])
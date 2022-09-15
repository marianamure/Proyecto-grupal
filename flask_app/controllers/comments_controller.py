from flask import render_template, redirect, session, request, jsonify
from flask_app import app


from flask_app.models.cultivators import Cultivator
from flask_app.models.crops import Crop
from flask_app.models.comments import Comment



@app.route('/muro_cultivador')
def muro_cultivador():
    if 'cultivator_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['cultivator_id']
    }
    
    cultivator = Cultivator.get_by_id(formulario) #Usuario que inicio sesión
    crops = Crop.all()
    comments = Comment.get_cultivators_wall(formulario)
    cultivators = Cultivator.get_all()

    return render_template('muro_cultivador.html', cultivator=cultivator, crops=crops, comments = comments,cultivators=cultivators)

@app.route('/send_comment', methods=['POST'])
def send_comentario():
    if 'cultivator_id' not in session:
        return redirect('/')
    
    #Guardar el mensaje. request.form = Diccionario con todos los campos del formulario
    Comment.save(request.form)
    return redirect('/muro_cultivador')
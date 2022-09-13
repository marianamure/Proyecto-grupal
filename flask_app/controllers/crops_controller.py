from flask import render_template, redirect, session, request, flash
from flask_app import app


from flask_app.models.cultivators import Cultivator
from flask_app.models.crops import Crop
from werkzeug.utils import secure_filename
import os

@app.route('/nuevo_dato')
def nuevo_dato():
    if 'cultivator_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['cultivator_id']
    }

    cultivator = Cultivator.get_by_id(formulario) #Usuario que inicio sesión

    return render_template('nuevo_dato.html', cultivator=cultivator)

@app.route('/crear_dato', methods=['POST'])
def crear_dato():
    if 'cultivador_id' not in session: 
        return redirect('/')

    if not Crop.valida_crop(request.form):  
        return redirect('/nuevo_dato')

    if 'image' not in request.files:
        flash('Imagen no encontrada', 'crop')
        return redirect('/nuevo_dato')

    image = request.files['imagen']

    if image.filename == "":
        flash ('Nombre de imagen vacía', 'crop')
        return redirect ('/nuevo_dato')

    name_image = secure_filename(image.filename) 
    image.save(os.path.join(app.config ['UPLOAD_FOLDER'],name_image)) 
    
    formulario = {
        'farm' : request.form['farm'],
        'state' : request.form['state'],
        'municipality' : request.form['municipality'],
        'fertilizer' : request.form['fertilizer'],
        'f_amount' : request.form['f_amount'],
        'date' : request.form['date'],
        'disease' : request.form['disease'],
        'production' : request.form['production'],
        'description' : request.form['description'],
        'image' : name_image,
        'share' : request.form['share'],
        'cultivators_id' : request.form['cultivators_id'],
    }
    crop = Crop.save(formulario)

    return redirect('/mi_perfil_cultivador', crop = crop)
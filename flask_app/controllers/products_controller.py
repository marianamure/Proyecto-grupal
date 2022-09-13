from flask import render_template, redirect, session, request, flash
from flask_app import app


from flask_app.models.cultivators import Cultivator
from flask_app.models.crops import Crop
from flask_app.models.products import Product
from werkzeug.utils import secure_filename
import os

@app.route('/nuevo_producto')
def nuevo_producto():
    if 'cultivator_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['cultivator_id']
    }

    cultivator = Cultivator.get_by_id(formulario) #Usuario que inicio sesión

    return render_template('nuevo_producto.html', cultivator=cultivator)

@app.route('/crear_producto', methods=['POST'])
def crear_producto():
#    if 'cultivador_id' not in session: 
#        return redirect('/')

#    if not Crop.valida_crop(request.form):  
#        return redirect('/nuevo_dato')

    if 'image' not in request.files:
        flash('Imagen no encontrada', 'product')
        return redirect('/nuevo_producto')

    image = request.files['image']

    if image.filename == "":
        flash ('Nombre de imagen vacía', 'product')
        return redirect ('/nuevo_producto')

    name_image = secure_filename(image.filename) 
    image.save(os.path.join(app.config ['UPLOAD_FOLDER'],name_image)) 
    
    formulario = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'p_sale' : request.form['p_sale'],
        'presentation' : request.form['presentation'],
        'price' : request.form['price'],
        'image' : name_image,
        'cultivators_id' : request.form['cultivators_id'],
    }
    Product.save(formulario)

    return redirect('/perfil_cultivador')

"""@app.route('/update/crop/<int:id>') 
def update_crop(id):
#    if 'cultivator_id' not in session: 
#        return redirect('/')

    formulario = {
        'id': session['cultivator_id']
    }

    cultivator = Cultivator.get_by_id(formulario) 

    
    formulario_crop = {"id": id}
    crop = Crop.get_by_id(formulario_crop )

    return render_template('edita_dato.html', cultivator=cultivator, crop=crop)

@app.route('/update/data', methods=['POST'])
def update_data():
#    if 'cultivator_id' not in session: 
#        return redirect('/')
    
#    if not Publicacion.valida_publicacion(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
#        return redirect('/editar/publicacion/'+request.form['id'])

    name_image = ''
    
    if 'image' in request.files:
        image = request.files['image']

        if image.filename != "":
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
        'id': request.form['id']
    }

    Crop.update(formulario)
    return redirect('/perfil_cultivador')

@app.route('/delete/crop/<int:id>') #En mi URL voy a obtener ID
def delete_crop(id):
#    if 'cultivator_id' not in session: #Solo puede ver la página si ya inició sesión 
#        return redirect('/')

    formulario = {"id": id}
    Crop.delete(formulario)
#    Crop.delete2(formulario)
    
    return redirect('/perfil_cultivador')"""
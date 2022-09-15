from flask import render_template, redirect, session, request, jsonify
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
    if 'cultivator_id' not in session: 
        return redirect('/')

    validacion = Product.valida_products(request.form)  
    if not validacion[0]: 
        return jsonify(message=validacion[1][0])

    
    if 'image' not in request.files:
        return jsonify(message="Imagen no encontrada")

    image = request.files['image']

    if image.filename == '':
        return jsonify(message="Nombre de imagen vacío")

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

    return jsonify(message="Correcto")

@app.route('/update/product/<int:id>') 
def update_product(id):
    if 'cultivator_id' not in session: 
        return redirect('/')

    formulario = {
        'id': session['cultivator_id']
    }

    cultivator = Cultivator.get_by_id(formulario) 

    
    formulario_product = {"id": id}
    product = Product.get_by_id(formulario_product )

    return render_template('edita_producto.html', cultivator=cultivator, product=product)

@app.route('/update/data/product', methods=['POST'])
def update_data_product():
    if 'cultivator_id' not in session: 
        return redirect('/')
    
#    if not Publicacion.valida_publicacion(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
#        return redirect('/editar/publicacion/'+request.form['id'])

    validacion = Product.valida_products(request.form)  
    if not validacion[0]: 
        return jsonify(message=validacion[1][0])

    
    if 'image' not in request.files:
        return jsonify(message="Imagen no encontrada")

    image = request.files['image']

    if image.filename == '':
        return jsonify(message="Nombre de imagen vacío")

    name_image = secure_filename(image.filename) 
    image.save(os.path.join(app.config ['UPLOAD_FOLDER'],name_image)) 

    formulario = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'p_sale' : request.form['p_sale'],
        'presentation' : request.form['presentation'],
        'price' : request.form['price'],
        'image' : name_image,

        'id': request.form['product_id'],
    }


    Product.update(formulario)
    return jsonify(message="Correcto")

@app.route('/delete/product/<int:id>') #En mi URL voy a obtener ID
def delete_product(id):
#    if 'cultivator_id' not in session: #Solo puede ver la página si ya inició sesión 
#        return redirect('/')

    formulario = {"id": id}
    Product.delete(formulario)
#    Product.delete2(formulario)
    
    return redirect('/perfil_cultivador')





























































































































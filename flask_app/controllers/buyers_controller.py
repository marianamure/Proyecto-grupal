from email import message
from itertools import product
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

#Importación del modelo
from flask_app.models.buyers import Buyer
from flask_app.models.products import Product


#Importación BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#Pagina principal renderizando pagina comprador
@app.route('/registro_comprador/vista') 
def comprador():
    return render_template('registro_comprador.html')


#Guarda informacion del formulario con validacion jsonify
@app.route('/registro_comprador', methods=['POST'])
def registracomprador():
    #Validar la información ingresada
    validacion = Buyer.valida_comprador(request.form)
    if not validacion[0]: 
        return jsonify(message=validacion[1][0])
    #Aca se encripta la contraseña.
    pwd = bcrypt.generate_password_hash(request.form['password']) #Encriptamos el password del usuario

    #formulario que se va a estar comparando con el request.form 
    formulario = {
        'full_name': request.form['full_name'],
        'n_identification': request.form['n_identification'],
        'email': request.form['email'],
        'address': request.form['address'],
        'password': pwd,
        'type_buyer': request.form['type_buyer'],
    }

    #request.form = FORMULARIO HTML
    id = Buyer.save(formulario) #Recibo el identificador de mi nuevo usuario

    session['user_id'] = id #Se guarda en sesion el id de usuario.

    return jsonify(message="Correcto") #Se retorna

@app.route('/muro_comprador')
def vistamuro():

    if 'comprador_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['comprador_id']
    }

    comprador = Buyer.get_by_id(formulario)
    productos = Product.get_all_for_buyers()
    return render_template('muro_comprador.html', comprador = comprador, productos = productos)

@app.route('/comprar/<int:id>')
def agregar_producto_carrito(id):

    if 'comprador_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['comprador_id']
    }

    formulario_producto = {
        'id': id
    }

    comprador = Buyer.get_by_id(formulario)
    productos = Product.get_all_for_buyers()
    producto = Product.get_by_id(formulario_producto)

    #session['product_ids'].append(id)

    return render_template('carrito.html', comprador = comprador, productos = productos, producto = producto)

@app.route('/finalizar_compra')
def finalizar_compra():
    if 'comprador_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['comprador_id']
    }

    comprador = Buyer.get_by_id(formulario)

    # Metodo query guardar carro compra
    # Metodo query guardar información compra
    

    return render_template('compra.html', comprador = comprador)

@app.route('/registro_compra', methods=['POST'])
def registrar_compra():
    if 'comprador_id' not in session:
        return redirect('/')

    formulario = {
        'address': request.form['address'],
        'home_delivery': request.form['home_delivery'],
        'method_payment': request.form['method_payment'],
        'name_bank': request.form['name_bank'],
        'state': request.form['state']
    }

    Product.terminar_compra(formulario)

    return redirect('/muro_comprador')


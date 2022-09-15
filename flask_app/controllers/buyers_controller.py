from email import message
from itertools import product
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

#Importación del modelo
from flask_app.models.buyers import Buyer
from flask_app.models.products import Product
from flask_app.models.cultivators import Cultivator


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

    session['comprador_id'] = id #Se guarda en sesion el id de usuario.

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
    return render_template('muro_comprador.html', comprador = comprador, productos = productos  )

@app.route('/agregar_carritos', methods=['POST'])
def agregar_carrito():
    
    formulario = {
        'id': request.form['id']
    }

    producto_agregar = Product.get_by_id(formulario)

    if 'carrito' not in session:
        session['carrito'] = {}
        #print("creando carrito")
    #print(session['carrito'].keys())
    if 'total_carrito' not in session:
        session['total_carrito'] = 0

    if request.form['id']  not in session['carrito']:
        session['carrito'][request.form['id']] = 1
        session['total_carrito'] += int(producto_agregar.price)
    else:
        session['carrito'][request.form['id']] += 1
        session['total_carrito'] += int(producto_agregar.price)

    session.modified = True
    return redirect ('/muro_comprador')


@app.route('/compra')
def agregar_producto_carrito():

    if 'comprador_id' not in session:
        return redirect('/')

    if 'carrito' not in session:
        return redirect('/muro_comprador')

    formulario = {
        'id': session['comprador_id']
    }

    comprador = Buyer.get_by_id(formulario)
    productos = Product.get_all_for_buyers()
    
    ids_carrito = []
    for key in session['carrito'].keys():
        ids_carrito.append(int(key))
    print(ids_carrito)

    return render_template('carrito.html', comprador = comprador, productos = productos, ids_carrito = ids_carrito)

@app.route('/quitar_producto_carrito/<int:id>')
def quitar_producto_carrito(id):

    if 'comprador_id' not in session:
        return redirect('/')

    if 'carrito' not in session:
        return redirect('/muro_comprador')

    formulario = {
        'id': session['comprador_id']
    }

    comprador = Buyer.get_by_id(formulario)
    productos = Product.get_all_for_buyers()

    formulario_quitar = {
        'id': id
    }

    producto_quitar = Product.get_by_id(formulario_quitar)

    for times in range(session['carrito'][str(id)]):
        session['total_carrito'] -= int(producto_quitar.price)

    session['carrito'].pop(str(id))

    ids_carrito = []
    for key in session['carrito'].keys():
        ids_carrito.append(int(key))
    print(ids_carrito)

    return render_template('carrito.html', comprador = comprador, productos = productos, ids_carrito = ids_carrito, producto_quitar = producto_quitar)

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
        'address': request.form['domicilio'],
        'home_delivery': request.form['retirar'],
        'method_payment': request.form['transferencia'],
        'name_bank': request.form['banco'],
        'state': 'pending',
        'user_id' : session['comprador_id']
    }

    Product.terminar_compra(formulario)

    return redirect('/muro_comprador')


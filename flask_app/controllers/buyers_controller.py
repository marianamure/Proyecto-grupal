from email import message
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

#Importación del modelo
from flask_app.models.buyers import Buyer


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

    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    comprador = Buyer.get_by_id(formulario)
    return render_template('muro_comprador.html', comprador = comprador)
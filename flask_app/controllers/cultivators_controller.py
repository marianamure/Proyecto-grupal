from email import message
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

#Importación del modelo
from flask_app.models.buyers import Buyer
from flask_app.models.cultivators import Cultivator

#Importación BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#Pagina principal renderizando pagina cultivador
@app.route('/registro_cultivador/vista') 
def cultivador():
    return render_template('registro_cultivador.html')

#Guarda informacion del formulario con validacion jsonify
@app.route('/registro_cultivador', methods=['POST'])
def registracultivador():
    #Validar la información ingresada
    validacion = Cultivator.valida_cultivador(request.form) #voy aca
    if not validacion[0]: 
        return jsonify(message=validacion[1][0])
    #Aca se encripta la contraseña.
    pwd = bcrypt.generate_password_hash(request.form['password']) #Encriptamos el password del usuario

    #formulario que se va a estar comparando con el request.form 
    formulario = {
        'full_name': request.form['full_name'],
        'n_identification': request.form['n_identification'],
        'email': request.form['email'],
        'password': pwd,

    }

    #request.form = FORMULARIO HTML
    id = Cultivator.save(formulario) #Recibo el identificador de mi nuevo usuario

    session['user_id'] = id #Se guarda en sesion el id de usuario.

    return jsonify(message="Correcto") #Se retorna

@app.route('/perfil_cultivador')
def vistaperfil():

    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    cultivador = Cultivator.get_by_id(formulario)

    return render_template('mi_perfil_cultivador.html')

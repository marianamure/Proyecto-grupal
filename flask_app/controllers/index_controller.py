

from email import message
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

#Importación del modelo
from flask_app.models.buyers import Buyer
from flask_app.models.cultivators import Cultivator


#Importación BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/') #Pagina principal renderizando index
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    if request.form['user_type'] == 'Comprador':

        comprador = Buyer.get_by_email(request.form)
        if not comprador:
            #flash('E-mail no encontrado', 'login')
            #return redirect('/')
            return jsonify(message="E-mail no encontrado")

        if not bcrypt.check_password_hash(comprador.password, request.form['password']):
            
            return jsonify(message="Password incorrecto")
            #flash('Password incorrecto', 'login')
            #return redirect('/')

        session['user_id'] = comprador.id
        return jsonify(message="Correcto1")
    
    else:
        
        if request.form['user_type'] == 'Cultivador':
            cultivator = Cultivator.get_by_email(request.form) #Recibiendo una instancia de usuario o Falso

            if not cultivator:
                #flash('E-mail no encontrado', 'login')
                #return redirect('/')
                return jsonify(message="E-mail no encontrado")

            if not bcrypt.check_password_hash(cultivator.password, request.form['password']):
                
                return jsonify(message="Password incorrecto")
                #flash('Password incorrecto', 'login')
                #return redirect('/')

            session['user_id'] = cultivator.id
            return jsonify(message="Correcto")


    

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

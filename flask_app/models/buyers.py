from flask_app.config.mysqlconnection import  connectToMySQL

import re #Importando Expresiones regulares
#Expresion Regular de Email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class Buyer:

    def __init__(self, data):
        self.id = data['id']
        self.full_name = data['full_name']
        self.n_identification = data['n_identification']
        self.email = data['email']
        self.address = data['address']
        self.password = data['password']
        self.type_buyer = data['type_buyer']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO buyers (full_name, n_identification, email, address, password, type_buyer) VALUES (%(full_name)s, %(n_identification)s, %(email)s, %(address)s, %(password)s, %(type_buyer)s)"
        result = connectToMySQL('weedproject').query_db(query, formulario) 
        #me regresan el nuevo ID del comprador registrado
        #result = 5
        return result

    @staticmethod
    def valida_comprador(formulario): #El formulario es 
        #formulario = { DICCIONARIO
        #   first_name = "Elena",    
        #   last_name = "De Troya",    
        #   email = "elena@codingdojo.com",    
        #   password = "123",    
        #   confirm_password = "234",    
        #}

        es_valido = True #Siempre va ser true hasta que sea false por
        #la sentencia if.
        
        errores=[]

        #Validar que el nombre y el apellido no esten vacios
        if len(formulario['full_name']) < 3:
            #flash('Nombre completo o razon social debe tener un valor ingresado', 'comprador')
            errores.append('Nombre completo o razon social debe tener al menos 3 caracteres')
            es_valido = False

        if len(formulario['n_identification']) < 6:
            #flash('Numero de identificacion debe tener un valor ingresado', 'comprador')
            errores.append('Numero de identificacion debe tener al menos 6 caracteres')
            es_valido = False

        #Verificar que el email tenga formato correcto - EXPRESIONES REGULARES
        if not EMAIL_REGEX.match(formulario['email']):
            #flash('E-mail inválido', 'comprador')
            errores.append('E-mail inválido')
            es_valido = False
        
        #Password con al menos 8 caracteres
        if len(formulario['address']) < 4:
            #flash('Direccion debe tener al menos 8 caracteres', 'comprador')
            errores.append('Direccion debe tener al menos 4 caracteres')
            es_valido = False
        
        #Verificamos que las contraseñas coincidan
        if formulario['password'] != formulario['confirm_password']:
            #flash('Contraseñas no coinciden', 'comprador')
            errores.append('Contraseñas no coinciden')
            es_valido = False

        #Verificamos que tipo de comprador no este vacio
        if len(formulario['type_buyer']) < 3:
            #flash('Tipo de comprador no debe estar vacio', 'comprador')
            errores.append('Tipo de comprador no debe estar vacio')
            es_valido = False
        
        #Consultar si ya existe ese correo electrónico
        query = "SELECT * FROM buyers WHERE email = %(email)s"
        
        results = connectToMySQL('weedproject').query_db(query, formulario)
        print(results)
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'comprador')
            errores.append('E-mail registrado previamente')
            es_valido = False
        
        return (es_valido, errores)


    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM buyers WHERE email = %(email)s"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        #Los SELECT regresan una lista
        if len(result) < 1: #NO existe registro con ese correo
            #result = []
            return False
        else:
            user = cls(result[0])
            return user
    
    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM buyers WHERE id = %(id)s"
        result = connectToMySQL('weedproject').query_db(query, formulario) #RECIBIMOS UNA LISTA
        user = cls(result[0]) #creamos una instancia de usuario
        return user
    
   




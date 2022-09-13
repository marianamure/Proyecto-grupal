from flask_app.config.mysqlconnection import  connectToMySQL

class Product:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.p_sale = data['p_sale']
        self.presentation = data['presentation']
        self.price = data['price']
        self.image = data ['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cultivators_id = data['cultivators_id']

    """@staticmethod
    def valida_crop(formulario):
        es_valido = True 

        errores=[]
        
        if formulario['farm'] == "":
            errores.append('Debe ingresar el nombre de la finca')
            es_valido = False

        if formulario['state'] == "":
            errores.append('Debe ingresar el nombre del departamento')
            es_valido = False

        if formulario['municipality'] == "":
            errores.append('Debe ingresar el nombre del municipio')
            es_valido = False
        
        if formulario['fertilizer'] == "":
            errores.append('Debe ingresar el nombre del municipio')
            es_valido = False
        
        if formulario['f_amount'] == "":
            errores.append('Debe ingresar la cantidad de fertilizante')
            es_valido = False
        
        if formulario['date'] == "":
            errores.append('Debe ingresar la fecha de cosecha')
            es_valido = False

        if formulario['production'] == "":
            errores.append('Debe ingresar la produccion de su cosecha')
            es_valido = False

        if formulario['description'] == "":
            errores.append('Debe ingresar una descripcion')
            es_valido = False

        if formulario['image'] == "":
            errores.append('Debe ingresar una imagen')
            es_valido = False

        if formulario['share'] == "":
            errores.append('Debe seleccionar si desea compartir')
            es_valido = False
        
        return (es_valido, errores)"""


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO products (name, description, p_sale, presentation, price, image, cultivators_id) VALUES (%(name)s, %(description)s, %(p_sale)s, %(presentation)s,%(price)s, %(image)s, %(cultivators_id)s)"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls,formulario):
        query = "SELECT crops.*, farm FROM crops LEFT JOIN cultivators ON cultivators.id = crops.cultivators_id WHERE cultivators.id=%(id)s"
        results = connectToMySQL('weedproject').query_db(query,formulario) 
        crops = []
        for crop in results:
            
            crops.append(cls(crop)) 

        return crops

    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT crops.*, farm FROM crops LEFT JOIN cultivators ON cultivators.id = crops.cultivators_id WHERE crops.id = %(id)s"
        result = connectToMySQL('weedproject').query_db(query, formulario) #Lista de diccionarios
        publicacion = cls(result[0])
        return publicacion

    @classmethod
    def update(cls, formulario):
        if(formulario['image'] != ''):
            query = "UPDATE crops SET farm=%(farm)s, state=%(state)s, municipality=%(municipality)s, fertilizer=%(fertilizer)s, f_amount=%(f_amount)s, date=%(date)s, disease=%(disease)s, production=%(production)s, description=%(description)s, image=%(image)s, share=%(share)s WHERE id = %(id)s"
        else:
            query = "UPDATE crops SET farm=%(farm)s, state=%(state)s, municipality=%(municipality)s, fertilizer=%(fertilizer)s, f_amount=%(f_amount)s, date=%(date)s, disease=%(disease)s, production=%(production)s, description=%(description)s, share=%(share)s WHERE id = %(id)s"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM crops WHERE id = %(id)s;"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result

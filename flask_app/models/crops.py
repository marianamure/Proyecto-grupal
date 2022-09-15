from flask_app.config.mysqlconnection import  connectToMySQL

class Crop:

    def __init__(self, data):
        
        self.id = data['id']
        self.farm = data['farm']
        self.state = data['state']
        self.municipality = data['municipality']
        self.fertilizer = data['fertilizer']
        self.f_amount = data['f_amount']
        self.date = data['date']
        self.disease = data['disease']
        self.production = data['production']
        self.description = data['description']
        self.image = data['image']
        self.share = data['share']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cultivators_id = data['cultivators_id']

    @staticmethod
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

        if formulario['share'] == "":
            errores.append('Debe seleccionar si desea compartir')
            es_valido = False
        
        return (es_valido, errores)


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO crops (farm, state, municipality, fertilizer, f_amount, date, disease, production, description, image, share, cultivators_id) VALUES (%(farm)s, %(state)s, %(municipality)s, %(fertilizer)s,%(f_amount)s, %(date)s, %(disease)s, %(production)s, %(description)s, %(image)s, %(share)s, %(cultivators_id)s)"
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

    @classmethod
    def all(cls):
        query = "SELECT * FROM crops"
        results = connectToMySQL('weedproject').query_db(query) 
        crops = []
        for crop in results:
            crops.append(cls(crop)) 
        return crops

    @classmethod
    def get_crops(cls):
        query = "SELECT comments.*, crops.*, cultivators.full_name AS sender FROM comments LEFT JOIN cultivators ON cultivators.id = comments.cultivators_id LEFT JOIN crops ON crops.id = comments.crop_id"
        results = connectToMySQL('weedproject').query_db(query) 
        crops = []
        for crop in results:
            crops.append(cls(crop)) 
        return crops

"""    @classmethod
    def delete2(cls, formulario):
        query = "DELETE FROM comments WHERE id = %(id)s;"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result"""

"""    @classmethod
    def get_all_muro(cls):
        query = "SELECT publicaciones.*, users.first_name FROM publicaciones LEFT JOIN users ON users.id = publicaciones.user_id;"
        results = connectToMySQL('agro').query_db(query) 
        publicaciones = []
        for publicacion in results:
            
            publicaciones.append(cls(publicacion)) 

        return publicaciones"""
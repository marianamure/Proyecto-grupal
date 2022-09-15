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
        #self.cultivators_name = data['full_name']

    @staticmethod
    def valida_products(formulario):
        es_valido = True 

        errores=[]
        
        if formulario['name'] == "":
            errores.append('Debe ingresar el nombre del producto')
            es_valido = False

        if formulario['description'] == "":
            errores.append('Debe ingresar una descripcion')
            es_valido = False

        if formulario['p_sale'] == "":
            errores.append('Debe ingresar el punto de venta')
            es_valido = False
        
        if formulario['presentation'] == "":
            errores.append('Debe ingresar la presentacion del producto')
            es_valido = False
        
        if formulario['price'] == "":
            errores.append('Debe ingresar el precio')
            es_valido = False
                
        return (es_valido, errores)


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO products (name, description, p_sale, presentation, price, image, cultivators_id) VALUES (%(name)s, %(description)s, %(p_sale)s, %(presentation)s,%(price)s, %(image)s, %(cultivators_id)s)"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls,formulario):
        query = "SELECT products.*, name FROM products LEFT JOIN cultivators ON cultivators.id = products.cultivators_id WHERE cultivators.id=%(id)s"
        results = connectToMySQL('weedproject').query_db(query,formulario) 
        products = []
        for product in results:
            
            products.append(cls(product)) 

        return products

    @classmethod
    def get_all_for_buyers(cls):
        query = "SELECT * FROM products"
        results = connectToMySQL('weedproject').query_db(query) 
        products = []
        for product in results:
            products.append(cls(product)) 
        return products

    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT products.*, name FROM products LEFT JOIN cultivators ON cultivators.id = products.cultivators_id WHERE products.id = %(id)s"
        result = connectToMySQL('weedproject').query_db(query, formulario) #Lista de diccionarios
        product = cls(result[0])
        return product

    @classmethod
    def terminar_compra(cls, formulario):
        query = "INSERT INTO shopping (name_bank, address, home_delivery, method_payment, state, user_id) VALUES (%(name_bank)s, %(address)s, %(home_delivery)s, %(method_payment)s, %(state)s, %(user_id)s);"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result

    @classmethod
    def update(cls, formulario):
        if(formulario['image'] != ''):
            query = "UPDATE products SET name=%(name)s, description=%(description)s, p_sale=%(p_sale)s, presentation=%(presentation)s, price=%(price)s, image=%(image)s WHERE id = %(id)s"
        else:
            query = "UPDATE products SET name=%(name)s, description=%(description)s, p_sale=%(p_sale)s, presentation=%(presentation)s, price=%(price)s WHERE id = %(id)s"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM products WHERE id = %(id)s;"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result
    
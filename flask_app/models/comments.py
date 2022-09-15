from flask_app.config.mysqlconnection import  connectToMySQL

class Comment:

    def __init__(self,data):
        self.id = data['id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.crop_id = data['crop_id']
        self.cultivators_id = data['cultivators_id']
        self.sender_id = data['sender_id']

        self.sender_name = data['sender_name']
        self.cultivators_name = data['cultivators_name']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO comments (comment, crop_id, cultivators_id, sender_id ) VALUES (%(comment)s, %(crop_id)s, %(cultivators_id)s, %(sender_id)s)"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result

    """@classmethod
    def get_cultivators_comments(cls, formulario):
        #formulario = {id: 1}
        #2 LEFT JOINS
        query = "SELECT comments.*, cultivators.full_name AS sender FROM comments LEFT JOIN cultivators ON cultivators.id = comments.ultivators_id LEFT JOIN crops ON crops.id = comments.crop_id"
        results = connectToMySQL('weedproject').query_db(query, formulario) #Lista de diccionarios
        comments = []
        for comment in results:
            #message = {id: 1, content: "Hola", creat.., up.., rec_id.., send_id.., receiver_name: "Pedro", sender_name:"Barack"}
            comments.append(cls(comment)) #1.- cls(message) me crea instancia de mensaje. 2.- Agregamos la instancia a la lista de mensajes

        return comments"""

    
    @classmethod
    def get_cultivators_wall(cls, formulario):
        query = "SELECT comments.*, receivers.full_name as cultivator_name, senders.full_name as sender_name FROM comments LEFT JOIN cultivators as receivers ON receivers.id = cultivators_id LEFT JOIN cultivators as senders ON senders.id = sender_id WHERE cultivators_id = %(id)s"
        results = connectToMySQL('weedproject').query_db(query, formulario) #Lista de diccionarios
        comments = []
        for comment in results:
            #message = {id: 1, content: "Hola", creat.., up.., rec_id.., send_id.., receiver_name: "Pedro", sender_name:"Barack"}
            comments.append(cls(comment)) #1.- cls(message) me crea instancia de mensaje. 2.- Agregamos la instancia a la lista de mensajes

        return comments

    @classmethod
    def eliminar(cls, formulario):
        #formulario = {id: 1}
        query = "DELETE FROM comments WHERE id = %(id)s"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result


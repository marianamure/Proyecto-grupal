#EJECUTA nuestra aplicación
from flask_app import app

#Importando mi controlador
from flask_app.controllers import users_controller, publicaciones_controller, comentarios_controller



if __name__=="__main__":
    app.run(debug=True)
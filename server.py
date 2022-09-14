#EJECUTA nuestra aplicación
from flask_app import app

#Importando mi controlador
from flask_app.controllers import index_controller, cultivators_controller, buyers_controller, crops_controller, products_controller, comments_controller

#pipenv install flask pymysql flask-bcrypt
#pipenv shell
#py server.py

if __name__=="__main__":
    app.run(debug=True)
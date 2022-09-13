#EJECUTA nuestra aplicación
from flask_app import app

#Importando mi controlador
from flask_app.controllers import index_controller, cultivators_controller, buyers_controller, crops_controller



if __name__=="__main__":
    app.run(debug=True)
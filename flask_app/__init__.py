#INICIALIZA la aplicación
from flask import Flask

app = Flask(__name__)

#Establecemos una secret key
app.secret_key = "Mi llave super secreta"

app.config ['UPLOAD_FOLDER'] = "flask_app/static/images/"
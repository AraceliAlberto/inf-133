from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.libro_controller import libro_bp
from controllers.user_controller import user_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database import db

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "tu_clave_secreta_aqui"
SWAGGER_URL = "/api/docsLibrole"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Libreria API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///libreriarole.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(libro_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
    db.create_all()

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run(debug=True)

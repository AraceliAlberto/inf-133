from flask import Flask
from flask_login import LoginManager
from controllers import user_controller
from models.user_model import User
from database import db 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usersWA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "clave-secreta"

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
db.init_app(app)
app.register_blueprint(user_controller.user_bp)

if __name__ == '__main__':
    # Crea las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True)
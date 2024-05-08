from flask import Blueprint, request, redirect, url_for
# Importamos la vista de usuarios
from views import user_view
# Importamos el modelo de usuario
from models.user_model import User
from datetime import datetime

# Un Blueprint es un objeto que agrupa rutas y vistas
user_bp = Blueprint('user', __name__)  #aca vive 

# Definimos las rutas "/" asociada a la funcion usuarios
# que nos devuelve la vista de usuarios
@user_bp.route('/')
def usuarios():
    # Obtenemos todos los usuarios
    users = User.get_all()
    # Llamamos a la vista de usuarios
    return user_view.usuarios(users)

# Definimos la ruta "/users" asociada a la función registro
# que nos devuelve la vista de registro
@user_bp.route('/users', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        contrasenia = request.form['contrasenia']
        fecha_str = request.form['fecha_Nacimiento']
        
        # Creamos un nuevo usuario
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        user = User(first_name, last_name, email, contrasenia, fecha)
    
        # Guardamos el usuario
        user.save()
        # Redirigimos a la vista de usuarios
        return redirect(url_for('user.usuarios'))
    # Llamamos a la vista de registro
    return user_view.registro()
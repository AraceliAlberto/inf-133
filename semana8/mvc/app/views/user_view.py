from flask import render_template
def usuarios(users):
    return render_template('usuarios.html', users = users)

def registro():
    return render_template('registro.html')
#Mayucula clase
#minuscula funcion
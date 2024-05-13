
from functools import wraps
# Define un decorador que imprime un mensaje antes
# y después de llamar a la función decorada
# Usando wraps para mantener los metadatos de la función original
def my_decorator (func):
    @wraps (func)
    def wrapper (*args, **kwargs):
        print("Antes de llamar a la función")
        result = func(*args, **kwargs)
        print("Después de llamar a la función")
        return result
    return wrapper


# Aplica el decorador a una función
@my_decorator
def greet (name):
    """Función para saludar a alguien"""
    print(f"Hola, {name}!")
    # Llama a la función decorada
greet("Juan")
# Accede a los metadatos de la función original
print(greet.___name___)
# Output: greet
print(greet.____doc____)
# Output: Función para saludar a alguien

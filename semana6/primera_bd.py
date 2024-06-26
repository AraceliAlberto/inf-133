# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conectando = sqlite3.connect("instituto.db")

# Crear tabla de carreras
conectando.execute(
    """
    CREATE TABLE CARRERAS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL);
    """
)

# Insertar datos de carreras
conectando.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Ingeniería en Informática', 5)
    """
)
conectando.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Licenciatura en Administración', 4)
    """
)

# Consultar datos
print("CARRERAS:")
cursor = conectando.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)

# CARRERAS:
# (1, 'Ingeniería en Informática', 5)
# (2, 'Licenciatura en Administración', 4)

# Crear tablas de estudiantes
try:
    conectando.execute(
        """
        CREATE TABLE ESTUDIANTES
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        fecha_nacimiento DATE NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARRERAS ya existe")

# Insertar datos de estudiantes
conectando.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('Juan', 'Perez', '2000-05-15')
    """
)
conectando.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('María', 'Lopez', '1999-08-20')
    """
)

# Consultar datos de estudiantes
print("\nESTUDIANTES:")
cursor = conectando.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)

# ESTUDIANTES:
# (1, 'Juan', 'Perez', '2000-05-15')
# (2, 'María', 'Lopez', '1999-08-20')

# Crear tabla de matriculación
conectando.execute(
    """
    CREATE TABLE MATRICULACION
    (id INTEGER PRIMARY KEY,
    estudiante_id INTEGER NOT NULL,
    carrera_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
    FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
    """
)

# Insertar datos de matriculación
conectando.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha) 
    VALUES (1, 1, '2024-01-15')
    """
)
conectando.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha) 
    VALUES (2, 2, '2024-01-20')
    """
)

conectando.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
    VALUES (1, 2, '2024-01-25')
    """
)

# Consultar datos de matriculación
print("\nMATRICULACION:")
cursor = conectando.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha 
    FROM MATRICULACION
    JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)

# MATRICULACION:
# ('Juan', 'Perez', 'Ingeniería en Informática', '2024-01-15')
# ('María', 'Lopez', 'Licenciatura en Administración', '2024-01-20')
# ('Juan', 'Perez', 'Licenciatura en Administración', '2024-01-25')    

# Eliminar una fila de la tabla de matriculación
conectando.execute(
    """
    DELETE FROM MATRICULACION
    WHERE id = 3
    """
)

# Listar datos de matriculación
print("\nMATRICULACION:")
cursor = conectando.execute(
    "SELECT * FROM MATRICULACION"
)

for row in cursor:
    print(row)

# MATRICULACION:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-20')

# Actualizar una fila de la tabla de matriculación
conectando.execute(
    """
    UPDATE MATRICULACION
    SET fecha = '2024-01-30'
    WHERE id = 2
    """
)
# Listar datos de matriculación
print("\nMATRICULACION:")
cursor = conectando.execute(
    "SELECT * FROM MATRICULACION"
)
for row in cursor:
    print(row)
    
# MATRICULACION:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-30')

#cnfirmar cambios
conectando.commit()
# Cerrar conexión
conectando.close()

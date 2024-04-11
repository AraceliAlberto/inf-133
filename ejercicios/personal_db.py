# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conectando = sqlite3.connect("personal.db")

# =========> Crear tablas DEPARTAMENTOS <=========
try:
    conectando.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion DATE NOT NULL)
        """
    )

except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya existe")

# Insertar datos en departamentos
conectando.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ("Ventas", '10-04-2020')
    """
),

conectando.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ("Marketing", '11-04-2020')
    """
),

print("\nDEPARTAMENTOS:")
cursor = conectando.execute("SELECT * FROM DEPARTAMENTOS")
for row in cursor:
    print(row)
# =========> Crear tablas CARGOS <=========
try:
    conectando.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion DATE NOT NULL)
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")

# Insertar datos en CARGOS
conectando.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ("Gerente de Ventas", "Senior", '10-04-2020')
    """
),

conectando.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ("Analista de Marketing", "Junior", '11-04-2020')
    """
),

conectando.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ("Representante de Ventas", "Junior", '12-04-2020')
    """
),

print("\nCARGOS:")
cursor = conectando.execute("SELECT * FROM CARGOS")
for row in cursor:
    print(row)

# =========> Crear tablas EMPLEADOS <=========
try:
    conectando.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        departamento_id INTEGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        fecha_creacion DATE NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")

# Insertar datos en EMPLEADOS
conectando.execute(
    """
    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion) 
    VALUES ("Juan", "Gonzales", "Perez", '2023-05-15', 1, 1, '2020-04-10')
    """
),

conectando.execute(
    """
    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion) 
    VALUES ("Maria", "Lopez", "Martinez", '2023-06-20', 2, 2, '2020-04-10')
    """
),

print("\nEMPLEADOS:")
cursor = conectando.execute("SELECT * FROM EMPLEADOS")
for row in cursor:
    print(row)

# =========> Crear tablas SALARIOS <=========
try:
    conectando.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        empleado_id INTEGER,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion DATE NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
        """
    )

except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")

# Insertar datos en SALARIOS
conectando.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (1, '3000', '01-04-2024', '30-04-2025', '10-04-2024')
    """
),

conectando.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (2, '3500', '01-07-2024', '30-04-2024', '10-04-2024')
    """
),

print("\nSALARIOS:")
cursor = conectando.execute("SELECT * FROM SALARIOS")
for row in cursor:
    print(row)

#Ejercicios Propuestos
conectando.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)

conectando.execute(
    """
    DELETE FROM SALARIOS
    WHERE id = 2
    """
)

conectando.commit()
conectando.close()
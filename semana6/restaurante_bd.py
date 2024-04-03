# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conectando = sqlite3.connect("restaurante.db")

# =========> Crear tablas PLATOS <=========
try:
    conectando.execute(
        """
        CREATE TABLE PLATOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL, 
        categoria TEXT NOT NULL)
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARRERAS ya existe")

# Insertar datos en platos
conectando.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Pizza', 10.99, 'Italiana')
    """
),

conectando.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Hamburguesa', 8.99, 'Americana')
    """
),

conectando.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Sushi', 12.99, 'Japonesa')
    """
),

conectando.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Ensala', 6.99, 'Vegetariana')
    """
)

conectando.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)

# Consultar datos
print("PLATOS:")
cursor = conectando.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

# =========> Crear tablas MESAS <=========
try:
    conectando.execute(
        """
        CREATE TABLE MESAS
        (id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL)
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARRERAS ya existe")

# Insertar datos de mesas
conectando.execute(
        """
        INSERT INTO MESAS (numero) 
        VALUES (1)
        """
    ),
conectando.execute(
        """
        INSERT INTO MESAS (numero) 
        VALUES (2)
        """
    ),
conectando.execute(
        """
        INSERT INTO MESAS (numero) 
        VALUES (3)
        """
    ),
conectando.execute(
        """
        INSERT INTO MESAS (numero) 
        VALUES (4)
        """
    )

# Consultar datos de mesas
print("\nMESAS:")
cursor = conectando.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

# =========> Crear tablas PEDIDOS <=========
try:
    conectando.execute(
        """
        CREATE TABLE PEDIDOS
        (id INTEGER PRIMARY KEY,
        platos_id INTEGER NOT NULL,
        mesas_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (platos_id) REFERENCES PLATOS(id),
        FOREIGN KEY (mesas_id) REFERENCES MESAS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARRERAS ya existe")

# Insertar datos de pedidos
conectando.execute(
    """
    INSERT INTO PEDIDOS (platos_id, mesas_id, cantidad, fecha) 
    VALUES (1, 2, 2, '2024-04-01')
    """
),
conectando.execute(
    """
    INSERT INTO PEDIDOS (platos_id, mesas_id, cantidad, fecha) 
    VALUES (2, 3, 1, '2024-04-01')
    """
),
conectando.execute(
    """
    INSERT INTO PEDIDOS (platos_id, mesas_id, cantidad, fecha) 
    VALUES (3, 1, 3, '2024-04-02')
    """
),
conectando.execute(
    """
    INSERT INTO PEDIDOS (platos_id, mesas_id, cantidad, fecha) 
    VALUES (4, 4, 1, '2024-04-02')
    """
),

# Consultar datos de PEDIDOS
print("\nPEDIDOS:")
cursor = conectando.execute(
    """
    SELECT PLATOS.id, MESAS.id, PEDIDOS.cantidad, PEDIDOS.fecha 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.platos_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesas_id = MESAS.id
    """
)
for row in cursor:
    print(row)

conectando.commit()
conectando.close()
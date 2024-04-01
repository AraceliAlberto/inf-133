# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conectando = sqlite3.connect("restaurante.db")

# =========> Crear tablas PLATOS <=========

conectando.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL, 
    categoria TEXT NOT NULL)
    """
)

# Insertar datos en platos
conectando.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Pizza', 20, 'Hawaina')
    """
)

# Consultar datos
print("PLATOS:")
cursor = conectando.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

# =========> Crear tablas MESAS <=========
conectando.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL)
    """
)

# Insertar datos de mesas
conectando.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (7)
    """
)

# Consultar datos de mesas
print("\nMESAS:")
cursor = conectando.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

# =========> Crear tablas PEDIDOS <=========

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

# Insertar datos de pedidos
conectando.execute(
    """
    INSERT INTO PEDIDOS (platos_id, mesas_id, cantidad, fecha) 
    VALUES (1, 1, 1, '2024-01-15')
    """
)

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

# Cerrar conexión
conectando.close()
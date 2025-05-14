from sqlalchemy.orm import sessionmaker
import csv
from crear_base import Saludo2
from configuracion import engine

with open('data/saludos_mundo.csv', 'r') as f:
    # pasar los datos a estructuras de Python
    data = csv.reader(f, delimiter='|')

    # saltar la primera encabezado
    next(data)


    lista_datos = []

    for row in data:
        saludo2 = row[0]
        tipo2 = row[1]
        origen2 = row[2]

        miSaludo = Saludo2(
            mensaje=saludo2,
            tipo=tipo2,
            origen=origen2
        )
        lista_datos.append(miSaludo)

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Agregar todos los saludos a la sesión
session.add_all(lista_datos)

# Confirmar los cambios
session.commit()
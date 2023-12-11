import sqlite3
import csv

# Extraer los datos de la BD
db_path = 'warehouse.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

query = '''
    SELECT * FROM Boxes b JOIN Warehouses w ON b.Warehouse = w.code
'''
cursor.execute(query)

data = cursor.fetchall() # los datos estan en la variable data

connection.close()

# Generar CSV
csv_file_path = 'exportar_data_warehouse.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Escribir encabezados (nombres de columnas)
    column_names = [description[0] for description in cursor.description]
    csv_writer.writerow(column_names)
    
    # Escribir datos
    csv_writer.writerows(data)

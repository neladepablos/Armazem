import pandas as pd
import random

# Generar más datos aleatorios
num_rows_to_generate = 500
new_data = []

for _ in range(num_rows_to_generate):
    country =  random.choice(['USA', 'Canada'])
    usa_cities = ['New York', 'Chicago', 'San Francisco', 'Los Angeles']
    can_cities = ['Vancouver', 'Toronto', 'Montreal']

    if country == 'USA':
        city = random.choice(usa_cities)
    else:
        city = random.choice(can_cities)

    new_row = {
        'code': ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4)),
        'contents': random.choice(['Rocks', 'Scissors', 'Paper', 'Markers', 'Notebooks', 'Staplers', 'Pencils']),
        'value': random.randint(100, 700),
        'status': random.choice(['waiting_pickup', 'delivered', 'lost', 'returned']),
        'warehouse': random.randint(1, 10),
        'country': country,
        'city': city,
        'capacity': random.randint(100, 800)
    }

    new_data.append(new_row)


df = pd.DataFrame(new_data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('warehouse_data_pandas_test.csv', index=False)


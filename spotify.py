#analisis del codigo ESTE GENERA UN GRAFICO DE BARRAS
# Este código lee un archivo CSV que contiene información sobre canciones de Spotify.
# Filtra las canciones para quedarse solo con las 3 que tienen más streams (reproducciones),
# luego crea un gráfico de barras para mostrar estas 3 canciones con los datos de streams 
# encima de cada barra.
#https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023 link dataset

import pandas as pd  
import matplotlib.pyplot as plt  

# Cargamos el archivo CSV con los datos de las canciones de Spotify
file_path = 'C:\\Users\\bbria\\Downloads\\archive (1)\\spotify-2023.csv'
spotify_data = pd.read_csv(file_path, encoding='latin1')  

# Convertimos la columna 'streams' a números. Si algún dato no es numérico, lo dejamos fuera
spotify_data['streams'] = pd.to_numeric(spotify_data['streams'], errors='coerce')

# Quitamos las filas que no tienen datos numéricos en la columna de streams
spotify_data_clean = spotify_data.dropna(subset=['streams'])

# Ordenamos las canciones por el número de streams (de más a menos) y seleccionamos las 3 principales
top_songs = spotify_data_clean.nlargest(3, 'streams')[['track_name', 'streams']]

# Creamos un gráfico de barras para las 3 canciones más populares
plt.figure(figsize=(10, 6))  # Establecemos el tamaño del gráfico
bars = plt.bar(top_songs['track_name'], top_songs['streams'], color='skyblue')  # Dibujamos las barras

# Añadimos las cantidades de streams encima de cada barra
for bar in bars:
    yval = bar.get_height()  # Obtenemos la altura de la barra (el número de streams)
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')  # Colocamos el número encima

# Títulos y etiquetas para que el gráfico sea más fácil de entender
plt.title('Top 3 Songs with Most Streams', fontsize=16)  # Título del gráfico
plt.xlabel('Song Names', fontsize=12)  # Etiqueta para el eje X
plt.ylabel('Streams', fontsize=12)  # Etiqueta para el eje Y
plt.xticks(rotation=45, ha='right')  # Giramos los nombres de las canciones para que se lean mejor
plt.tight_layout()  # Acomodamos el gráfico para que no se superpongan los elementos

# Mostramos el gráfico en pantalla
plt.show()

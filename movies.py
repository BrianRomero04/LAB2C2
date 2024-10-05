import pandas as pd
import matplotlib.pyplot as plt

# analisis del código: GENERA UN GRAFICO CIRCULAR
# Lo que hago aquí es cargar un archivo que tiene datos de películas.
# Este codigo selecciona las 4 películas que han ganado más dinero en taquilla y las ordena de mayor a menor.
# Luego, creo un gráfico circular que muestra tanto el nombre como la cantidad de dinero recaudado.
#https://www.kaggle.com/datasets/delfinaoliva/movies link dataset

# Cargar el archivo CSV con la información de las películas
file_path = 'C:/Users/bbria/Downloads/archive (2)/movies_data.csv'
movies_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Seleccionar las 4 películas con más recaudación, organizándolas de mayor a menor
top_4_movies = movies_data[['Movie', 'Box Office']].sort_values(by='Box Office', ascending=False).head(4)

# Crear etiquetas que incluyan el nombre de la película y la cantidad recaudada
labels = [f"{movie}: ${box_office:,}" for movie, box_office in zip(top_4_movies['Movie'], top_4_movies['Box Office'])]

# Aquí dibujo el gráfico circular para mostrar la recaudación de las películas con el monto
plt.figure(figsize=(8, 8))  # Ajusto el tamaño del gráfico
plt.pie(top_4_movies['Box Office'], labels=labels, autopct='%1.1f%%', colors=['red', 'blue', 'green', 'purple'])

# Agrego un título al gráfico
plt.title('Top 4 Movies by Box Office Earnings')

# Finalmente, muestro el gráfico en pantalla
plt.show()

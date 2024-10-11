import pandas as pd
import matplotlib.pyplot as plt

'''
analisis
El gráfico circular muestra la proporción de ingresos de las cuatro películas con mayor recaudación.
Cada segmento representa una película, con su tamaño proporcional a la cantidad recaudada.
Las etiquetas incluyen el nombre de la película y la recaudación en dólares,
junto con el porcentaje del total. Los colores diferenciados facilitan la identificación de cada película, 
permitiendo comparar rápidamente su éxito relativo en taquilla.
https://www.kaggle.com/datasets/delfinaoliva/movies link dataset
'''

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

import pandas as pd
import matplotlib.pyplot as plt
'''
analisis
El gráfico de líneas compara los goles de los cuatro equipos más goleadores de la Premier League.
Cada punto representa un equipo y su cantidad de goles, conectados por líneas para facilitar la comparación.
Las cifras de goles se muestran sobre cada punto, y la cuadrícula ayuda a interpretar mejor los datos,
destacando qué equipo tuvo el mejor desempeño goleador, como en este caso nos muestra al "manchester city" como el 
mayor goleador con 179 goles.
https://www.kaggle.com/datasets/abdelrahmanemad594/premier-league-season-2024 link dataset.
'''
# Cargar el archivo CSV con la información de los equipos
file_path = 'C:/Users/bbria/Downloads/archive/PremierLeagueSeason2024.csv'
premier_data = pd.read_csv(file_path)

# Seleccionar los 4 equipos con más goles, organizándolos de mayor a menor
top_4_teams_most_goals = premier_data[['team', 'goals_scored']].sort_values(by='goals_scored', ascending=False).head(4)

# Aquí es donde se dibuja el gráfico de líneas para mostrar los goles de los equipos
plt.figure(figsize=(10, 6))
plt.plot(top_4_teams_most_goals['team'], top_4_teams_most_goals['goals_scored'], marker='o', color='blue', linestyle='--')

# Agrego el título del gráfico y etiquetas para los ejes
plt.title('Top 4 Teams with Most Goals (Line Chart)')
plt.xlabel('Team')
plt.ylabel('Goals Scored')

# Agregar la cantidad de goles encima de cada punto
for i, txt in enumerate(top_4_teams_most_goals['goals_scored']):
    plt.text(i, top_4_teams_most_goals['goals_scored'].iloc[i] + 2, str(txt), ha='center')

# Muestro las líneas de la cuadrícula para hacer más fácil ver las cantidades
plt.grid(True)
plt.tight_layout()

# Finalmente, muestro el gráfico
plt.show()


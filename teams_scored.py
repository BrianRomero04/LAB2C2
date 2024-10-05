import pandas as pd
import matplotlib.pyplot as plt

# analisis del código: GENERA UNA GRAFICO DE LINEAS
# Lo que hago aquí es cargar un archivo CSV que tiene datos de los equipos de la Premier League.
# Luego selecciono los 4 equipos que han marcado más goles en la temporada y los organizo de mayor a menor.
# Al final, creo un gráfico de líneas donde se puede ver cuántos goles ha marcado cada equipo y agrego las cantidades en cada punto.
#https://www.kaggle.com/datasets/abdelrahmanemad594/premier-league-season-2024 link dataset.

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


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime



def bar_chart():

    data = pd.read_csv('player_shooting_2023_2024.csv')


    top_10 = data.nlargest(10, data.columns[9])


    
    
    players_top10 = top_10.iloc[:, 2]
    nintey_played = top_10.iloc[:, 8]
    goals = top_10.iloc[:, 9]

    
    plt.figure(figsize=(12, 7), facecolor='#D3D3D3')
    width = 0.5  

    
    plt.bar(players_top10, goals, width=width, label='Goals scored', alpha= 1, color = '#003399')


    plt.xlabel('Player names', color = '#003399', fontweight = 'bold')
    plt.ylabel('Total Number of goals scored', color = '#003399', fontweight = 'bold')
    plt.title('Top 10 goal scorers in Premier League 23/24 Season', color = '#003399', fontweight = 'bold')
    plt.xticks(rotation=30,fontsize= 8,fontweight = 'bold')  
    plt.yticks(np.arange(0, goals.max() + 1,1),fontweight = 'bold')
    plt.legend()
    
    plt.show(block = False)


def scatter_plt():
    data = pd.read_csv('player_shooting_2023_2024.csv')

    
    top_50 = data.nlargest(40, data.columns[9])  

    top_10 = data.nlargest(10, data.columns[9])
    
    players_top10 = top_10.iloc[:, 2]  
    SOT_played = top_50.iloc[:, 10] 
    goals = top_50.iloc[:, 9]  

    
    plt.figure(figsize=(10, 5), facecolor='#D3D3D3' )

    
    plt.scatter(SOT_played, goals, color='#0099cc', alpha=0.6, s=80)  

    
    slope, intercept = np.polyfit(SOT_played, goals, 1)
    x_values = np.array([min(SOT_played), max(SOT_played)])
    y_values = intercept + slope * x_values

    plt.plot(x_values, y_values, 'b--', label='Regression Line', )

    
    for i, txt in enumerate(players_top10):
        plt.annotate(txt, (SOT_played.iloc[i], goals.iloc[i]), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xlabel('Total Shots Taken', color = '#003399', fontweight = 'bold')
    plt.ylabel('Goals Scored', color = '#003399', fontweight = 'bold')
    plt.title("Player's total Shoots vs Goals Scored Premier League 23/24 Season", color = '#003399', fontweight = 'bold')
    plt.legend()
    plt.show(block = False)


def line2():
    data = pd.read_csv('player_shooting_2023_2024.csv')
    data_team = pd.read_csv('EPL Standings 2000-2022.csv')
    man_city_data = data_team.loc[data_team.iloc[:, 2] == 'Manchester City']
    top_10 = data.nlargest(1, data.columns[9])

    last_10_seasons = man_city_data.iloc[-10:, :]


    seasons = last_10_seasons.iloc[:, 0]
    goals_scored = last_10_seasons.iloc[:, 7]

    plt.figure(figsize=(10, 6), facecolor= 'skyblue')
    plt.plot(seasons, goals_scored, linestyle='-', marker='o', color='navy', label='Goals Scored')

    plt.xlabel('Season', color = 'white', fontweight = 'bold')
    plt.ylabel('Goals Scored (GF)', color = 'white', fontweight = 'bold')
    plt.title('Manchester City Goals Scored in the Last 10 Seasons', color = 'white', fontweight = 'bold' )
    plt.legend()
    plt.xticks(rotation=45, fontweight = 'bold')  
    plt.tight_layout()  
    plt.show()

def main():
    
    bar_chart()
    scatter_plt() 
    line2()

if __name__ == "__main__":
    main()


    
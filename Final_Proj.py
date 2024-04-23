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

    
    plt.figure(figsize=(12, 7))
    width = 0.5  

    
    plt.bar(players_top10, goals, width=width, label='Goals scored', alpha=0.6)


    plt.xlabel('Player names')
    plt.ylabel('Total Number of goals scored')
    plt.title('Top 10 goal scorers in Premier League 23/24 Season')
    plt.xticks(rotation=30)  
    plt.yticks()
    plt.legend()
    
    plt.show(block = False)


def scatter_plt():
    data = pd.read_csv('player_shooting_2023_2024.csv')

    
    top_50 = data.nlargest(30, data.columns[9])  

    top_10 = data.nlargest(10, data.columns[9])
    
    players_top10 = top_10.iloc[:, 2]  
    SOT_played = top_50.iloc[:, 10] 
    goals = top_50.iloc[:, 9]  

    
    plt.figure(figsize=(10, 5))

    
    plt.scatter(SOT_played, goals, color='green', alpha=0.6, s=80)  

    
    slope, intercept = np.polyfit(SOT_played, goals, 1)
    x_values = np.array([min(SOT_played), max(SOT_played)])
    y_values = intercept + slope * x_values

    plt.plot(x_values, y_values, 'b--', label='Regression Line')

    
    for i, txt in enumerate(players_top10):
        plt.annotate(txt, (SOT_played.iloc[i], goals.iloc[i]), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xlabel('Total Shots Taken')
    plt.ylabel('Goals Scored')
    plt.title("Player's total Shoots vs Goals Scored Premier League 23/24 Season")
    plt.legend()
    plt.show()




""" line graph"""
def line_plt():
    data = pd.read_csv('player_shooting_2023_2024.csv')

    top_10 = data.nlargest(10, data.columns[9]) 

    players_top10 = top_10.iloc[:, 2]  
    SOT_played = top_10.iloc[:, 11] 
    goals = top_10.iloc[:, 10]  

    
    sorted_data = top_10.sort_values(by=top_10.columns[11])
    sorted_players = sorted_data.iloc[:, 2]
    sorted_SOT = sorted_data.iloc[:, 11]
    sorted_goals = sorted_data.iloc[:, 10]

    plt.figure(figsize=(12, 8))

    plt.plot(sorted_SOT, sorted_goals, linestyle='-', color='red', label='Goals vs SOT')



    plt.xlabel('Shots On Target')
    plt.ylabel('Total Shots')
    plt.title('Player shots on targets in Premier League 23/24 Season')
    plt.legend()

    plt.show()

def main():
    
    bar_chart()
    scatter_plt() 
    line_plt() 

if __name__ == "__main__":
    main()


    
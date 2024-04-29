"""
Author: Tri Do
SL: Thompson Nguyen
Class: ISTA 131
Assignment: Final Project
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Bar Chart 
def bar_chart(file):
    file['Age'] = pd.to_numeric(file['Age'], errors='coerce')
    file['Gls'] = pd.to_numeric(file['Gls'], errors='coerce')

    file = file.dropna(subset=['Age', 'Gls'])

    age_group_means = file.groupby('Age')['Gls'].mean().reset_index()

    plt.figure(figsize=(12, 7), facecolor="grey")

    plt.bar(age_group_means['Age'], age_group_means['Gls'], color='blue', alpha=0.7, label='Average Goals Scored')

    #ChatGPT help (lines 29-32)
    coefficients = np.polyfit(age_group_means['Age'], age_group_means['Gls'], 3)
    curve_fit = np.poly1d(coefficients)
    curve_x = np.linspace(min(age_group_means['Age']), max(age_group_means['Age']), 100)
    curve_y = curve_fit(curve_x)
    plt.plot(curve_x, curve_y, color='r', linestyle='--', label='Trend Curve')

    plt.xlabel('Age', fontweight='bold', color='navy')
    plt.ylabel('Goals Scored', fontweight='bold', color='navy')
    plt.title('Goals Scored by Age (Premier League 23/24 Season)', fontweight='bold', color='navy')

    plt.legend()
    plt.grid(True)
    plt.show()

# Scatter Plot
def scat_plot(file):
    file['Age'] = pd.to_numeric(file['Age'], errors='coerce')
    file['Gls'] = pd.to_numeric(file['Gls'], errors='coerce')

    file = file.dropna(subset=['Age', 'Gls'])

    age = file['Age']
    goals = file['Gls']

    plt.figure(figsize=(12, 7), facecolor='grey')

    plt.scatter(age, goals, color='b', alpha=0.7, label='Goals Scored')

    # ChatGPT help (lines 57 - 60)
    coefficients = np.polyfit(age, goals, 3)
    curve_fit = np.poly1d(coefficients)
    curve_x = np.linspace(min(age), max(age), 100)
    curve_y = curve_fit(curve_x)
    plt.plot(curve_x, curve_y, color='r', linestyle='--', label='Trend Curve')

    plt.xlabel('Age', fontweight='bold', color='navy')
    plt.ylabel('Goals Scored', fontweight='bold', color='navy')
    plt.title('Goals Scored by Age of Players (Premier League 23/24 Season)', fontweight='bold', color='navy')

    plt.legend()
    plt.show()

# Line Plot
def line_plt(file):
    team_season_wins = file[['Team', 'Season', 'W']]
    
    # ChatGPT help (line 76)
    team_palette = sns.color_palette("tab10", len(team_season_wins['Team'].unique()))

    plt.figure(figsize=(12, 8), facecolor='blue')
    
    #chatgpt help (line 77)
    sns.lineplot(x='Season', y='W', hue='Team', data=team_season_wins,
                 palette=team_palette, marker='o', linewidth=2.5)

    plt.xlabel('Season', fontsize=14, fontweight='bold', color='white')
    plt.ylabel('Number of Wins', fontsize=14, fontweight='bold', color='white')
    plt.title('Number of Wins Over Seasons by Team', fontsize=16, fontweight='bold', color='white')

    #chatgpt help (line 85)
    plt.legend(title='Team', title_fontsize='large', fontsize='medium', loc='upper left', bbox_to_anchor=(1.05, 1))

    plt.xticks(rotation=45, ha='right', fontsize=10)

    plt.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()

    plt.show()

def main():
    file = pd.read_csv("player_shooting_2023_2024.csv")
    file2 = pd.read_csv("EPL Standings 2000-2022.csv")
    bar_chart(file)
    scat_plot(file)
    line_plt(file2)
    

if __name__ == "__main__":
    main()
    

"""
Author Tri Do
SL: Thompson Nguyen
Class: ISTA 131
Final Project
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





# bar_chart 
def bar_chart(file):
    file['Age'] = pd.to_numeric(file['Age'], errors='coerce')
    file['Gls'] = pd.to_numeric(file['Gls'], errors='coerce')

    file = file.dropna(subset=['Age', 'Gls'])

    age_group_means = file.groupby('Age')['Gls'].mean().reset_index()

    plt.figure(figsize=(12, 7))

    plt.bar(age_group_means['Age'], age_group_means['Gls'], color='b', alpha=0.7, label='Average Goals Scored')

    coefficients = np.polyfit(age_group_means['Age'], age_group_means['Gls'], 3)
    curve_fit = np.poly1d(coefficients)
    curve_x = np.linspace(min(age_group_means['Age']), max(age_group_means['Age']), 100)
    curve_y = curve_fit(curve_x)
    plt.plot(curve_x, curve_y, color='r', linestyle='--', label='Trend Curve')

    plt.xlabel('Age')
    plt.ylabel('Goals Scored')
    plt.title('Goals Scored by Age Premier League 23/24 Season')

    plt.legend()
    plt.grid(True)
    plt.show()


def scat_plot(file):
    file['Age'] = pd.to_numeric(file['Age'], errors='coerce')
    file['Gls'] = pd.to_numeric(file['Gls'], errors='coerce')

    # Drop rows with NaN values in 'Age' or 'Gls'
    file = file.dropna(subset=['Age', 'Gls'])

    age = file['Age']
    goals = file['Gls']

    plt.figure(figsize=(12, 7))

    plt.scatter(age, goals, color='b', alpha=0.7, label='Goals Scored')

    # chatgpt help
    coefficients = np.polyfit(age, goals, 3) 
    curve_fit = np.poly1d(coefficients)
    curve_x = np.linspace(min(age), max(age), 100)
    curve_y = curve_fit(curve_x)
    plt.plot(curve_x, curve_y, color='r', linestyle='--', label='Trend Curve')

    plt.xlabel('Age')
    plt.ylabel('Goals Scored')
    plt.title('Goals Scored vs Age of Players Premier League 23/24 Season')

    plt.legend()
    plt.show()


def line_plt(file):
    age = file['Age']
    goals = file['G/Sh']

    plt.figure(figsize=(10, 6))
    plt.plot(age, goals, marker='o', linestyle='-', color='b')

    plt.xlabel('Age')
    plt.ylabel('G/Sh')
    plt.title('Goals/Shots vs Age Line Graph')

    plt.grid(True)
    plt.show()


def main():
    f = pd.read_csv("player_shooting_2023_2024.csv")
    bar_chart(f)
    scat_plot(f)
    line_plt(f)
    

if __name__ == "__main__":
    main()
    
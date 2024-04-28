"""
Author Tri Do
SL: Thompson Nguyen
Class: ISTA 131
Final Project
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def data_processing(file):
    print("Original Dataset:")
    print(file.head())

    # Convert 'Rk' column to string type and filter rows
    data_filtered = file[file['Rk'].astype(str).str.contains('Rk') == False]

    # Display the filtered dataset
    print("\nFiltered Dataset (Rows with 'Rk' in 'Rk' column removed):")
    print(data_filtered.head())


# bar_chart 
def bar_chart(file):
    file['Age'] = pd.to_numeric(file['Age'], errors='coerce')
    file['Gls'] = pd.to_numeric(file['Gls'], errors='coerce')

    # Drop rows with NaN values in 'Age' or 'Gls'
    file = file.dropna(subset=['Age', 'Gls'])

    # Aggregate data by 'Age' and calculate mean goals scored ('Gls')
    age_group_means = file.groupby('Age')['Gls'].mean().reset_index()

    # Plotting the bar chart with trend curve
    plt.figure(figsize=(12, 7))

    # Plotting the bar chart
    plt.bar(age_group_means['Age'], age_group_means['Gls'], color='b', alpha=0.7, label='Average Goals Scored')

    # Calculating and plotting the trend curve (polynomial curve)
    coefficients = np.polyfit(age_group_means['Age'], age_group_means['Gls'], 3)  # Use a third-degree polynomial
    curve_fit = np.poly1d(coefficients)
    curve_x = np.linspace(min(age_group_means['Age']), max(age_group_means['Age']), 100)
    curve_y = curve_fit(curve_x)
    plt.plot(curve_x, curve_y, color='r', linestyle='--', label='Trend Curve')

    # Adding labels and title
    plt.xlabel('Age')
    plt.ylabel('Goals Scored')
    plt.title('Goals Scored by Age Premier League 23/24 Season')

    # Adding legend and displaying the plot
    plt.legend()
    plt.grid(True)
    plt.show()


def scat_plot(file):
    file['Age'] = pd.to_numeric(file['Age'], errors='coerce')
    file['Gls'] = pd.to_numeric(file['Gls'], errors='coerce')

    # Drop rows with NaN values in 'Age' or 'Gls'
    file = file.dropna(subset=['Age', 'Gls'])

    # Extract 'Age' and 'Gls' columns
    age = file['Age']
    goals = file['Gls']

    # Plotting the scatter plot with trendline
    plt.figure(figsize=(12, 7))

    # Plotting the scatter plot
    plt.scatter(age, goals, color='b', alpha=0.7, label='Goals Scored by Age')

    # Calculating and plotting the trend curve (polynomial curve)
    coefficients = np.polyfit(age, goals, 3)  # Use a third-degree polynomial
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

    # Plotting the line graph
    plt.figure(figsize=(10, 6))
    plt.plot(age, goals, marker='o', linestyle='-', color='b')

    plt.xlabel('Age')
    plt.ylabel('G/Sh')
    plt.title('Goals/Shots vs Age Line Graph')

    plt.grid(True)
    plt.show()


def main():
    f = pd.read_csv("player_shooting_2023_2024.csv")
    data_processing(f)
    bar_chart(f)
    scat_plot(f)
    line_plt(f)
    

if __name__ == "__main__":
    main()
    
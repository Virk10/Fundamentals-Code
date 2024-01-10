import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Loading the data from the data file accoridn to my rollnumber it
    data = pd.read_csv('data9.csv', header=None, names=['asslaray'])
    # Calculating the mean annual salary (˜W)
    mean_salary = np.mean(data['asslaray'])

    # Calculating the value X, which is the fraction of the population with salaries between 0.8 * ˜W and 1.2 * ˜W
    lower_bound = 0.8 * mean_salary
    upper_bound = 1.2 * mean_salary
    fraction_within_bounds = ((data['asslaray'] >= lower_bound) & (data['asslaray'] <= upper_bound)).sum() / len(data['asslaray'])

    # A reasonable figure size
    plt.figure(figsize=(12, 8))

    # Plot the histogram
    plt.hist(data['asslaray'], bins=30, density=True, alpha=0.75, label='Probability Density Function')
    plt.axvline(mean_salary, color='red', linestyle='dashed', linewidth=2, label='Mean Salary (˜W)')
    plt.xlabel('Annual Salary')
    plt.ylabel('Probability Density')
    plt.title('Probability Density Function of Annual Salaries')
    plt.legend()

    # Print the calculated values on the graph
    plt.text(mean_salary, 0.04, f'Mean Salary (˜W): {mean_salary:.2f}', color='red', ha='center')
    plt.text(mean_salary, 0.035, f'Fraction within 0.8˜W and 1.2˜W: {fraction_within_bounds:.2%}', color='blue', ha='center')

    # Save the figure to a file
    plt.savefig('output_figure.png')

    # Close the plot
    plt.close()

if __name__ == "__main__":
    main()

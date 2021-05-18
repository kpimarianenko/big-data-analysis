import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

salesDist = pd.read_csv('./Data/stores-dist.csv')

print('\nHEAD:')
print(salesDist.head())

salesDist = salesDist.rename(columns={'annual net sales': 'sales', 'number of stores in district': 'stores'})

print('\nRENAMED HEAD:')
print(salesDist.head())

print(salesDist.corr(method='pearson'))

sales = salesDist.drop(columns='district')
print(sales.head())

y = sales['sales']
x = sales.stores

plt.figure(figsize=(20, 10))

plt.plot(x, y, 'o', markersize=15)

plt.ylabel('Annual Net Sales', fontsize=30)
plt.xlabel('Number of Stores in the District', fontsize=30)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.show()

m, b = np.polyfit(x, y, 1)
print('The slope of line is {:.2f}.'.format(m))
print('The y-intercept is {:.2f}.'.format(b))
print('The best fit simple linear regression line is {:.2f}x + {:.2f}.'.format(m, b))

y_mean = y.mean()
x_mean = x.mean()
print('The centroid for this dataset is x = {:.2f} and y = {:.2f}.'.format(x_mean, y_mean))

# Enlarge the plot size
plt.figure(figsize=(20,10))

# Plot the scatter plot of the data set
plt.plot(x, y, 'o', markersize=14, label="Annual Net Sales")

# Plot the centroid point
plt.plot(x_mean, y_mean, '*', markersize=30, color="r")

# Plot the linear regression line
plt.plot(x, m*x + b, '-', label='Simple Linear Regression Line', linewidth=4)

# Create the x and y axis labels
plt.ylabel('Annual Net Sales', fontsize=30)
plt.xlabel('Number of Stores in District', fontsize=30)

# Enlarge x and y tick marks
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

# Point out the centroid point in the plot
plt.annotate('Centroid', xy=(x_mean-0.1, y_mean-5), xytext=(x_mean-3, y_mean-20),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=30)

# Create legend
plt.legend(loc='upper right', fontsize=20)
plt.show()


def create_prediction(query):
    if query >= 1:
        predict = m * query + b
        return predict
    else:
        print("You must have at least 1 store in the district to predict the annual net sales.")


for i in range(1, 11):
    print(f'Prediction for {i} stores in the district: {create_prediction(i)}')



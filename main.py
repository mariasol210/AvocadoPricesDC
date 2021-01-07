import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Open the pkl file and store it as avocados
with open('avoplotto.pkl', 'rb') as f:
    avocados = pickle.load(f)

# Look at the first few rows of data
# print(avocados[avocados["year"]==2016])


# QUESTION: Which avocado size is most popular?
# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind='bar')

# Show the plot
# plt.show()


# QUESTION: Changes in sales over time
# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(x="date", y="nb_sold", kind="line")

# Show the plot
# plt.show()


# QUESTION: Avocado supply and demand
# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter",
              title="Number of avocados sold vs. average price")

# Show the plot
# plt.show()


# QUESTION: Price of conventional vs. organic avocados
# Histogram of conventional avg_price
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["Conventional", "Organic"])

# Show the plot
# plt.show()


# QUESTION: Finding missing values
# In DataCamp a subset with only sales from 2016 is used, but i don't have nor the subset nor the complete
# information to create the subset (individual sales by size is missing from avocados)

# Check individual values for missing values
print(avocados.isna())

# Check each column for missing values
print(avocados.isna().any())

# Bar plot of missing values by variable
avocados.isna().sum().plot(kind="bar")

# Show plot
plt.show()


# QUESTION: Removing missing values
# Remove rows with missing values
avocados_complete = avocados.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())


# QUESTION: Replacing missing values
# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()
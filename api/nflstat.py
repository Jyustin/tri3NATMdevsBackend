import pandas as pd

# Read the CSV file
df = pd.read_csv("api/nfl_offensive_stats.csv")

# Display the first few rows of the dataframe
print(df.head())

# Perform data analysis tasks on the dataframe
# Here are a few examples:

# Get the summary statistics of numerical columns
print(df.describe())

# Count the number of rows and columns in the dataframe
num_rows, num_cols = df.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

# Access specific columns

# Filter the dataframe based on conditions
filtered_df = df[df["Team"] == "New England Patriots"]
print(filtered_df)

# Group data by a column and calculate statistics
grouped_df = df.groupby("Team").mean()
print(grouped_df)

# Perform calculations on columns
df["Total_Yards"] = df["Passing_Yards"] + df["Rushing_Yards"]
print(df["Total_Yards"])



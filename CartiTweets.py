import pandas as pd

try:
    # Load the CSV file
    df = pd.read_csv("CartiTweets.csv")

    # Print the number of rows and columns
    print(f"CSV Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

    # Display the first 5 rows
    print("First 5 rows of the dataset:")
    print(df.head())

except Exception as e:
    print(f"Error loading CSV: {e}")

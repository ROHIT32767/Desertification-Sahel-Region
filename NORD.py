import pandas as pd
import plotly.express as px

# Create an empty DataFrame to store the data
data = pd.DataFrame()

# Define the years you want to analyze (2006 to 2015)
years = range(2006, 2016)

# Load data from CSV files for each year
for year in years:
    file_name = f'FLUX_NORD-{year}.csv'  # Adjust the file naming convention
    df = pd.read_csv(file_name)

    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Extract the month and year from the date
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year

    # Filter out rows with 'Cover Height Mean' equal to -9999.9 (assuming these are missing values)
    df = df[df['Cover Height Mean'] != -9999.9]

    # Concatenate the data into a single DataFrame
    data = pd.concat([data, df])

# Group the data by year and month, and calculate the mean 'Cover Height Mean'
monthly_mean = data.groupby(['Year', 'Month'])['Cover Height Mean'].mean().reset_index()

# Create a Plotly line chart to visualize the monthly trends
fig = px.line(monthly_mean, x='Month', y='Cover Height Mean', color='Year',
              labels={'Cover Height Mean': 'Average Cover Height Mean', 'Month': 'Month (1-12)'},
              title='Monthly Trends of Cover Height Mean (2006-2015)')

fig.show()

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Read the CSV file into a pandas DataFrame
df = pd.DataFrame({
    'Date': ['Mar-23', 'Mar-22', 'Mar-21', 'Mar-20', 'Mar-19', 'Mar-18'],
    'Tangible Assets': [12, 13, 14, 15, 10, 10],
    'Intangible Assets': [1, 1, 0, 0, 0, 0],
    'Capital Work-In-Progress': [1, 1, 1, 1, 1, 1],
    'Fixed Assets': [14, 15, 15, 16, 11, 12],
    'Non-Current Investments': [2, 2, 2, 2, 2, 2],
    'Deferred Tax Assets [Net]': [2, 2, 3, 2, 2, 3],
    'Long Term Loans And Advances': [0, 0, 0, 0, 0, 2],
    'Other Non-Current Assets': [4, 3, 3, 4, 6, 6],
    'Total Non-Current Assets': [23, 22, 24, 25, 21, 25],
    'Current Investments': [30, 24, 26, 24, 28, 39],
    'Inventories': [0, 0, 0, 0, 0, 0],
    'Trade Receivables': [36, 30, 23, 27, 24, 21],
    'Cash And Cash Equivalents': [4, 11, 3, 5, 9, 4],
    'Short Term Loans And Advances': [0, 5, 10, 7, 7, 3],
    'OtherCurrentAssets': [8, 8, 15, 12, 11, 9],
    'Total Current Assets': [77, 78, 76, 75, 79, 75],
    'Total Assets': [100, 100, 100, 100, 100, 100]
})

# Set the page title
st.title('Assets Analysis')

# Sidebar widgets for user input
selected_assets = st.sidebar.multiselect('Select Assets', df.columns[1:])

# Filter the DataFrame based on user input
filtered_df = df[['Date'] + selected_assets]

# Calculate the percentage change
filtered_df[selected_assets] = filtered_df[selected_assets].pct_change() * 100

# Plot the pie chart
pie_fig = go.Figure(data=go.Pie(labels=selected_assets, values=filtered_df.iloc[-1, 1:]))

# Plot the line graph
line_fig = px.line(filtered_df, x='Date', y=selected_assets)

# Plot the bar chart
bar_fig = px.bar(filtered_df, x='Date', y=selected_assets, barmode='group')

# Set the layout for the pie chart
pie_fig.update_layout(
    title='Percentage Distribution of Selected Assets',
    height=400
)

# Set the layout for the line graph
line_fig.update_layout(
    title='Percentage Change in Selected Assets Over Time', height=400
)

# Set the layout for the bar chart
bar_fig.update_layout(
    title='Percentage Change in Selected Assets Over Time',
    barmode='group',
    height=400
)

# Create a Streamlit layout to display the visualizations side by side


# Display the pie chart in the first column
st.plotly_chart(pie_fig, use_container_width=True)

# Display the line graph in the second column
st.plotly_chart(line_fig, use_container_width=True)

# Display the bar chart in the third column
st.plotly_chart(bar_fig, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="TCS Financial Statement Analysis", page_icon=":guardsman:", layout="wide")


def about():
    st.subheader("About the project")
    st.write("The project aims to analyze the financial statements of Tata Consultancy Services (TCS), one of the leading global IT services and consulting companies. TCS, a subsidiary of the Tata Group, has established itself as a frontrunner in the technology industry, providing a wide range of services including software development, consulting, and business process outsourcing. The financial statements of TCS, including the balance sheet, horizontal analysis, vertical analysis, profit and loss, cash flow and ratio analysis provide valuable insights into the company's financial performance, position, and cash flow dynamics. By conducting a comprehensive analysis of these statements, we can gain a deeper understanding of TCS's profitability, liquidity, solvency, and overall financial health. This project will delve into key financial ratios, trends, and patterns within the financial statements to evaluate TCS's financial performance and make informed assessments of its future prospects. Through this project, we aim to highlight the significance of financial statement analysis in assessing the financial strength and stability of a company like TCS. By examining the various components of TCS's financial statements, we can uncover valuable information that will contribute to a comprehensive evaluation of the company's financial position, aid in decision-making, and provide insights for potential investors, stakeholders, and industry enthusiasts.")
 



def balance_sheet():
    df = pd.read_csv("eq&liab.csv", header=0)
    df1 = pd.read_csv("assets.csv", header=0)
    col1, col2 = st.columns(2)
   
    with col1:
        st.header("Equity")
        st.dataframe(df, height=785)
    with col2:
        st.header("Assets")
        st.dataframe(df1, height=785)
    

    df2 = pd.DataFrame({
        'Date': ['Mar-23', 'Mar-22', 'Mar-21', 'Mar-20', 'Mar-19', 'Mar-18'],
        'Tangible Assets': [14881, 15506, 15697, 15883, 9522, 9430],
        'Intangible Assets': [809, 1018, 362, 239, 139, 10],
        'Capital Work-In-Progress': [1103, 1146, 861, 781, 834, 1238],
        'Fixed Assets': [16793, 17670, 16920, 16903, 10495, 10678],
        'Non-Current Investments': [2405, 2405, 2405, 2189, 2189, 2186],
        'Deferred Tax Assets [Net]': [2464, 2779, 3160, 2219, 2097, 3051],
        'Long Term Loans And Advances': [3, 8, 2, 2, 2, 1503],
        'Other Non-Current Assets': [5378, 4209, 3734, 4468, 5685, 5416],
        'Total Non-Current Assets': [27043, 27071, 26221, 25781, 20468, 22834],
        'Current Investments': [35738, 29262, 28324, 25686, 28280, 35073],
        'Inventories': [27, 19, 7, 5, 10, 25],
        'Trade Receivables': [42798, 36102, 25222, 28660, 24029, 18882],
        'Cash And Cash Equivalents': [4543, 13692, 3142, 4824, 8900, 3487],
        'Short Term Loans And Advances': [332, 5653, 10486, 7270, 7018, 2793],
        'OtherCurrentAssets': [9346, 9464, 15979, 12749, 10795, 7962],
        'Total Current Assets': [92784, 94192, 83160, 79194, 79032, 68222],
        'Total Assets': [119827, 121263, 109381, 104975, 99500, 91056],
        'Equity Share Capital (face value is Rs 1)': [366, 366, 370, 375, 375, 191],
        'Other Equity(Reserves and Surplus)': [74172, 76807, 74424, 73993, 78523, 75675],
        'Total Shareholders Funds(Equity)': [74538, 77173, 74794, 74368, 78898, 75866],
        'Long Term Borrowings': [0, 0, 0, 0, 0, 39],
        'Deferred Tax Liabilities [Net]': [190, 129, 365, 347, 339, 424],
        'Other Long Term Liabilities': [5775, 6060, 5697, 6234, 1367, 643],
        'Long Term Provisions': [0, 0, 0, 0, 0, 26],
        'Total Non-Current Liabilities': [5965, 6189, 6062, 6581, 1706, 1132],
        'Short Term Borrowings': [0, 0, 0, 0, 0, 181],
        'Trade Payables': [13768, 10082, 7962, 8734, 7692, 4775],
        'Other Current Liabilities': [25277, 26442, 19213, 15057, 11030, 8931],
        'Short Term Provisions': [279, 1377, 1350, 235, 174, 171],
        'Total Current Liabilities': [39324, 37901, 28525, 24026, 18896, 14058],
        'Total Liabilites': [45289, 44090, 34587, 30607, 20602, 15190],
        'Total Capital And Liabilities': [119827, 121263, 109381, 104975, 99500, 91056]
    })

    # Set the page title
    st.title('Asset Trends')

    # Get the column names representing the assets
    selected_assets = st.sidebar.multiselect('Select Assets', df2.columns[1:])

# Filter the DataFrame based on user input
    filtered_df = df2[['Date'] + selected_assets]

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
    

    # Display the line graph in the second column
    st.plotly_chart(line_fig, use_container_width=True)

    # Display the bar chart in the third column
    st.plotly_chart(bar_fig, use_container_width=True)
    
    st.plotly_chart(pie_fig, use_container_width=True)


def horizontal():
    df3 = pd.read_csv("HA1.csv", header=0)
    df4 = pd.read_csv("HA2.csv", header=0)
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Equity")
        st.dataframe(df3, height=785)
    with col2:
        st.header("Assets")
        st.dataframe(df4, height=785, )
    

    df5 = pd.DataFrame({
        'Date': ['23-Mar', '22-Mar', '21-Mar', '20-Mar', '19-Mar', '18-Mar'],
        'Equity Share Capital (face value is Rs 1)': [192, 192, 194, 196, 196, 100],
        'Other Equity(Reserves and Surplus)': [98, 101, 98, 98, 104, 100],
        'Total Shareholders Funds(Equity)': [98, 102, 99, 98, 104, 100],
        'Long Term Borrowings': [0, 0, 0, 0, 0, 100],
        'Deferred Tax Liabilities [Net]': [45, 30, 86, 82, 80, 100],
        'Other Long Term Liabilities': [898, 942, 886, 970, 213, 100],
        'Long Term Provisions': [0, 0, 0, 0, 0, 100],
        'Total Non-Current Liabilities': [527, 547, 536, 581, 151, 100],
        'Short Term Borrowings': [0, 0, 0, 0, 0, 100],
        'Trade Payables': [288, 211, 167, 183, 161, 100],
        'Other Current Liabilities': [283, 296, 215, 169, 124, 100],
        'Short Term Provisions': [163, 805, 789, 137, 102, 100],
        'Total Current Liabilities': [280, 270, 203, 171, 134, 100],
        'Total Liabilites': [298, 290, 228, 201, 136, 100],
        'Total Capital And Liabilities': [132, 133, 120, 115, 109, 100],
        'Tangible Assets': [158, 164, 166, 168, 101, 100],
        'Intangible Assets': [8090, 10180, 3620, 2390, 1390, 100],
        'Capital Work-In-Progress': [89, 93, 70, 63, 67, 100],
        'Fixed Assets': [157, 165, 158, 158, 98, 100],
        'Non-Current Investments': [110, 110, 110, 100, 100, 100],
        'Deferred Tax Assets [Net]': [81, 91, 104, 73, 69, 100],
        'Long Term Loans And Advances': [0, 1, 0, 0, 0, 100],
        'Other Non-Current Assets': [99, 78, 69, 82, 105, 100],
        'Total Non-Current Assets': [118, 119, 115, 113, 90, 100],
        'Current Investments': [102, 83, 81, 73, 81, 100],
        'Inventories': [108, 76, 28, 20, 40, 100],
        'Trade Receivables': [227, 191, 134, 152, 127, 100],
        'Cash And Cash Equivalents': [130, 393, 90, 138, 255, 100],
        'Short Term Loans And Advances': [12, 202, 375, 260, 251, 100],
        'OtherCurrentAssets': [117, 119, 201, 160, 136, 100],
        'Total Current Assets': [136, 138, 122, 116, 116, 100],
        'Total Assets': [132, 133, 120, 115, 109, 100]
    })

    # Set the page title
    st.title('Asset Trends')

    # Get the column names representing the assets
    selected_assets = st.sidebar.multiselect('Select Assets', df5.columns[1:])

# Filter the DataFrame based on user input
    filtered_df = df5[['Date'] + selected_assets]

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
    

    # Display the line graph in the second column
    st.plotly_chart(line_fig, use_container_width=True)

    # Display the bar chart in the third column
    st.plotly_chart(bar_fig, use_container_width=True)

    st.plotly_chart(pie_fig, use_container_width=True)

def vertical():
    df6 = pd.read_csv("VA1.csv", header=0)
    df7 = pd.read_csv("VA2.csv", header=0)
    col1, col2 = st.columns(2)
   
    with col1:
        st.header("Equity")
        st.dataframe(df6, height=785)
    with col2:
        st.header("Assets")
        st.dataframe(df7, height=785)
    

    df8 = pd.DataFrame({
        'Date': ['23-Mar', '22-Mar', '21-Mar', '20-Mar', '19-Mar', '18-Mar'],
        'Equity Share Capital': [0, 0, 0, 0, 0, 0],
        'Other Equity(Reserves and Surplus)': [62, 63, 68, 70, 79, 83],
        'Total Shareholders Funds(Equity)': [62, 64, 68, 71, 79, 83],
        'Long Term Borrowings': [0, 0, 0, 0, 0, 0],
        'Deferred Tax Liabilities [Net]': [0, 0, 0, 0, 0, 0],
        'Other Long Term Liabilities': [5, 5, 5, 6, 1, 1],
        'Long Term Provisions': [0, 0, 0, 0, 0, 0],
        'Total Non-Current Liabilities': [5, 5, 6, 6, 2, 1],
        'Short Term Borrowings': [0, 0, 0, 0, 0, 0],
        'Trade Payables': [11, 8, 7, 8, 8, 5],
        'Other Current Liabilities': [21, 22, 18, 14, 11, 10],
        'Short Term Provisions': [0, 1, 1, 0, 0, 0],
        'Total Current Liabilities': [33, 31, 26, 23, 19, 15],
        'Total Liabilities': [38, 36, 32, 29, 21, 17],
        'Total Capital And Liabilities': [100, 100, 100, 100, 100, 100],
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
    st.title('Asset Trends')

    # Get the column names representing the assets
    selected_assets = st.sidebar.multiselect('Select Assets', df8.columns[1:])

# Filter the DataFrame based on user input
    filtered_df = df8[['Date'] + selected_assets]

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
    

    # Display the line graph in the second column
    st.plotly_chart(line_fig, use_container_width=True)

    # Display the bar chart in the third column
    st.plotly_chart(bar_fig, use_container_width=True)
    
    st.plotly_chart(pie_fig, use_container_width=True)

def app():
    st.write("<div style='text-align: center'><h1>TCS Financial Statement Analysis</h1></div>", unsafe_allow_html=True)
    pages = {
        "About": about,
        "Balance Sheet": balance_sheet,
        "Horizontal Analysis": horizontal,
        "Vertical Analysis": vertical,
    }
    st.sidebar.title("Navigation")
    selection = st.sidebar.selectbox("Go to", list(pages.keys()))
    page = pages[selection]
    page()


def main():
    app()


if __name__ == "__main__":
    main()

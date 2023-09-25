import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

suiciderates = pd.read_csv('suicide_rates.csv')

# Calculate the suicide rate
suiciderates['suicide_rate'] = suiciderates['suicides_no'] / suiciderates['population']
# Or use suicides/100k pop like i did below

# Sort the DataFrame by year
suiciderates = suiciderates.sort_values(by="year")

def create_suicide_rate_map(year):
    # Filter the DataFrame by the selected year
    year_filtered = suiciderates[suiciderates['year'] == year]

    # Calculate the suicide rate for the filtered data
    year_filtered['suicide_rate'] = year_filtered['suicides_no'] / year_filtered['population']

    # Create the choropleth map
    fig_map = px.choropleth(
        year_filtered,
        locations="country",
        locationmode='country names',
        color="suicide_rate",
        hover_name="country",
        projection="natural earth",
        title=f"Suicide Rate by Country in {year}",
        color_continuous_scale=px.colors.sequential.Viridis,
        labels={'suicide_rate': 'Suicide Rate'},
    )

    fig_map.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")

    return fig_map

def main():
    st.title("Suicide Rates between 1985 and 2016 per country")
    st.write("This visualization displays an animated map of suicide rates by country over time.")
    
    st.sidebar.title("Year Selector")
    
    # Place the year slider in the sidebar
    selected_year = st.sidebar.slider('year', min_value=1985, max_value=2016, value=1985, step=1)

    # Create the suicide rate map for the selected year
    fig = create_suicide_rate_map(selected_year)

    # Display the map in the Streamlit app
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()


# Add a horizontal line to separate visuals
st.markdown("<hr>", unsafe_allow_html=True)

# Set the title for your Streamlit app
st.title('Suicide number across Gender')


# Read data from the CSV file
suiciderates = pd.read_csv('suicide_rates.csv')

# Calculate the suicide rate
suiciderates['suicide_rate'] = suiciderates['suicides_no'] / suiciderates['population']

# Sort the DataFrame by year
suiciderates = suiciderates.sort_values(by="year")

# Define colors for the bar chart
colors = ['#1f77b4', '#ff7f0e']

# Sidebar
st.sidebar.title("Gender Selector")
gender = st.sidebar.selectbox("Select Gender", ['Male', 'Female', 'Both'])

# Filter data based on the selected gender
if gender == 'Male':
    filtered_data = suiciderates[suiciderates['sex'] == 'male']
    title = 'Total Suicides by Male'
elif gender == 'Female':
    filtered_data = suiciderates[suiciderates['sex'] == 'female']
    title = 'Total Suicides by Female'
else:
    filtered_data = suiciderates
    title = 'Total Suicides by Gender'

# Create bar chart
fig4 = px.bar(filtered_data, x='sex', y='suicides_no', color='sex',
              title=title,
              labels={'suicides_no': 'Total Suicides'},
              color_discrete_sequence=colors)

# Display the bar chart
st.plotly_chart(fig4)


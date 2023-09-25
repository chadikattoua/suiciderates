#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:51:15 2023

@author: chadikattouah
"""

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


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


# Load your data
suiciderates = pd.read_csv('/Users/chadikattouah/Downloads/suicide_rates.csv')

# Calculate the suicide rate
suiciderates['suicide_rate'] = suiciderates['suicides_no'] / suiciderates['population']

# Sort the DataFrame by year
suiciderates = suiciderates.sort_values(by="year")

# Define categories for suicides/100k pop
suiciderates['suicide_category'] = pd.cut(
    suiciderates['suicides/100k pop'],
    bins=[0, 50, 100, float('inf')],
    labels=['Low', 'Mid', 'High']
)

# Create the grouped bar chart
fig_gdp_vs_suicides = px.bar(
    suiciderates,
    x='suicide_category',
    y='gdp_per_capita ($)',
    title='animated barchart',
    labels={'gdp_per_capita ($)': 'GDP per Capita', 'suicides/100k pop': 'Suicides per 100k Population'},
    color='suicide_category',
    hover_name='country',
    animation_frame='country',
    color_discrete_map={
        'Low': 'green',
        'Mid': 'orange',
        'High': 'red'
    },
    category_orders={"suicide_category": ["Low", "Mid", "High"]},
    text='gdp_per_capita ($)',
    height=500,
    width=800
)

fig_gdp_vs_suicides.update_xaxes(title_text="Suicide Category")
fig_gdp_vs_suicides.update_yaxes(title_text="GDP per Capita ($)")

fig_gdp_vs_suicides.update_layout(
    title_x=0.5,
    title_font=dict(size=20),
)

fig_gdp_vs_suicides.update_layout(
    legend_title_text='Suicide Category',
    legend=dict(
        x=1,
        y=1,
    )
)

# Set the title for your Streamlit app
st.title('GDP per Capita vs. Suicides per 100k Population')

# Display the chart
st.plotly_chart(fig_gdp_vs_suicides)


# Add a horizontal line to separate visuals
st.markdown("<hr>", unsafe_allow_html=True)

# Set the title for your Streamlit app
st.title('Suicide number across Gender')


# Read data from the CSV file
suiciderates = pd.read_csv('/Users/chadikattouah/Downloads/suicide_rates.csv')

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


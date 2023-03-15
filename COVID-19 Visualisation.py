import pycountry
import plotly.express as px
import pandas as pd

# Step 1: Load the dataset
url_dataset = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(url_dataset)

# Step 2: Map country names to ISO codes
countries = df['Country'].unique().tolist()
country_codes = {}
for country in countries:
    try:
        country_data = pycountry.countries.search_fuzzy(country)[0]
        country_codes[country] = country_data.alpha_3
    except:
        country_codes[country] = ' '
df['iso_alpha'] = df['Country'].map(country_codes)

# Step 3: Visualize the data on a choropleth map
fig = px.choropleth(
    data_frame=df,
    locations='iso_alpha',
    color='Confirmed',
    hover_name='Country',
    color_continuous_scale='RdYlGn',
    animation_frame='Date'
)
fig.show()

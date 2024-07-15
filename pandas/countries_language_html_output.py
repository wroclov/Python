import folium
import json

# Example data: A dictionary with country codes and their dominant language
language_data = {
    'USA': 'English',
    'FRA': 'French',
    'ESP': 'Spanish',
    'CAN': 'English',
    'BRA': 'Portuguese',
    'RUS': 'Russian',
    'POR': 'Portuguese'

    # Add more countries and their dominant languages
}

# Define a color mapping for the top languages
language_colors = {
    'English': 'blue',
    'French': 'green',
    'Spanish': 'red',
    'Portuguese': 'purple',
    'Russian': 'grey'
    # Add more languages if needed
}

# Load GeoJSON data for world countries
with open('path/countries.geojson', 'r') as f:
    countries_geojson = json.load(f)

# Print properties of the first few countries to inspect the structure
for feature in countries_geojson['features'][:5]:
    print(feature['properties'])

print(countries_geojson['features'][0]['properties'])

# Create a map centered around a specific location
m = folium.Map(location=[20, 0], zoom_start=2)

# Function to get the color based on the dominant language
def get_color(language):
    return language_colors.get(language, 'gray')  # Default color if language not found

# Add GeoJSON to the map
folium.GeoJson(
    countries_geojson,
    style_function=lambda feature: {
        'fillColor': get_color(language_data.get(feature['properties']['sov_a3'], '')),
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.6,
    }
).add_to(m)

# Add a legend to the map
legend_html = '''
     <div style="position: fixed;
     bottom: 50px; left: 50px; width: 150px; height: 150px;
     border:2px solid grey; z-index:9999; font-size:14px;
     ">&nbsp; Dominant Languages <br>
     &nbsp; <i class="fa fa-circle fa-1x" style="color:blue"></i>&nbsp; English <br>
     &nbsp; <i class="fa fa-circle fa-1x" style="color:green"></i>&nbsp; French <br>
     &nbsp; <i class="fa fa-circle fa-1x" style="color:red"></i>&nbsp; Spanish <br>
     &nbsp; <i class="fa fa-circle fa-1x" style="color:purple"></i>&nbsp; Portuguese <br>
     &nbsp; <i class="fa fa-circle fa-1x" style="color:grey"></i>&nbsp; Russian <br>
     </div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

# Save the map to an HTML file
m.save("language_map.html")

print("Map saved as language_map.html")


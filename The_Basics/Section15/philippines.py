import folium
import pandas as pd


data = pd.read_csv("Volcanoes.txt")
latitudes = list(data["LAT"])
longitudes = list(data["LON"])
elevations = list(data["ELEV"])
names = list(data["NAME"])

html = """
Volcano name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
Height: %s m
"""


def color_producer(elevation):

    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lat, lon, elevation, name in zip(latitudes, longitudes, elevations, names):
    iframe = folium.IFrame(html=html % (
        name, name, elevation), width=140, height=75)

    fgv.add_child(folium.vector_layers.CircleMarker(location=[lat, lon], radius=6,
                                                    popup=folium.Popup(iframe), fill_color=color_producer(elevation), color='black', fill_opacity=0.7))

    # Pin Marker
    # fg.add_child(folium.Marker(location=[lat, lon],
    #              popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(elevation))))

    # old style
    # fg.add_child(folium.Marker(location=[lat, lon],
    #              popup=folium.Popup(name + "\n " + str(elevation) , parse_html=True), icon=folium.Icon(color='green')))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                       else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Philippines.html")

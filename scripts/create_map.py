import base64
import webbrowser
import folium
from IPython.core.display_functions import display
from folium import plugins
import ee
import os, sys

from folium.plugins import FloatImage
from IPython.display import HTML

workdir = os.path.dirname(os.path.dirname(__file__))

sys.path.append(workdir)

from scripts.ee_handler import basemaps
from scripts.map_overlay import color_dict, position, class_geojson_from_pos


def create_map(position):
    # ee.Authenticate()
    # ee.Initialize()

    my_map = folium.Map(location=[20, 0], zoom_start=3, height=500)
    m = folium.Map(location=position,
                   zoom_start=13)

    geojson = class_geojson_from_pos(position)

    # # Add custom basemaps
    # basemaps['Google Maps'].add_to(m)
    # basemaps['Google Satellite Hybrid'].add_to(m)

    styler = lambda x: {
        "fillOpacity": 0.3,
        "weight": 0,
        "fillColor": color_dict[int(x['properties']['class'])],
    }
    folium.GeoJson('./json_data.json', name="geojson", style_function=styler).add_to(m)

    legend_img = 'legend.png'

    with open(legend_img, 'rb') as lf:
        # open in binary mode, read bytes, encode, decode obtained bytes as utf-8 string
        b64_content = base64.b64encode(lf.read()).decode('utf-8')

    FloatImage('data:image/png;base64,{}'.format(b64_content), bottom=0, left=86).add_to(m)

    # # Add the elevation model to the map object.
    # my_map.add_ee_layer(dem.updateMask(dem.gt(0)), vis_params, 'DEM')

    # Add a layer control panel to the map.
    m.add_child(folium.LayerControl())

    # Add fullscreen button
    plugins.Fullscreen().add_to(m)

    m.save('map.html')
    webbrowser.open("map.html")

if __name__ == '__main__':
    create_map(position)
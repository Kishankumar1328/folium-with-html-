import folium

# Create a map centered around Tamil Nadu
map = folium.Map(location=(11.1271, 78.387451), zoom_start=8)

# Yercaud
yercaud_marker = folium.Marker(
    location=[11.77, 78.21],
    tooltip="Yercaud",
    icon=folium.Icon(icon='cloud', icon_color="white", color="darkblue"),
    popup=folium.Html(
        "<h1>King Of Eastern Ghats</h1>"
        "<img src='C:/Users/krss1/OneDrive/Pictures/folium pic/yercaud1.jpg'>"
        "<p>Nestled 'midst emerald hills, Yercaud's allure unfolds,<br>"
        "Whispers of serenity in mist-kissed tales, a tranquil haven to behold</p>",
        script=True
    )
).add_to(map)
folium.Circle(location=(11.77, 78.21), radius=5000, popup="Hill Station", color="blue", fill=True,fill_color="blue").add_to(map)

# Kodaikanal
kodikanal_marker = folium.Marker(
    location=[10.23, 77.49],
    tooltip="Kodaikanal",
    icon=folium.Icon(icon='cloud', icon_color="white", color="darkblue"),
    popup=folium.Html(
        "<h1>The Princess of Hill Stations</h1>"
        "<img src='C:/Users/krss1/OneDrive/Pictures/folium pic/kodaikanal.jpg'>"
        "<p>Amidst the mist-kissed embrace of Kodai's hills,<br>"
        "Nature's canvas unfolds, a tranquil haven that serenity instills.</p>",
        script=True
    )
).add_to(map)
folium.Circle(location=(10.23, 77.49), radius=5000, popup="Hill Station", color="blue", fill=True,fill_color="blue").add_to(map)

# Ooty
ooty_marker = folium.Marker(
    location=[11.410000, 76.699997],
    tooltip="Ooty",
    icon=folium.Icon(icon='cloud', icon_color="white", color="darkblue"),
    popup=folium.Html(
        "<h1>Queen of the Hills</h1>"
        "<img src='C:/Users/krss1/OneDrive/Pictures/folium pic/ooty.jpg'>"
        "<p>In Ooty's emerald embrace, the Nilgiri's whispers unfold,<br>"
        "A symphony of mist and tea, where tales of serenity are told.</p>",
        script=True
    )
).add_to(map)
folium.Circle(location=(11.410000, 76.699997), radius=5000, popup="Hill Station", color="blue", fill=True,
              fill_color="blue").add_to(map)

# Yelagiri
yelagiri_marker = folium.Marker(
    location=[12.59, 78.63],
    tooltip="Yelagiri",
    icon=folium.Icon(icon='cloud', icon_color="white", color="darkblue"),
    popup=folium.Html(
        "<h1>Poor Man's Ooty</h1>"
        "<img src='C:/Users/krss1/Downloads/yelagiri.jpg'>"
        "<p>Yelagiri's verdant hills weave tales of tranquility,<br>"
        "Nature's poetry unfolds, a serene retreat of simplicity.</p>",
        script=True
    )
).add_to(map)
folium.Circle(location=(12.59, 78.63), radius=5000, popup="Hill Station", color="blue", fill=True,fill_color="blue").add_to(map)

# Save the map
map.save("famous_hill_stations_in_tamilnadu.html")

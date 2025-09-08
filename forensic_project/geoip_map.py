import geoip2.database
import folium

def generate_geo_map(ip_list, db_path='GeoLite2-City.mmdb', output_file='attack_map.html'):
    reader = geoip2.database.Reader(db_path)
    world_map = folium.Map(location=[20,0], zoom_start=2)

    for ip in ip_list:
        try:
            response = reader.city(ip)
            lat = response.location.latitude
            lon = response.location.longitude
            if lat and lon:
                folium.Marker([lat, lon], popup=ip).add_to(world_map)
        except:
            continue  # skip if not resolvable (local/fake IPs)

    world_map.save(output_file)
    print(f"Map saved as {output_file}")

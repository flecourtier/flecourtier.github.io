# Leaflet cluster map of talk and poster locations
#
# Scrapes the location YAML field from each .md file in _talks/ and _posters/,
# geolocates it with geopy/Nominatim, and generates an interactive map with
# color-coded markers (red for talks, blue for posters).
import frontmatter
import glob
import json
import time

from geopy import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

# Set the default timeout, in seconds
TIMEOUT = 5

# Collect the Markdown files from both talks and posters
# Adjust paths to work from talkmap directory
g = glob.glob("../_talks/*.md") + glob.glob("../_posters/*.md")

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_data = []  # List of dicts: {description, lat, lon, type, color}
location = ""
permalink = ""
title = ""


def is_virtual_location(value):
    if not value:
        return False
    lowered = value.lower()
    return "visioconf" in lowered or "visio" in lowered or "online" in lowered or "zoom" in lowered


def geocode_with_fallback(primary, fallback):
    for query in (primary, fallback):
        if not query:
            continue
        try:
            result = geocoder.geocode(query, timeout=TIMEOUT)
        except (GeocoderTimedOut, GeocoderUnavailable, ValueError) as ex:
            print(f"Error: geocode failed on input {query} with message {ex}")
            result = None
        time.sleep(1)
        if result:
            return result, query
    return None, None

# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Only show items explicitly enabled for the map
    if not data.get('showonmap', False):
        continue

    # Determine type (talk or poster) and color
    item_type = data.get('collection', 'talk')  # 'talks' or 'posters'
    if 'poster' in item_type:
        item_type = 'poster'
        color = '#2E5CA6'  # Blue for posters
    else:
        item_type = 'talk'
        color = '#D62828'  # Red for talks

    # Prepare the description
    title = data.get('title', '').strip()
    location = data.get('location', '').strip()
    if is_virtual_location(location):
        location = ""
    if location:
        description = f"{title}<br />{location}"
    else:
        description = title

    # Geocode the location and report the status
    result, used_query = geocode_with_fallback(location, location)
    if not result:
        print(f"Warning: geocode returned no result for {description}")
        continue
    
    # Get permalink for link to full page
    permalink = data.get('permalink', '')
    
    location_data.append({
        'description': description,
        'latitude': result.latitude,
        'longitude': result.longitude,
        'type': item_type,
        'color': color,
        'permalink': permalink
    })
    print(description, f"(geocoded from: {used_query})", f"[{item_type}]", result)

# Save the map data as org-locations.js
import json
with open('org-locations.js', 'w', encoding='utf-8') as f:
    f.write('var addressPoints = ')
    json.dump(location_data, f, ensure_ascii=False, indent=2)
    f.write(';\n')

print(f"\nGenerated org-locations.js with {len(location_data)} points")
print(f"  - Talks (red): {sum(1 for x in location_data if x['type'] == 'talk')}")
print(f"  - Posters (blue): {sum(1 for x in location_data if x['type'] == 'poster')}")

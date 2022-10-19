from pyproj import Proj, transform
import pandas as pd
import json

df = pd.read_csv('train.csv')
#print(df)


# UTM-K
proj_UTMK = Proj(init='epsg:5178')

# WGS1984
proj_WGS84 = Proj(init='epsg:4326')

# convert json format
traj_json = json.loads('{"data":'+df['POLYLINE'][0]+"}")

data = []
for i in traj_json['data']:
    x1, y1 = i
    # UTMK -> WGS84
    x2, y2, = transform(proj_UTMK, proj_WGS84, x1, y1)
    data.append([x2, y2])

print(data)

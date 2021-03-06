
import random
import requests
import io
from PIL import Image


lat_lon = {}
#first 2 arrays make urban data, last two make rural
latitude = [
            43.73931091,
            43.64126107,
            43.87291998,
            43.70223921,
            43.9158961,
            43.87116378,
            43.53525341,
            43.49838054,
            45.46521155,
            45.3704906,
            48.38823395,
            48.36415436,
            48.46017072,
            48.39288556,
            43.38593494,
            43.35295402,
            43.00541457,
            42.94848924,
            48.49056051,
            48.46293814,
            46.47787941,
            46.46044087,
            44.4098766,
            44.32530104,
            43.47854254,
            43.41510627

            ]

longditude = [
            -79.80803609008086,
            -79.3307547944647,
            -79.58914712967197,
            -79.22293411492061,
            -78.96336960896963,
            -78.82261885397327,
            -79.90763199443325,
            -79.84490843493369,
            -75.8215771217328,
            -75.59806995265932,
            -89.31268043634205,
            -89.25697631162211,
            -89.27346981884926,
            -89.22168670260514,
            -81.0054983159572,
            -80.95989542673489,
            -82.45427937893163,
            -82.34938446972396,
            -81.35173315776723,
            -81.31433691410514,
            -81.03187351757102,
            -81.00095381395263,
            -79.72957799917188,
            -79.68721742635673,
            -80.54920477608853,
            -80.46768858061829

            ]

lats = [
        43.837498549851645,
        43.76216815555821,
        44.24667465368694,
        44.14279782818058,
        42.84073051691987,
        42.6450712987999,
        42.21478796951033,
        42.14355068927749,
        47.47637579720936,
        46.66451741754238,
        54.41892996865827,        
        51.699799849741936,
        49.160154652338015,
        48.20271028869975,
        43.952540557050675,
        43.905313639187
        ]

longs = [
        -81.25831604003908,
        -80.91636657714845,
        -80.77011108398439,
        -79.94201660156251,
        -82.32330322265626,
        -81.93878173828126,
        -82.73117065429689,
        -82.37274169921876,
        -84.21569824218751,
        -81.26586914062501,         
        -86.396484375,
        -83.80371093750001,
        -92.16979980468751,
        -89.90112304687501,
        -79.21726226806642,
        -79.06345367431642

         ]

def gen_pts(lat1, lon1, lat2, lon2):
    coords = {}
    for j in range (0,500):
        x = random.uniform(lats[i*2], lats[(i*2)+1])
        y = random.uniform(longs[i*2], longs[(i*2)+1])

        coords[j] = [x,y]
    return coords


for i in range(0,5):
    lat_lon[i] = gen_pts(lats[i*2], longs[i*2], lats[(i*2)+1], longs[(i*2)+1])
m = 4000
for k in range(0,5):
    for l in range(0,500):
        coord = lat_lon[k][l]
        lat = coord[0]
        lon = coord[1]

        img = requests.get("https://dev.virtualearth.net/REST/v1/Imagery/Map/Aerial?pp=" + str(lat) + "," + str(lon) + ";;1&mapSize=800,800&key=Anz84uRE1RULeLwuJ0qKu5amcu5rugRXy1vKc27wUaKVyIv1SVZrUjqaOfXJJoI0")
        path = "rural." + str(m) + ".jpeg"

        if img.status_code == 200:
            with open(path, 'wb') as f:
                f.write(img.content)
                
        m = m + 1    


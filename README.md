# Aerial-Image-Retrieval

##### Verbose Tile
Satellite Aerial Imagery Retrieval From Bing Maps
##### Input Parameters
Geographic Co-ordinates

Permissibe Formats: 

&nbsp;&nbsp;&nbsp;&nbsp;WGS84,

&nbsp;&nbsp;&nbsp;&nbsp;Sexagesimal degrees

&nbsp;&nbsp;&nbsp;&nbsp;Decimal degrees

Accesses Bing Maps API

&nbsp;&nbsp;&nbsp;&nbsp;Link: https://docs.microsoft.com/en-us/bingmaps/rest-services/
##### Output
Imagery in .jpeg file format, centered at coodinate
##### Usage
In the command line,

&nbsp;&nbsp;&nbsp;&nbsp;To return image:
```sh
$ python -c 'import aerial_retrieval.py; img_get(<coordinate>)'
```

License
----
GNU

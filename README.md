A script which can scrap the data for a few sensors in the luftdaten.info archiv:

http://archive.luftdaten.info/

In order to get the IDs of Sensors in an area, you can use QGIS and use the intersect function in a convex hull produced with a shp or any polygon.

In Terminal:

python3 PATH/recup_data.py

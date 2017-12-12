import py2neo
from py2neo import Graph, Node, Relationship
import requests
import json

#open Graph database
graph=Graph("localhost")  #depend on your authorization choice


#send url to get your current location #can use better method to get the division automatically as well
send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lati = j['latitude']
longi = j['longitude']

#query for the match your location with the restaurant
query='''
WITH point({latitude:{lat},longitude:{lon}}) AS mapcenter
   MATCH (a:Restaurant)-[:IN_DIVISION]->(b:Division{e_name:{division}}) 
   WITH a, distance (point({latitude: a.latitude, longitude: a.longitude}), mapcenter) AS distance 
     //near you but we can just do the limit so that only shows
   RETURN a.shopId, distance
   ORDER BY distance LIMIT 1000
'''
lat=24.8229533748
lon=121.771853579
division="Jiaoxi Township"
graph.run(query,lat=lati,lon=longi,division=division).data()
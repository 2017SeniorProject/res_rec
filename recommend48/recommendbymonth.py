import py2neo
from py2neo import Graph, Node, Relationship

#open Graph database
graph=Graph("localhost")  #depend on your authorization choice


#recommendation for restaurant by month: ranking the the restaurant by their review rating: most high reviews(SDRate>3) of the month
query='''
match (d:Division{e_name:{division}})-[:IN_MONTH]->(m:Month{month:{month}})
match	(m)<-[:WRITTEN_IN]-(r:Review)
match   (r)-[:ABOUT]->(n:Restaurant) where r.SDRate>3
return n.shopId, count(r) as count order by count desc
'''
month=1
division="Jiaoxi Township"
graph.run(query,month=month,division=division).data()
graph.run(query,month=month,division=division).data()
from cassandra.cluster import Cluster

cluster = Cluster(['localhost'], port=9042)
session = cluster.connect('books', wait_for_all_pools=True)
session.execute('USE books')
rows = session.execute('SELECT * FROM BOOK')
for row in rows:
    print(row)
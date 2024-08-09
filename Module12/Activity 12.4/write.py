from cassandra.cluster import Cluster
keyspace = None
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect(keyspace)

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS books
    WITH REPLICATION = {'class':'SimpleStrategy','replication_factor' :1};
    """)

session.set_keyspace('books')

session.execute("""
    CREATE TABLE IF NOT EXISTS book (
        BOOK_ID int PRIMARY KEY,
        Name text,
        Author text,
        Year_Published int,
        Number_of_Pages int
    );
""")

session.execute("""
    INSERT INTO book (BOOK_ID, Name, Author, Year_Published, Number_of_Pages)
    VALUES (1, 'The Mystery of Capital', 'Hernando de Soto', 1970, 209);
""")

session.execute("""
    INSERT INTO book (BOOK_ID, Name, Author, Year_Published, Number_of_Pages)
    VALUES (2, 'Fairy Tales', 'Hans Christian Andersen', 1836, 784);
""")

session.execute("""
    INSERT INTO book (BOOK_ID, Name, Author, Year_Published, Number_of_Pages)
    VALUES (3, 'The Divine Comedy', 'Dante Alighieri', 1315, 928);
""")

session.execute("""
    INSERT INTO book (BOOK_ID, Name, Author, Year_Published, Number_of_Pages)
    VALUES (4, 'Romeo and Juliet', 'William Shakespeare', 1597, 100);
""")

session.execute("""
    INSERT INTO book (BOOK_ID, Name, Author, Year_Published, Number_of_Pages)
    VALUES (5, 'Hamlet', 'William Shakespeare', 1603, 100);
""")
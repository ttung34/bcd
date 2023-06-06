import psycopg2

conn = psycopg2.connect(host="localhost", dbname ="postgers", user="postgres",
                        password="thanhtung3434342004", port=5432 )

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person(
    id INT PRIMARY KEY,
    name VARCAHR(250),
    age INT,
    gender CHAR
);
""")

#do sth

conn.commit()

cur.close()
conn.close()
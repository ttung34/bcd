import psycopg2

hostname = 'localhost'
database = 'demo'
username = 'posrgers'
pwd ='thanhtung343434342004'
port_id = 5432

conn = psycopg2.connect(
            host = hostname,
            dbname =database,
            user =username,
            password =pwd,
            port =port_id)


conn.close()

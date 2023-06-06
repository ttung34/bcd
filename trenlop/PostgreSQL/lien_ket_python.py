from sqlalchemy import create_engine
from sqlalchemy.sql import text 
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:thanhtung3434342004 @127.0.0.1:5432/Python")
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute(text("SELECT origin, destination, duration FROM flights")).fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")
        
if __name__ == "__main__":
    main()
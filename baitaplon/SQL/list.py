from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:trinhthanhtung30@127.0.0.2:5432/ORM")
db = scoped_session(sessionmaker(bind=engine))

def main():
    diemsv= db.execute("SLECET id, hotensv, diem_a, diem_b, diem_c").fetchall()
    for diem in diemsv:
        print(f"{diem.id}, {diem.hotensv}, {diem.diem_a}, {diem.diem_b}, {diem.diem_c}")

main()

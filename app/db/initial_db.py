# app/db/initial_db.py

from app.db.base import Base
from app.db.session import engine

def init_db():
    print("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created.")

if __name__ == "__main__":
    init_db()


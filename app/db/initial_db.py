from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.models.user import User
from app.core.security import hash_password  # or wherever you hash passwords

def init_db():
    print("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created.")

    db = SessionLocal()
    existing = db.query(User).filter(User.email == "demo@example.com").first()
    if not existing:
        user = User(
            email="demo@example.com",
            hashed_password=hash_password("demo123"),  # ensure hashing is done
            full_name="Demo User",
            is_active=True,
        )
        db.add(user)
        db.commit()
        print("Demo user created.")
    else:
        print("Demo user already exists.")
    db.close()

if __name__ == "__main__":
    init_db()

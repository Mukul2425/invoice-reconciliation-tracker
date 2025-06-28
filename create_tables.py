from app.models.user import Base
from app.core.db import engine

# Create all tables
Base.metadata.create_all(bind=engine)


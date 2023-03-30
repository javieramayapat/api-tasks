from .config.database import SessionLocal


def get_db():
    """Create a session local to interact with database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
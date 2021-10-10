from sqlalchemy.engine import create_engine, URL
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from .config import settings

DB_URL = "postgresql://root:root@localhost:25432/root"

engine = create_engine(URL(**settings.db_config))
SessionLocal = sessionmaker(bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

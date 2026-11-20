from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRESQL_URL = "postgresql+psycopg://postgres:0704Cs221023%40@localhost:5432/auth_db"

engine = create_engine(POSTGRESQL_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
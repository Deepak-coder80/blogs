from sqlalchemy import create_engine

#data mapping
from sqlalchemy.ext.declarative import declarative_base

#session
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread":False})


#data mapping
Base = declarative_base()

#session
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
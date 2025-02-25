import sqlalchemy as db

from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


engine = db.create_engine(os.getenv("DATABASE_URL"))
connection = engine.connect()
metadata = db.MetaData()
Base = declarative_base()


class Books(Base):
    __tablename__ = 'books'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(255), unique=True, nullable=False)
    publication_time = db.Column(db.DateTime)
    genre = db.Column(db.String(255))
    price = db.Column(db.Float())
    quantity = db.Column(db.Integer())

Base.metadata.create_all(engine)

connection.commit()

connection.close()
engine.dispose()



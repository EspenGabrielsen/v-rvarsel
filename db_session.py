from sqlalchemy.orm import sessionmaker
from db_conn import conn

Session = sessionmaker(bind=conn.engine)
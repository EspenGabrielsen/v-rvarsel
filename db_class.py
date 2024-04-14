from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float,func, DateTime


Base = declarative_base()

class Forcast(Base):
    __tablename__ = "forcast"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lat = Column(Float)
    long = Column(Float)
    weather = Column(String)
    precipitation = Column(Float)
    air_temperature = Column(Float)
    wind_from_direction = Column(Float)
    wind_speed = Column(Float)
    time = Column(DateTime(timezone=False), server_default=func.now())

class Create_tab():
        from db_conn import conn
        Forcast.__table__
        Base.metadata.create_all(conn.engine)
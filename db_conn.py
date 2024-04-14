from sqlalchemy import create_engine

class DbConnection:
    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///sample.db", echo=False)

conn = DbConnection()

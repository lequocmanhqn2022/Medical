from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:123456@127.0.0.1/medical_management')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

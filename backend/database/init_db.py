from db_connection import engine
from models import Base

def create_database():
    Base.metadata.create_all(bind=engine)
    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_database()

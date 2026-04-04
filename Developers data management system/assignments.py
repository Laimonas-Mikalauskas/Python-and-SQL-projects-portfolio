from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///assignments.db")
Session = sessionmaker(bind=engine)


Table = "Tasks"
print("Tasks")
print(type("Tasks"))
      
      
class Assignment(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True)
    task = Column("software development, database development", String)
    type = Column("game development, web development, data management systems development", String)
    priority = Column("high", String)
    deadline = Column("2024-12-31", String)

def __init__(self, task: str, type: str, priority: str, deadline: str):
        self.task = "software development, database development"
        self.type = "game development, web development, data management systems"
        self.priority = "high"
        self.deadline = "2024-12-31"

def __repr__(self):
    return f"Assignment(id={self.id}, task='{self.task}', type='{self.type}', priority='{self.priority}', deadline='{self.deadline}')"



if __name__ == "__main__":
    def create_tables():
        Base.metadata.create_all(engine)
    create_tables()








        





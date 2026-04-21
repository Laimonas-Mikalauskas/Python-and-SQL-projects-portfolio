from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import re

Base = declarative_base()
engine = create_engine('sqlite:///assignments.db')
Session = sessionmaker(bind=engine)
session = Session()

Table_name = "Assignments"
print("Assignments")
print(type("Assignments"))

class Assignment(Base):
    __tablename__ = Table_name
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    def __init__(self, title, description):
        self.set_title(title)
        self.set_description(description)

    def set_title(self, title):
        if not title or len(title) < 5:
            raise ValueError("Title must be at least 5 characters.")
        self.title = title

    def set_description(self, description):
        if not description or len(description) < 10:
            raise ValueError("Description must be at least 10 characters.")
        self.description = description

Base.metadata.create_all(engine)

# Create a new assignment
try:
    new_assignment = Assignment(title="Project 1", description="Complete the first project.")
    session.add(new_assignment)
    session.commit()
    print(f"Assignment created: {new_assignment.title}")
except ValueError as e:
    print("Error:", e)
finally:
    session.close()

try:
    new_assignment = Assignment(title="Project 2", description="Short desc.")
    session.add(new_assignment)
    session.commit()
    print(f"Assignment created: {new_assignment.title}")
except ValueError as e:
    print("Error:", e)
finally:    
    session.close()   

try:
    new_assignment = Assignment(title="Project 3", description="Complete the project.")
    session.add(new_assignment)
    session.commit()
    print(f"Assignment created: {new_assignment.title}")
except ValueError as e:
    print("Error:", e)
finally:    
    session.close()

try:
    session = Session()
    assignment = session.query(Assignment).filter(Assignment.title.in_(["Project 1", "Project 2", "Project 3"])).first()
    if assignment:
        print(f"Assignment found: {assignment.title} - {assignment.description}")
    else:
        print("Assignment not found.")
except Exception as e:
    print("Error:", e)
finally:
    session.close()

Session = sessionmaker(bind=engine)
session = Session()    

Base = declarative_base()
session = commit = sessionmaker(bind=engine)()
session = Session()






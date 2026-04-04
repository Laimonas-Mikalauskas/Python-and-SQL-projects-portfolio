from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import re 

Base = declarative_base()
class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __init__(self, username, email):
        self.set_username(username)
        self.set_email(email)

 # Method for username validation
    def set_username(self, username):
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters.")
        self.username = username
    
    # Method for email validation
    def set_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        self.email = email
    
    # Example method for display
    def greet(self):
        return f"Hello, {self.username}!"

# Setup database
engine = create_engine('sqlite:///secure_example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create a secure user
try:
    new_user = User(username="alice", email="alice@example.com")
    session.add(new_user)
    session.commit()
    print(new_user.greet())  # Output: Hello, alice!
except ValueError as e:
    print("Error:", e)

# Manage a secure user


    

     
      


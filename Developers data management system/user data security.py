from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import re 

Base = declarative_base()
engine = create_engine('sqlite:///secure_example.db')
Session = sessionmaker(bind=engine)
session = Session()

Table = "Users"
print("Users")
print(type("Users"))

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

# Secure database session management

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
Session = sessionmaker(bind=engine)
session = Session()

# Manage a secure user
try:
    user = session.query(User).filter_by(username="alice").first()
    if user:
        user.set_email("alice@newexample.com")
        session.commit()
        print(f"Updated email: {user.email}")  # Output: Updated email:
    else:        
        print("User not found.")
except ValueError as e:
    print("Error:", e)
                       
# Attempt to create a user with invalid email
try:
    invalid_user = User(username="bob", email="invalid-email")
    session.add(invalid_user)
    session.commit()
except ValueError as e:
    print("Error:", e)  # Output: Error: Invalid email format.

# Attempt to create a user with short username
try:
    invalid_user = User(username="ab", email="ab@example.com")
    session.add(invalid_user)
    session.commit()
except ValueError as e:
    print("Error:", e)  # Output: Error: Username must be at least 3 characters.

# Create user with valid data
try:
    valid_user = User(username="charlie", email="charlie@example.com")
    session.add(valid_user)
    session.commit()
    print(valid_user.greet())
except ValueError as e:
    print("Error:", e)

# Update user with valid data
try:
    user = session.query(User).filter_by(username="charlie").first()
    if user:
        user.set_email("charlie@newexample.com")
        session.commit()
        print(f"Updated email: {user.email}")
except ValueError as e:
    print("Error:", e)

# Secure user data management with error handling
try:
    user = session.query(User).filter_by(username="charlie").first()
    if user:
        user.set_email("invalid-email")
        session.commit()
except ValueError as e:
    print("Error:", e)  # Output: Error: Invalid email format.    

# Clean up
session.query(User).delete()
session.commit()
session.close()

# In summary, this code demonstrates how to implement basic validation and error handling for user data in a SQLAlchemy application, while also highlighting the importance of security best practices when managing user information in a database.

                                                       


    

     
      


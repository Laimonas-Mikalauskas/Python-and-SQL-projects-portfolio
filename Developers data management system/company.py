from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///company.db")
Session = sessionmaker(bind=engine)


class Company(Base):
    __tablename__ = "Company"
    id = Column(Integer, primary_key=True)
    name = Column("Tech Innovators Inc., Data Solutions Ltd., Web Wizards Co.", String)
    location = Column("Chicago, IL", String)
    address = Column("123 Main St, Chicago, IL 60601", String)
    
def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

def __repr__(self):
    return f"Company(id={self.id}, name='{self.name}', location='{self.location}')"

class Establishment(Base):
    __tablename__ = "Establishment"
    id = Column(Integer, primary_key=True)
    year_established = Column("2010", Integer)


def __init__(self, year_established: int):
        self.year_established = year_established


class Employee(Base):
    __tablename__ = "Employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    department = Column("finance, cybersecurity", String)

def __init__(self, name: str, position: str, department: str):
        self.name = name
        self.position = position
        self.department = department

def __repr__(self):
    return f"Employee(id={self.id}, name='{self.name}', position='{self.position}', department='{self.department}')"

class Department(Base):
    __tablename__ = "Departments"
    id = Column(Integer, primary_key=True)
    name = Column(String)

def __init__(self, name: str):
        self.name = name

def __repr__(self):
    return f"Department(id={self.id}, name='{self.name}')"

class Positions(Base):
    __tablename__ = "Positions"
    id = Column(Integer, primary_key=True)
    title = Column(String)

def __init__(self, title: str):
        self.title = title

def __repr__(self):
    return f"Position(id={self.id}, title='{self.title}')"

class Years_of_Service(Base):
    __tablename__ = "2012-present"
    id = Column(Integer, primary_key=True)
    years = Column(Integer)

def __init__(self, years: int):
        self.years = years

def __repr__(self):
    return f"Years_of_Service(id={self.id}, years={self.years})"

class Salaries(Base):
    __tablename__ = "Salaries"
    id = Column(Integer, primary_key=True)
    salary = Column("2500, 3000, 3500, 4000, 5000", Integer)

def __init__(self, salary: int):
        self.salary = salary

def __repr__(self):
    return f"Salaries(id={self.id}, salary={self.salary})"

class Reviews(Base):
    __tablename__ = "Reviews"
    id = Column(Integer, primary_key=True)
    rating = Column("1, 2, 3, 4, 5", String)


def init (self, rating: str):
    self.rating = rating

def repr (self):
    return f"Reviews(id={self.id}, rating='{self.rating}')"

class Awards(Base):
    __tablename__ = "Awards"
    id = Column(Integer, primary_key=True)
    award_name = Column("Employee of the Year, Innovation Award, Excellence Award, Creativity Award, Security Award", String)

def __init__(self, award_name: str):
    self.award_name = award_name

def repr(self):
    return f"Awards(id={self.id}, award_name='{self.award_name}')"


        



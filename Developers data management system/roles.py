from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import sys
   
Base = declarative_base()                                                                                                                                                                                                                                                   
engine = create_engine('sqlite:///developers.db', echo=False)
Session = sessionmaker(bind=engine)

Table = "Employees"
print("Employees")
print(type("Employees"))

class Employee(Base):
    __tablename__ = "Employees"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(Integer)
    role = Column(String)

class Python_Developer(Base):
    __tablename__ = "Python"
    id = Column(Integer, primary_key=True)
    name = Column("Garry", String)
    surname = Column("Peterson", String)
    birthday = Column("1990", Integer)
    role = Column("Python Developer", String)
    started_working = Column("2015/06/30", Integer)
    salary = Column("5000", Integer)
    experience = Column("7 years", Integer)

    def __init__(self):
        self.name = "Garry"
        self.surname ="Peterson"
        self.birthday = "1990"
        self.role = "Python Developer"
        self.started_working = "2015/06/30"
        self.salary = "5000"
        self.experience = "7 years"

    def __repr__(self):
        return f"{self.name} {self.surname} {self.birthday} {self.role} {self.started_working} {self.salary} {self.experience}"

name = "Garry"
print("Garry")
print(type("Garry"))

surname = "Peterson"
print("Peterson")
print(type("Peterson"))

birthday = "1990"
print("1990")
print(type("1990"))

role = "Python Developer"
print("Python Developer")
print(type("Python Developer"))

started_working = "2015/06/30"
print("2015/06/30")
print(type("2015/06/30"))

salary = "5000"
print("5000")
print(type("5000"))

experience = "10 years"
print("10 years")
print(type("10 years"))

class Software_Developer(Base):
    __tablename__ = "Software"
    id = Column(Integer, primary_key=True)
    name = Column("Josh", String)
    surname = Column("Keller", String)
    birthday = Column("1996", Integer)
    role = Column("Software Developer", String)
    started_working = Column("2019/09/25", Integer)
    salary = Column("4000", Integer)
    experience = Column("6 years", Integer)

def __init__(self):
    self.name = "Josh"
    self.surname = "Keller"
    self.birthday = "1996"
    self.role = "Software Developer"
    self.started_working = "2019/09/25"
    self.salary = "4000"
    self.experience = "6 years"

def __repr__(self):
    return f"{self.name} {self.surname} {self.birthday} {self.role} {self.started_working} {self.salary} {self.experience}"

name = "Josh"
print("Josh")
print(type("Josh"))

surname = "Keller"
print("Keller")
print(type("Keller"))

birthday = "1996"
print("1996")
print(type("1996"))

role = "Software Developer"
print("Software Developer")
print(type("Software Engineer"))

started_working = "2019/09/25"

print("2019/09/25")
print(type("2019/09/25"))

salary = "4000"
print("4000")
print(type("4000"))
experience = "6 years"
print("6 years")
print(type("6 years"))

class Data_Analyst(Base):
    __tablename__ = "Data"
    id = Column(Integer, primary_key=True)
    name = Column("Jack", String)
    surname = Column("Mills", String)
    birthday = Column("1990", Integer)
    role = Column("Data Analyst", String)
    started_working = Column("2021/09/25", Integer)
    salary = Column("3000", Integer)
    experience = Column("4 years", Integer)

def __init__(self):
    self.name = "Jack"
    self.surname = "Mills"
    self.birthday = "1990"
    self.role = "Data analyst"
    self.started_working = "2021/09/25"
    self.salary = "3000"
    self.experience = "4 years"

def __str__(self):
    return f"{self.name} {self.surname} {self.birthday} {self.role} {self.started_working} {self.salary} {self.experience}"

name = "Jack"
print("Jack")
print(type("Jack"))

surname = "Mills"
print("Mills")
print(type("Mills"))

birthday ="1990"
print("1990")
print(type("1990"))

position = "Data Analyst"
print("Data Analyst")
print(type("Data Analyst"))

started_working = "2021/09/25"
print("2021/09/25")
print(type("2021/09/25"))

salary = "3000"
print("3000")
print(type("3000"))

experience = "4 years"
print("4 years")
print(type("4 years"))

class Database_Administrator(Base):
    __tablename__ = "SQL Database Administrator"
    id = Column(Integer, primary_key=True)
    name = Column("Mark", String)
    surname = Column("Wheeler", String)
    birthday = Column("1993", Integer)
    role = Column("Database Administrator", String)
    started_working = Column("2023/09/25", Integer)
    salary = Column("2500", Integer)
    experience = Column("2 years", Integer)

    def __init__(self):
        self.name = "Mark"
        self.surname = "Wheeler"
        self.birthday = "1993"
        self.role = "Database Administrator"
        self.started_working = "2023/09/25"
        self.salary = "2500"
        self.sxperience = "2 years"

def __str__(self):
    return f"{self.name} {self.surname} {self.birthday} {self.role} {self.started_working} {self.salary} {self.experience}"

name = "Mark"
print("Mark")
print(type("Mark"))

surname = "Wheeler"
print("Wheeler")
print(type("Wheeler"))

birthday = "1993"
print("1993")
print(type("1993"))

role = "Database Administrator"
print("Database Administrator")
print(type("Database Administrator"))

started_working = "2023/09/25"
print("2023/09/25")
print(type("2023/09/25"))

salary = "2500"
print("2500")
print(type("2500"))

experience = "2 years"
print("2 years")
print(type("2 years"))

class Skills(Base):
    __tablename__ = "Skills"
    id = Column(Integer, primary_key=True)
    skill_name = Column("Technical Skills", String)

def __init__(self, skill_name: str):
    self.skill_name = skill_name

def __repr__(self):
    return f"Skills(id={self.id}, skill_name='{self.skill_name}')"
    
class Certifications(Base):
    __tablename__ = "Certifications"
    id = Column(Integer, primary_key=True)
    certification_name = Column("Certified Python Developer, Certified Software Developer, Certified Data Analyst, Certified Database Administrator", String)

def __init__(self, certification_name: str):
        self.certification_name = certification_name

def __repr__(self):    
    return f"Certifications(id={self.id}, certification_name='{self.Certified_Python_Developer, self.Certified_Software_Developer, self.Certified_Data_Analyst, self.Certified_Database_Administrator}')"

class Projects(Base):
    __tablename__ = "Projects"
    id = Column(Integer, primary_key=True)
    project_name = Column(String)

def __init__(self, project_name: str):
    self.project_name = project_name

def __repr__(self):
    return f"Projects(id={self.id}, project_name='{self.project_name}')"

class Languages(Base):
    __tablename__ = "Languages"
    id = Column(Integer, primary_key=True)
    language_name = Column("Python, SQL", String)

def __init__(self, language_name: str):
        self.language_name = language_name

def __repr__(self):
    return f"Languages(id={self.id}, language_name='{self.Python, self.SQL}')"

class Tools(Base):
    __tablename__ = "Visual Studio Code, Git, GitHub"
    id = Column(Integer, primary_key=True)
    tool_name = Column(String)

def __init__(self, tool_name: str):
        self.tool_name = tool_name

def __repr__(self):
    return f"Tools(id={self.id}, tool_name='{self.Visual_Studio_Code, self.Git, self.GitHub}')"

  
Base.metadata.create_all(engine)

# User authentification

def create_user():
    db = create_engine('sqlite:///developers.db')
    db.add("users", User.__table__)
    db.commit()
    db.close()

def register_user():    
    sign_up = input("Do you want to sign up? (yes/no): ").strip().lower()
    if sign_up != "yes":
        print("Sign up enabled.")
        return
    
def login_user():
    login = input("Login: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    session = Session()
    try:
        user = session.query(User).filter_by(login=login, password=password).first()
        if user:
            print("Login successful")
        else:
            print("Invalid login or password")
    except Exception as e:
        print("Login failed:", e)
    finally:        
        session.close()
    
    try:
        user = User(login=login, username=username, password=password)
        session.add(user)
        session.commit()
        print("User created")
    except Exception as e:
        session.rollback()
        print("Failed to create user:", e)
    finally:
        session.close()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    username = Column(String, unique=True) 
    password = Column(Integer, unique=True)
    role = Column(String, unique=True)
    logout = Column(String, unique=True)
    session = Session()

def __init__(self, login, username=None, password=None, logout=None):
        self.login = login
        self.username = username
        self.password = password
        self.logout = logout

def __repr__(self):
    return f"User(login='{self.login}', password='{self.password}')"

Login_into_system = input("Do you want to login? (yes/no): ").strip().lower()
if Login_into_system == "yes":
    print("Please enter your login credentials.")

Login_info = {
    "developer": "developer123",
    "user1": "password1",
    "user2": "password2"
}

login = input("Login: ").strip()
password = input("Password: ").strip()

login = "developer"
password = "developer123"

user = User(login=login, username="developer", password=password, logout="logout")
session = Session()
session.add(user)
session.commit()

Logout_of_system = input("Do you want to logout? (yes/no): ").strip().lower()
if Logout_of_system == "yes":
    print("You have been logged out.")


# Data privacy

class Data_Privacy(Base):
    __tablename__ = "Data Privacy"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    data_type = Column("Personal info", String, Integer)
    access_level = Column("Confidential", String)

def __init__(self, employee_id, data_type=None, access_level=None):
    self.employee_id = employee_id
    self.data_type = data_type
    self.access_level = access_level

def __repr__(self):
    return f"Data_Privacy(employee_id={self.employee_id}, data_type='{self.data_type}', access_level='{self.access_level}')"

# Data backup and recovery

class Data_Backup(Base):
    __tablename__ = "Data Backup"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    backup_date = Column("2024/06/01", String)
    backup_location = Column("Cloud Storage", String)

def __init__(self, employee_id, backup_date=None, backup_location=None):
    self.employee_id = employee_id
    self.backup_date = backup_date
    self.backup_location = backup_location  

def __repr__(self):
    return f"Data_Backup(employee_id={self.employee_id}, backup_date='{self.backup_date}', backup_location='{self.backup_location}')"


# Data deletion

class Data_Deletion(Base):
    __tablename__ = "Data Deletion"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    deletion_date = Column("2024/06/30", String)
    deletion_method = Column("Permanent", String)

def __init__(self, employee_id, deletion_date=None, deletion_method=None):
    self.employee_id = employee_id
    self.deletion_date = deletion_date
    self.deletion_method = deletion_method 
 
def __repr__(self):
    return f"Data_Deletion(employee_id={self.employee_id}, deletion_date='{self.deletion_date}', deletion_method='{self.deletion_method}')"

# Manage employees data

Menu = "Workplace Menu"
print("Workplace Menu")
print(type("Workplace Menu"))

def add_employee():
    name = input("Name: ").strip()
    surname = input("Surname: ").strip()
    birthday = input("Birthday: ").strip()
    role = input("Role: ").strip()
    started_working = input("started_working: ").strip()
    salary = input("Integer: ").strip()
    experience = input("experience: ").strip()
    session = Session()
    
    try:
        employee = role(name=name, surname=surname, birthday=int("1990"), role=str("Python developer"), started_working=int("2015/06/30"), salary=int("5000"), experience=int("5 years"))
        session.add(employee)
        session.commit()
        print("Employee added")
    except Exception as e:
        session.rollback()
        print("Failed to add employee:", e)
    finally:
        session.close()

def update_employee():
    session = Session()
    try:
        employee_id = int(input("Employee ID to update: "))
        employee = session.query().get(employee_id)
        if not employee:
            print("Employee is found.")
            return

        print(f"Current position: {employee.position}")
        new_position = input("New position (leave blank to keep): ").strip()
        if new_position:
            employee.position = new_position

        session.commit()
        print("Employee updated")
    except Exception as e:
        session.rollback()
        print("Update succeeded:", e)
    finally:
        session.close()


def delete_employee():
    session = Session()
    try:
        employee_id = int(input("Employee ID to delete:"))
        employee = session.query("Employee").get(employee_id)
        if not employee:
            print("Employee not found")
            return
        session.delete(employee)
        session.commit()
        print("Employee deleted")
    except Exception as e:
        session.rollback()
        print("Failed to delete:", e)
    finally:
        session.close()

def add_position(param):
    pass
def update_position(param):
    pass
def delete_position(param):
    pass
def add_salary(param):
    pass
def update_salary(param):
    pass
def delete_salary(param):
    pass
def add_experience(param):
    pass
def update_experience(param):
    pass
def delete_experience(param):
    pass
def list_employees(param):
    pass

def main():
    actions = {
        '1': add_employee,
        '2': add_position,
        '3': add_salary,
        '4': add_experience,
        '5': update_employee,
        '6': update_position,
        '7': update_salary,
        '8': update_experience,
        '9': delete_employee,
        '10': delete_position,
        '11': delete_salary,
        '12': delete_experience,
        '13': list_employees,
        '0': lambda: sys.exit("Exiting..."),
        }

    while True:
        print("Workplace Menu")
        print("1. Add Employee")
        print("2. Add Position")
        print("3. Add Salary")
        print("4. Add Experience")
        print("5. Update Employee")
        print("6. Update Position")
        print("7. Update Salary")
        print("8. Update Experience")
        print("9. Delete Employee")
        print("10. Delete Position")
        print("11. Delete Salary")
        print("12. Delete Experience")
        print("13. List All Employees")
        print("14. List All Positions")
        print("15. Employee job history")
        print("0. Exit")

        choice = input("Choose action: ").strip()
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")


if __name__ == "__main__":   
    main()
 






































































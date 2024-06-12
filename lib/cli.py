import getpass
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

class DiaryEntry(Base):
    __tablename__ = 'diary_entries'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    date = Column(Date, default=datetime.date.today)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref="diary_entries")

engine = create_engine('sqlite:///diary.db')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def create_user():
    username = input("Enter a username: ")
    if check_username_exists(username):
        print("Username already exists. Please choose a different one.")
        return
    password = getpass.getpass("Enter a password: ")
    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    print("User created successfully!")

def check_username_exists(username):
    user = session.query(User).filter_by(username=username).first()
    return user is not None

def login_user():
    username = input("Enter your username: ")
    if not check_username_exists(username):
        print("User does not exist. Please create an account first.")
        return None
    password = getpass.getpass("Enter your password: ")
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        print("Login successful!")
        return user
    else:
        print("Invalid password.")
        return None

def create_diary_entry(user):
    title = input("Enter a title for your diary entry: ")
    content = input("Enter the content of your diary entry: ")
    diary_entry = DiaryEntry(title=title, content=content, user=user, date=datetime.date.today())
    session.add(diary_entry)
    session.commit()
    print("Diary entry created successfully!")

def view_diary_entries(user):
    diary_entries = session.query(DiaryEntry).filter_by(user=user).all()
    for diary_entry in diary_entries:
        print(f"{diary_entry.date}: {diary_entry.title} - {diary_entry.content}")
        
def find_diary_entry_by_title(user):
    title = input("Enter the title of the diary entry you're looking for: ")
    diary_entry = session.query(DiaryEntry).filter_by(user=user, title=title).first()
    if diary_entry:
        print(f"Title: {diary_entry.title}, Content: {diary_entry.content}")
    else:
        print("Diary entry not found.")

def delete_diary_entry(user):
    title = input("Enter the title of the diary entry you want to delete: ")
    diary_entry = session.query(DiaryEntry).filter_by(user=user, title=title).first()
    if diary_entry:
        session.delete(diary_entry)
        session.commit()
        print("Diary entry deleted successfully!")
    else:
        print("Diary entry not found.")

def greet_user(user):
    current_time = datetime.datetime.now().time()
    if current_time.hour < 12:
        greeting = "Good morning"
    elif current_time.hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    print(f"{greeting}, {user.username}!")

def main():
    while True:
        print("Welcome to your personal diary!")
        print("1. Create an account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_user()
        elif choice == "2":
            user = login_user()
            if user:
                greet_user(user)
                while True:
                    print("1. Create a diary entry")
                    print("2. View all diary entries")
                    print("3. Find a diary entry by title")
                    print("4. Delete a diary entry")
                    print("5. Logout")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        create_diary_entry(user)
                    elif choice == "2":
                        view_diary_entries(user)
                    elif choice == "3":
                        find_diary_entry_by_title(user)
                    elif choice == "4":
                        delete_diary_entry(user)
                    elif choice == "5":
                        break
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
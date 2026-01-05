from db import SessionLocal, engine
from models import Base, User, AccessLevel
from getpass import getpass

#Create tables in the database if they don't exist, or if the wensites has not been ran yet
Base.metadata.create_all(bind=engine)


def create_admin():
    session = SessionLocal()
    admin_email = input("Enter admin email ").strip()
    existing_admin = session.query(User).filter_by(email=admin_email).first()
    if existing_admin:
        print(f"Admin {admin_email} already exist.")
        session.close()
        return
    
    while True:
        password = getpass("Enter admin password: ")
        confirm = getpass("Confirm admin password:")
        if password != confirm:
            print("Password do not match. Try again.")
        elif len(password) < 8 and len(password) > 12:
            print("Password must be between 8 to 12 characters.")
        else:
            break

        admin_user = User(
            email=admin_email,
            access_level=AccessLevel.ADMIN
        )
        admin_user.set_password(password)

        session.add(admin_user)
        session.commit()
        session.close()
        print(f"Admin user {admin_email} created sucessfully!")
if __name__ == "__main__":
    create_admin()
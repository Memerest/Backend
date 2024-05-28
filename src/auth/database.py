from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5433/auth"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class UserInDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    access_token = Column(String, nullable=True)
    refresh_token = Column(String, nullable=True)


Base.metadata.create_all(bind=engine)


def get_user_by_username(db_session, username):
    return db_session.query(UserInDB).filter(UserInDB.username == username).first()


def add_user(db_session, username, email, full_name, hashed_password, access_token, refresh_token):
    new_user = UserInDB(
        username=username,
        email=email,
        full_name=full_name,
        hashed_password=hashed_password,
        access_token=access_token,
        refresh_token=refresh_token
    )
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    return new_user
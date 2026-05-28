from sqlalchemy import Column, Integer, String, DateTime, Date, Numeric, Enum, ForeignKey
from app.database import Base
from datetime import datetime




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    id_user = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    type = Column(Enum("income", "expense" , name="transaction_type"), nullable=False)
    value = Column(Numeric, nullable=False)
    data = Column(Date, default=datetime.now)
    id_user = Column(Integer, ForeignKey("users.id"))
    id_category = Column(Integer, ForeignKey("categories.id"))
    created_at = Column(DateTime, default=datetime.now)

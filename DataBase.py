from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///bot.db', echo=False)
Base = declarative_base(bind=engine)


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    text = Column(String(length=2048))

    def __init__(self, text, message_id, chat_id, user_id):
        self.chat_id = chat_id
        self.message_id = message_id
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f'<Message chat_id={self.chat_id}, message_id={self.message_id}>'


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    step = Column(Integer, default=0)

    def __init__(self, user_id):
        self.step = 0
        self.user_id = user_id


Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)






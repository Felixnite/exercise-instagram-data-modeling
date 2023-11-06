import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class User(Base): 
    __tablename__ = 'user'
    id = Column(Integer, primary_key =True)
    username = Column(String(25), nullable=False, unique=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(30), nullable=False)
    followers = relationship("Followers", uselist=True, backref='user')
    comments = relationship("Comments", uselist=True, backref='user')
    post = relationship("Post", uselist=True, backref='user')

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False)
    url = Column(String(70))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    comments = relationship("Comments", uselist=True, backref='post')
    media = relationship("media", uselist=True, backref='post')


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

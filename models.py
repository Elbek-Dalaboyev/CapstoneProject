import os
from sqlalchemy import Column, String, Boolean, Integer, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy

database_filename = "database/database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_create_all():
    db.create_all()

class Actors(db.Model):
    __tablename__ = 'Actors'
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    name = Column(String, nullable=False)
    age = Column(String, nullable=False)
    role = Column(String, nullable=False)
    gender = Column(String)

    def __init__(self, id, name, age, role, gender):
        self.id = id
        self.name = name
        self.age = age
        self.role = role
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'role': self.role,
            'gender': self.gender
        }

class Movies(db.Model):
    __tablename__ = 'Movies'
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    release_date = Column(String)

    def __init__(self, title, genre, release_date):
        self.title = title
        self.genre = genre
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'release_date': self.release_date
        }


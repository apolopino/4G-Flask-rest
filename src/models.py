from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class People(db.Model):
	__tablename__ = 'people'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), unique=True, nullable=False)
	planet = db.relationship('Planets')
	planet_name = db.Column(db.String(250), db.ForeignKey('planets.name'))


	def serialize(self):
		return {
			"id": self.id,
			"name": self.name,
			"planet": self.planet_name
		}

class Planets(db.Model):
	__tablename__ = 'planets'
	id = db.Column(db.Integer, primary_key=True)
	name= db.Column(db.String(120), unique=True, nullable=False)
	people = db.relationship('People')
	# inhabitants = db.Column(db.String(250), db.ForeignKey('people.name'))

	def __repr__(self):
		return self.name

	def serialize(self):
		return {
			"id": self.id,
			"name": self.name,
			"people": self.people
		}

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(80), unique=False, nullable=False)
	is_active = db.Column(db.Boolean(), unique=False, nullable=False)

	def __repr__(self):
		return '<User %r>' % self.username

	def serialize(self):
		return {
				"id": self.id,
				"email": self.email,
				# do not serialize the password, its a security breach
		}
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class People(db.Model):
	__tablename__ = 'people'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), unique=True, nullable=False)
	planets = db.relationship('Planets', lazy=True)

	def serialize(self):
		return {
			"id": self.id,
			"name": self.name,
			"planets_list": self.planets
		}

class Planets(db.Model):
	__tablename__ = 'planets'
	id = db.Column(db.Integer, primary_key=True)
	name= db.Column(db.String(120), unique=True, nullable=False)
	people_id = db.Column(db.Integer, db.ForeignKey('people.id'))

	def __repr__(self):
		return self.name

	def serialize(self):
		return {
			"id": self.id,
			"name": self.name,
			"people_id": self.people_id
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
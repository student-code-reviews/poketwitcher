"""Models and database functions for PokeTwitcher project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

""" TODO:
* test all of this
* verify syntax of Boolean args
* make decision regarding 'type' column in database and possible addtl relational table for it
* make decision regarding 'gender' and possible addtl relational table for it
* make decision for location column and datatype
"""

# def login(self.password):
#     check_password_hash(password, self.password)

# def create_password(self, password):
#     self.password = generate_password_hash(password)

class User(db.Model):
    """User of PokeTwitcher website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User id={self.user_id} email={self.email}>"


# class Pokemon(db.Model):
#     """A Pokemon available in the app Pokemon Go."""

#     __tablename__ = "pokemon"

#     pokemon_id = db.Column(db.Integer, autoincrement=False, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     #############################################################
#     # shiny = db.Column(db.Boolean(), nullable=False)
#     # gender = db.Column(db.String(1))
#     # https://docs.sqlalchemy.org/en/13/core/type_basics.html#sqlalchemy.types.ARRAY
#     # poke_type = db.Column(db.ARRAY(String))
#     # alolan = db.Column(db.Boolean())
#     # isDitto = db.Column(db.Boolean())
#     # img store as url
#     # img = db.Column(db.String)

#     def __repr__(self):
#         """Provide helpful representation when printed."""

#         return f"<Pokemon id={self.pokemon_id} name={self.name}>"


# class Sighting(db.Model):
#     """Sighting of an individual Pokemon, belongs to a User."""

#     __tablename__ = "sightings"

#     sighting_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.pokemon_id'))
#     # How do I timestamp a sighting? ###
#     timestamp = db.Column(db.DateTime())
#     ############################################################
#     # How do I convert lat and long into a string for this? ###
#     # location = db.Column(db.String(200))

#     # Define relationships to user and pokemon
#     user = db.relationship("User", db.backref("users", order_by=sighting_id))
#     pokemon = db.relationship("Pokemon", db.backref("pokemon", order_by=sighting_id))

#     def __repr__(self):
#         """Provide helpful representation when printed."""

#         return f"<Sighting sighting_id={self.sighting_id} user_id={self.user_id} pokemon_id={self.pokemon_id}>"


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///poketwitcher'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
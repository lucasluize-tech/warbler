"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase

from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data
db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""


    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
        
        self.client = app.test_client()
        

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

    # Does the repr method work as expected?
    def test_user_repr(self):
        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )
        
        u2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD2"
        )
        db.session.add(u)
        db.session.add(u2)
        
        db.session.commit()

        self.assertEqual(u2, User.query.filter_by(username=u2.username).one())
        self.assertEqual(u, User.query.filter_by(username=u.username).one())


    
    # Does is_following successfully detect when user1 is following user2?
    def test_user_is_following(self):
        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )
        
        u2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD2"
        )
        followed_user = u2
        u.following.append(followed_user)
        db.session.commit()

        self.assertTrue(u.is_following(u2))

    # Does is_following successfully detect when user1 is not following user2?
        u.following.pop()
        db.session.commit()
        self.assertFalse(u.is_following(u2))
    
    # Does is_followed_by successfully detect when user1 is followed by user2?
    def test_user_is_followed_by(self):
        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )
        
        u2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD2"
        )
        user_following = u2
        u.followers.append(u2)
        db.session.commit()

        self.assertTrue(u.is_followed_by(u2))
    
    # There's no User.create method to test.

    # Does User.authenticate successfully return a user when given a valid username and password?
    def test_user_authenticate(self):
        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )
        db.session.add(u)
        db.session.commit()

        self.assertEqual(User.authenticate(u.username, u.password), u)
            # Does User.authenticate fail to return a user when the username is invalid?
        self.assertFalse(User.authenticate('anyname', u.password))
        #     # Does User.authenticate fail to return a user when the password is invalid?
        self.assertFalse(User.authenticate(u.username, 'pass'))

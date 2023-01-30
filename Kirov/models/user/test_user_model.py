import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from env import TESTING_settings
from models import Base, User
from utils import Settings

settings = TESTING_settings


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine(Settings(settings).db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind = self.engine)

    def test_create_user(self):
        print('START create user')
        session = self.Session()
        user = User(username = 'testuser', email = 'testuser@example.com')
        session.add(user)
        session.commit()
        print('END create user')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')

    def tearDown(self):
        print('START tearDown')
        # Base.metadata.drop_all(self.engine)
        self.engine.dispose()
        print('END tearDown')
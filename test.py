#need help making tests
from app import app
from unittest import TestCase
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True

db.drop_all()
db.create_all()

class FlaskTests(TestCase):

  def setUp(self):

      self.client = app.test_client()
      User.query.delete()
      user = User(
          first_name="Tester",
          last_name="Testing",
          image_url="none")
      db.session.add(user)
      db.session.commit()

      self.user_id = user.id
  
  def tearDown(self):
    db.session.rollback()
  
  def test_homepage(self):

    self.client.get('/users')
    response = self.client.get('/')
    self.assertEqual(response.status_code, 302)
  
  def test_new_user(self):

    self.client.post('/user/new')
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

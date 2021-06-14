import unittest
from app.models import User, Comment

class UserPasswordTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'chicken')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('chicken'))

class CommentTest(unittest.TestCase):
  def setUp(self):
      self.user_layersony = User(id= 12345, username = 'layersony',password = 'chicken', email = 'layersony@gmail.com')
      self.new_comment = Comment(id=12345, comment='This movie is the best thing since sliced bread', user_id=12345, pitch_id=12345) 

  def test_check_instance_variables(self):
      self.assertEquals(self.new_comment.id,12345)
      self.assertEquals(self.new_comment.comment,'This movie is the best thing since sliced bread')
      self.assertEquals(self.new_comment.user_id,12345)
      self.assertEquals(self.new_comment.pitch_id,12345)

  def test_save_comment(self): 
      self.new_comment.save_comment()
      self.assertTrue(len(Comment.query.all())>0)

  def test_get_comment_by_id(self):

      self.new_comment.save_comment()
      got_comments = Comment.get_comments(12345)
      self.assertTrue(len(got_comments) == 1)
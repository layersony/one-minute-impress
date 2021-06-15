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


class CommentModelTest(unittest.TestCase):

    def setUp(self):

        self.comment= Comment(comment = 'testing testing')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.comment.comment ,'testing testing')
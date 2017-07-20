import unittest
from bucket import Bucket


class BucketTestCase(unittest.TestCase):
    
    #ClassIsSetup = False
    email = 'user@example.com'
    username = 'kev'
    password = 'czar'
    goal = 'make a difference'
    
    @classmethod
    def setUpClass(self):
        unittest.TestCase.setUp(self)
        self.Bucket = Bucket(username, password, goal)
    
    """    
    def setUpClass(self):
        unittest.TestCase.setUp(self)
        Bucket(username, password, goal)
        username = 'kev'
        password = 'czar'
        goal = 'make a difference'
    """
        

    def test_add_user(self):
        self.assertTrue(Bucket.add_user, 1)
        
    def test_invalid_user(self):
        self.assertTrue(Bucket.invalid_user, 1)
        
    def test_login(self):
        self.assertTrue(Bucket.login(username))

    def test_display_goal(self):
        self.assertEqual(self.user[username][1], goal)
                
if __name__ == '__main__':
    unittest.main(exit=False)

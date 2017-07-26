from bucketlist import BucketList
import uuid

class User(object):

    data = []

    def __init__(self, email, password):

        self.email = email
        self.password = password
        self.id = id


    # Create
    @staticmethod
    def create_bucketlist(description, goal, id=str(uuid.uuid1())):
        User.data.append(BucketList(id, description, goal)) 

    # Read
    @staticmethod
    def display_bucketlist():
        return User.data

    # Update
    @staticmethod
    def update_bucketlist(goal):
        User.data.insert(0, BucketList(id, description, goal))

    # Delete
    @staticmethod
    def rem_bucketlist(id):
        User.data.pop(id)

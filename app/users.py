from bucketlist import BucketList

class User(object):

    data = []

    def __init__(self, email, password):

        self.email = email
        self.password = password
        self.id = id


    # Create
    @staticmethod
    def create_bucketlist(id, description, goal):
        User.data.append(BucketList(id, description, goal)) 

    # Read
    @staticmethod
    def display_bucketlist():
        return User.data

    # Update
    @staticmethod
    def update_bucketlist():
        User.data.insert(0, BucketList(id, description, goal))

    # Delete
    @staticmethod
    def rem_bucketlist(goal_id):
        User.data.pop(goal_id)

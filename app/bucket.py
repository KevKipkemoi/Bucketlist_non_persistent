from bucketlist import BucketList

class Bucket(object):

    data = []

    # Create
    @staticmethod
    def create_bucketlist(description, goal, id=str(len(data))):
        new_bucket = BucketList(id, description, bucketlist)
        Bucket.data.append(new_bucket) 

    # Read
    @staticmethod
    def display_bucketlist():
        return Bucket.data

    # Update
    @staticmethod
    def update_bucketlist(bucketlist):
        updated_bucket = BucketList(id, description, bucketlist)
        Bucket.data.insert(0, updated_bucket)

    # Delete
    @staticmethod
    def rem_bucketlist(id):
        Bucket.data.pop(id)

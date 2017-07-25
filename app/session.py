class Session(object):

	def __init__(self, firstname, lastname, email, username, password, users = {}):
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.username = username
		self.password  = password
		self.logged_in = None
		self.users = users

class Login(Session):

	def log_in(self, email, password):
		if email in users.keys():
			
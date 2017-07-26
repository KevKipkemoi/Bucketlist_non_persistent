class UserData(object):

	def __init__(self, name, username, email, password):
		self.name = name
		self.username = username
		self.email = email
		self.password = password
		self.userdata = []

	def new_user_data(self, name, username, email, password):
		self.userdata.append({
			    'Name': name,
			    'Password': password,
			    'email': email,
			    'User Name': username
			})			
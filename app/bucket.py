from forms import LoginForm, GoalsForm


class Bucket(dict, LoginForm, GoalsForm):

    def __init__(self, username, password, goal):
        self.username = username
        self.password = password
        self.goal = goal
    
    remember = False
    added_user = False
    
    def login(self, username):
        if username in user.keys():
            if password == users[username][0]:
                print('login successful')
                remember = True
                return remember
        else:
            print('invalid username or password')
            
    def add_user(self, username, password):
        if username not in users.keys():
            user[username] = [password]
            return 1

    def invalid_user(self, username, password):
        reset = 0
        if not login(username):
            self.users.update({username : [password]})
            added_user = True
            if added_user:
                reset = 1
                added_user = False
            return reset
                
        
    def display_goal(self, username):
        if remember:
            return self.user[username][1]
        else:
            print('please login/signup')
            
    def add_goal(self, username, goal):      
        if remember:
            self.user[username][1].insert(goal)
        else:
            print('please login/signup')
            
    def logout(self, username):
        remember = False

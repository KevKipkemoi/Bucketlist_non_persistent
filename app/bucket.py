from forms import LoginForm, GoalsForm, SignUpForm


class Bucket(dict, LoginForm, GoalsForm):

    def __init__(self, email, username, password, goal):
        self.email = email
        self.username = username
        self.password = password
        self.goal = goal
    
    remember = False
    added_user = False
    
    def login(self, email):
        if email in user.keys():
            if password == users[email][0]:
                print('login successful')
                remember = True
                return remember
        else:
            print('invalid username or password')
            
    def add_user(self, email, password, username):
        if email not in users.keys():
            user[email] = [password, username]
            return 1

    def invalid_user(self, email, password, username):
        reset = 0
        if not login(email):
            self.users.update({email : [password, username]})
            added_user = True
            if added_user:
                reset = 1
                added_user = False
            return reset                
        
    def display_goal(self, email):
        if remember:
            return self.user[username][2]
        else:
            print('please login/signup')
            
    def add_goal(self, email, goal):      
        if remember:
            self.user[email][2].insert(goal)
        else:
            print('please login/signup')
            
    def logout(self, email):
        remember = False

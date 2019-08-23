#in memory table of registered users

from user import User
#
# userid_mapping={
# 1:
# {
# 'id':1,
# 'username':'harry',
# 'password':'potter'}
# }
users=[
    User(1,'bob','asdf')

]

user_mapping={u.username:u for u in users}
userid_mapping={u.id:u for u in users}

def authenticate(username,password):
    #return
    user = userid_mapping.get(username,None)
    if user and user.password==password:
        return user

def identity(payload):
    user_id=payload['identity']
    return userid_mapping.get(user_id,None)

from models.user import userModel


#users = [
 #      User(1, 'bob', 'asdf')
 
#]

#username_mapping = { u.username: u for u in users } ## map user details to usernames

#userid_mapping = { u.id: u for u in users    } ## map user details to ids  
         



def authenticate(username,password):
    user = userModel.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):  #The identity function takes the payload where payload is the content of the JWT token
    user_id = payload['identity']
    return userModel.find_by_id(user_id)
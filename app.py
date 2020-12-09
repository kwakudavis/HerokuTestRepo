from flask import Flask
from flask_restful import Api 
from flask_jwt import JWT

from security import authenticate, identity 
from resources.user    import UserRegister
from resources.item import Item, ItemsList
from resources.store import store, storeList




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///data.db' #Connecting to database 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #We want sql alchemy to do the tracking of modification not flask

app.secret_key = 'jose'

api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity)#autentication


api.add_resource(Item, '/item/<string:name>') #http::127.0.0.1:5000/student/studentName
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegister,'/register') #when we make a request to '/register' its going to make  call to the UserRegister resource 

api.add_resource(storeList, '/stores')

api.add_resource(store, '/store/<string:name>')



if __name__ == '__main__': #This creates the condition that the code should only run app.py when name is main, name is main only when we run python app.py, in that case we can sometimes import app.py and use it as is without having to run it
    from db import db
    db.init_app(app)
    app.run(port=5000, debug = True)#runs application on a particular port











##Notes

##Resource represents objects the API can deal with (response or request)  eg students, items can be resources, they can be mapped into database tables

#User class is a helper class for the UserRegister Resource because the api does not interact directly with it.

#User.py is a model, our internal represenentation of objects





##Simplifies the resource manipulation process


##Every resource has to be a class


##Test-First design - starting of by stating what your api is going to request| all itmes, specific items by name or by id |

##Flask restful allows you to return dictionaries without using jsonify

##tHE most popular http  status code is 200 not 404

##201 IS FOR CREATED

##202 IS FOR WHEN YOU ARE CREATING THE OBJECT WITHIN AFTER A MOMENT AND NOT INSTANTLY

##Filter is more efficient than iterating 

##FLASK JWT is needed for authentication, where JWT stands for Json web token thus encrypting data


##Secret key is going to contain the key


##jwt = JWT(app, authenticate, identity) jwt creates a new endpoint thus /auth and sends it a username and password to the authenticate function, a jwt token is created which is sent during the next request

#Folders in python are mostly reffered to as packages.__init__.py is within folders to show that it can look inside it for python files.. wihtout --init__ they are just folders
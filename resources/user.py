import sqlite3
from flask_restful import Resource,reqparse
from models.user import userModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required  = True, help = "This field cannot be left blank") #username argument
    parser.add_argument('password', type=str, required  = True, help = "This field cannot be left blank") #password argument

    def post(self):
        data =UserRegister.parser.parse_args()
    
        if userModel.find_by_username(data['username']):
            return {"message": "User already exists"}, 400
        else:
           
            user = userModel(**data) #data['username'],data['password'] parser will handle it
            user.save_to_db()

            return {"message":" The user has been created succesfully"},201




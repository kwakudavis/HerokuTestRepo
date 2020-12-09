from flask_restful import Resource, reqparse

from models.store import storeModel


class store(Resource):

    def get(self, name):
        store = storeModel.find_by_name(name)

        if store :
            return store.json()
        return {'message':'Store not found'}, 404


    def post(self, name):
       
       if storeModel.find_by_name(name):
           return {'message':"Store with the name' {} 'already exists".format(name)}, 400

       store = storeModel(name)

       try:
           store.save_to_db()
           return {'message':'store created'},201
       except:
           return {'message':'An error occured while creating the store'}, 500



    def delete(self,name):
       store = storeModel.find_by_name(name)

       if store:
           store.delete_from_db()

       return {'message':'Store deleted'}


class storeList(Resource):
    
    def get(self):
        return {'stores':[store.json() for store in storeModel.query.all()]}
 
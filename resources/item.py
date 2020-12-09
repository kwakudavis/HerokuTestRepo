import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import itemModel




class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required  = True, help = "This field cannot be left blank")
    parser.add_argument('store_id', type=int, required  = True, help = "This field cannot be left blank, an item must belong to a store")

          #This way, we have only defined price and including any other data apart from the price variable will be neglected.
           #request.get_json()







    @jwt_required() #This means we have to authenticate before we can call the get method
    def get(self,name): #name is the name of the item

        item = itemModel.find_by_name(name)
        if item:
            return item.json()
        
        return {'message':'Item not found'}, 404

     #  Previous code
     #  
     #   for item in items:
       #     if item['name'] == name:
       #         return item 
       # item =next(filter(lambda x: x['name'] == name, items), None) #this returns a filter object unless you call a list on it or next to return the first item
        #, NONE TO RETURN A NULL WHEN no item is found
      #  return {'item': item}, 200 if item else 404 #ITEM NOT FOUND




    def post(self,name):

        if itemModel.find_by_name(name):
            return {'message':"An item with the name {} already exists".format(name)}, 400


#  Old code->      if next(filter(lambda x: x['name'] == name, items), None): #since None is the default, condition is met if item name exists already. Check each element in the items against the lamda function 
 #   old code->        return {'message':"An item with name '{}' already exists".format(name)}, 400 #bad request


         #This way, we have only defined price and including any other data apart from the price variable will be neglected.
        data = Item.parser.parse_args()#request.get_json()

        

        #data = request.get_json()#data = request.get_json(force=True) #process content without looking at header, but this is dangerous
      #  item = {'name':name, 'price': data['price']}

        item =itemModel(name,**data)
      
        try:
          item.save_to_db()
        except:
            return {'message':'An error occured while inserting item'}, 500#internal server error
        return item.json(), 201



     #   items.append(item)
    #    return item.json(), 201 #ITEM CREATED






    def delete(self,name):
           item = itemModel.find_by_name(name)
           if item:
               item.delete_from_db()

           return {'message':'Item has been deleted'}

           
    def put(self,name):

          #This way, we have only defined price and including any other data apart from the price variable will be neglected.
        data = Item.parser.parse_args()#request.get_json()




      #Old code ->  item = next((filter(lambda x : x['name']==name, items)),None)

        item = itemModel.find_by_name(name)
        
       
        if item is None: #if item does not exisst 
            #item = {'name':name, 'price': data['price']}
            #items.append(item)
          
          item  = itemModel(name, **data) #creating a new item inserts it automatically to the database
          item.save_to_db()
        else:

          item.price = data['price']
          item.save_to_db()

        
        return item.json()


class ItemsList(Resource):
    def get(self):
      
      return {'items': [x.json() for x in itemModel.query.all()]} #item.json() for item in itemModel.query.all() or list(map(lambda x: x.json(),itemsModel.query.all()))
 
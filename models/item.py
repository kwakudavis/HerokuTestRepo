
from db import db



class itemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2 ))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('storeModel')

    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

     
    def save_to_db(self):
      
        db.session.add(self)
        db.session.commit()


    
    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price = ? WHERE name = ?"
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()


        
    @classmethod
    def find_by_name(cls,name):

       return cls.query.filter_by(name=name).first() #first returns the firsrt row only  ..Select * from items WHERE name = name, table name has already been set



    def json(self):
        return {'name':self.name,'price':self.price}
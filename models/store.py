
from db import db



class storeModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
  
    items = db.relationship('itemModel', lazy = 'dynamic')# so that wedo not spend memory on creating items objects even when we do  not need it

    def __init__(self,name):
        self.name = name
     


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

     
    def save_to_db(self):
      
        db.session.add(self)
        db.session.commit()


        
    @classmethod
    def find_by_name(cls,name):

       return cls.query.filter_by(name=name).first() #first returns the firsrt row only  ..Select * from items WHERE name = name, table name has already been set



    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}#adding .all() overrides the effect of the lazy feature telling the server that it can now create items ob
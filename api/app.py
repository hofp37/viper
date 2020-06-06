from flask import Flask
import json
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
Base = declarative_base()

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres', echo=True)
conn = engine.connect()

SessionFactory = sessionmaker(engine)  
session = SessionFactory()

class Sauto(Base):
    __tablename__ = 'sauto'
    car_id = Column(Integer, primary_key=True)
    brand = Column(String(50))
    model = Column(String(50))
    price = Column(Integer)
    mileage = Column(Integer)
    year_manufactured = Column(Integer)
    snaptime = Column(DateTime(timezone=False))
  
class SautoDTO:
    def __init__(self, ob):
        self.car_id = ob.car_id
        self.brand = ob.brand
        self.model = ob.model
        self.price = ob.price
        self.mileage = ob.mileage
        self.year_manufactured = ob.year_manufactured
        self.snaptime = ob.snaptime

@app.route('/api/cars/', methods=['GET'])
def get_all_cars():
   try:
      results = session.query(Sauto).order_by(Sauto.car_id.asc()).all()
      data = [json.loads(json.dumps(SautoDTO(ob).__dict__, default=lambda x: str(x))) for ob in results]
      response = app.response_class(
         response=json.dumps(data),
         status=200,
         mimetype='application/json'
      )
      return response
   except NoResultFound:
      print('No result was found')
   return 

app.run(port=4996)
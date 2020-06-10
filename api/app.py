from flask import Flask, jsonify, render_template, request
import json
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
def get_cars():
   brand = request.args.get('brand', None)
   priceMin = request.args.get('priceMin', None)
   priceMax = request.args.get('priceMax', None)
   yearMin = request.args.get('yearMin', None)
   yearMax = request.args.get('yearMax', None)
   mileageMax = request.args.get('mileageMax', None)

   sent_params = request.args.to_dict()
   conditions = {
      'brand': '.filter(Sauto.brand == brand)',
      'priceMin': '.filter(Sauto.price >= priceMin)',
      'priceMax': '.filter(Sauto.price <= priceMax)',
      'yearMin': '.filter(Sauto.year_manufactured >= yearMin)',
      'yearMax': '.filter(Sauto.year_manufactured <= yearMax)',
      'mileageMax': '.filter(Sauto.mileage <= mileageMax)'
   }

   def build_query(params):
      validated_dict = params.keys() & conditions.keys()
      filters = ''
      for param in validated_dict:
         filters = filters + conditions[param]
      return 'session.query(Sauto)' + filters + '.order_by(Sauto.car_id.asc())'

   sql_query = build_query(sent_params)
   results = eval(sql_query)
   data = [json.loads(json.dumps(SautoDTO(ob).__dict__, default=lambda x: str(x))) for ob in results]

   return jsonify(data)

@app.route('/cars/')
def render_cars():
   data = get_cars()
   req = data.get_json()

   return render_template('index.html', data=req)

app.run(port=4996)

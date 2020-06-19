import sauto
import load_cars
from constants import Constant

# Script for scraping and loading data into DB for all the car models we have in Constant class
models = Constant.model.keys()

for m in models:

    def get_manufacturer(m):
        return m.split('_', 1)[0]

    params = {
        'category': Constant.category["DEFAULT"],
        'condition': [
            Constant.condition["NEW"],
            Constant.condition["USED"],
            Constant.condition["DEMO"]
            ],
        'priceMax': "",
        'priceMin': "",
        'tachometrMax': "",
        'yearMax': "",
        'yearMin': "",
        'manufacturer': Constant.manufacturer[get_manufacturer(m)],
        'model': Constant.model[m]
    }

    print('Loading script for: ' + m)

    tuple = sauto.get_scraped_results(params)
    load_cars.load_cars_into_db(tuple)

    print('Script done for: ' + m)
    print('---------------------------')
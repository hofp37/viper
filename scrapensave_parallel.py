import sauto_parallel
import load_cars
from constants import Constant
from joblib import Parallel, delayed

# Script for parallel scraping and loading data into DB for all the car models we have in Constant class
models = Constant.model.keys()
params_list = []
tuple_list = []
index = 0
scrape_index = 0

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

    params_list.insert(index, params)
    index += 1

def scrapensave(params):
    tuple = sauto_parallel.get_scraped_results(params)
    return tuple
    

tuple_list = Parallel(n_jobs=-1)(delayed(scrapensave)(params) for params in params_list) #execute parallel for all urls

for tuple in tuple_list:
    load_cars.load_cars_into_db(tuple)
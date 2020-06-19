import  psycopg2
import pandas as pd

def load_cars_into_db(tuple_values):
    
    #QUERY DEFINITION
    sql_1 = """INSERT INTO cars(id,manufacturer,model,price,mileage,year_manufactured,snaptime) VALUES """
    sql_3 = "SELECT MAX(id) FROM cars"

    #CAR TO INSERT
    cars = {'manufacturer': tuple_values[0], 'model': tuple_values[1],'price': tuple_values[2],'mileage': tuple_values[3],'year_manufactured': tuple_values[4],'snaptime': tuple_values[5]}
    cars= pd.DataFrame(data=cars)

    #car2 = """,'""" +str(cars['manufacturer'][1]) + """','""" + str(cars['model'][1]) + """','""" + str(cars['price'][1]) + """','""" + str(cars['mileage'][1]) + """','""" + str(cars['year_manufactured'][1]) + """','""" + str(cars['snaptime'][1])+ """')"""


    #FUNCTION TO GENERATE STRING FOR CAR ADDITION
    def car_addition_string(cars):
        last_id = check_last_id()    
        car_id = last_id
        rows_to_add =cars.shape[0]
        if rows_to_add ==0:
            pass
        elif rows_to_add ==1:
            sql_string = """("""+str(car_id+1)+""",'""" +str(cars['manufacturer'][0]) + """','""" + str(cars['model'][0]) + """','""" + str(cars['price'][0]) + """','""" + str(cars['mileage'][0]) + """','""" + str(cars['year_manufactured'][0]) + """','""" + str(cars['snaptime'][0])+ """')"""
        else:
            sql_string = """("""+str(car_id+1)+""",'""" +str(cars['manufacturer'][0]) + """','""" + str(cars['model'][0]) + """','""" + str(cars['price'][0]) + """','""" + str(cars['mileage'][0]) + """','""" + str(cars['year_manufactured'][0]) + """','""" + str(cars['snaptime'][0])+ """')"""
            for i in range(1,rows_to_add):
                sql_string +=""",("""+str(car_id+i+1)+""",'""" +str(cars['manufacturer'][i]) + """','""" + str(cars['model'][i]) + """','""" + str(cars['price'][i]) + """','""" + str(cars['mileage'][i]) + """','""" + str(cars['year_manufactured'][i]) + """','""" + str(cars['snaptime'][i])+ """')"""
        return sql_string


    #FUNCTION TO CHECK LAST ID IN SAUTO TABLE
    def check_last_id():
        sql = sql_3
        try:
            conn = psycopg2.connect(host="localhost",database="sauto", user="postgres", password="postgres")
            # create a new cursor
            cur = conn.cursor()
            # execute the SELECT statement
            cur.execute(sql)
            # get the generated id back
            car_id = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return car_id

    #FUNCTION TO ADD CAR TO SAUTO TABLE
    def insert_car(car):
        """ insert a new vendor into the vendors table """
        conn = None
        sql = sql_1 + car_addition_string(car)
        try:
            conn = psycopg2.connect(host="localhost",database="sauto", user="postgres", password="postgres")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql)
            # get the generated id back
            #car_id = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        #return car_id

    #LOAD CARS

    insert_car(cars)
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:20:26 2020

@author: petrr
"""
import  psycopg2
import pandas as pd

#QUERY DEFINITION
sql_1 = """INSERT INTO sauto(car_id,brand,model,price,mileage,year_manufactured,snaptime) VALUES ("""
sql_3 = "SELECT MAX(car_id) FROM sauto"

#CAR TO INSERT
car = ",'AUDI','A2',290000,150000,2018,'2020-05-22 19:17:23-07')"


#FUNCTION TO CHECK LAST ID IN SAUTO TABLE
def check_last_id():
    sql = sql_3
    try:
        conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="ref")
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
    car_id = check_last_id()
    sql = sql_1 + str(car_id+1) + car
    try:
        conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="ref")
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
    
insert_car(car)

  
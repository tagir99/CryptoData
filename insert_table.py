from main import Recomendation
import psycopg2
import datetime

ltc_usdt = Recomendation('ltc', 'usdt', 142)

def insert_table():
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host='127.0.0.1',
            user='postgres',
            password='*****',
            dbname='bot_transaction',
            port=5432
        )

        # the cursor for performing database operator
        cursor = connection.cursor()

        item_purchase_time = datetime.datetime.now()
        insert_query = (
            """INSERT INTO transactions (coin, price, rec_price, purchase_time, buy) 
                VALUES (%s, %s, %s, %s, %s)""")
        item_tuple = (ltc_usdt.coin_nm(), ltc_usdt.inf_price(), ltc_usdt.rec_price(), item_purchase_time, \
                      ltc_usdt.buy())

        cursor.execute(insert_query, item_tuple) # в cursor.execute передаются два параметра - вставки, сами значения

        connection.commit()
        print('[INFO] insert sucessfully')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')

insert_table()
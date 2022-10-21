import psycopg2

def create_table():
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host='0.0.0.0',
            user='qwerty',
            password='qwerty',
            dbname='exampledb',
            port=5432
        )

        # the cursor for performing database operator
        cursor = connection.cursor()

        cursor.execute(
            """CREATE TABLE transactions(
                id_operaion serial PRIMARY KEY,
                coin varchar(10) NOT NULL,
                price float(5) NOT NULL,
                rec_price float(5) NOT NULL,
                purchase_time timestamp NOT NULL,
                buy varchar(10) NOT NULL
                )"""
        )

        connection.commit()
        print('[INFO] create table sucesfully')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')

create_table()
#docker-compose up -d
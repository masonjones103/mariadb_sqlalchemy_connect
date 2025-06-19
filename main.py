# Mason Jones mcjones@student.rtc.edu
# CNE 370
# Spring 2025
# code outline sourced from https://www.geeksforgeeks.org/python/connecting-to-sql-database-using-sqlalchemy-in-python/
# code uses sqlalchemy create_engine to connect to the mariadb database and uses the text module to query the databases.

from sqlalchemy import create_engine
from sqlalchemy import text

user = 'maxuser'
password = 'maxpwd'
host = '127.0.0.1'
port = 4000
database1 = 'zipcodes_one'
database2 = 'zipcodes_two'

def get_connection1():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database1
        )
    )

def get_connection2():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database2
        )
    )

if __name__ == '__main__':

    try:
      
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection1()
        with engine.connect() as connection:
            # largest zip code in zipcodes one
            result = connection.execute(text("SELECT MAX(Zipcode) FROM zipcodes_one"))
            input("The largest zip code in zipcodes one is:")
            for row in result:
                print(row)
            # all kentucky zipcodes in zipcodes one
            result = connection.execute(text("SELECT Zipcode FROM zipcodes_one WHERE State='KY'"))
            input("All zipcodes from Kentucky:")
            for row in result:
                print(row)

        engine = get_connection2()
        with engine.connect() as connection:
            # all kentucky zipcodes in zipcodes two
            result = connection.execute(text("SELECT Zipcode FROM zipcodes_two WHERE State='KY'"))
            for row in result:
                print(row)

        engine = get_connection1()
        with engine.connect() as connection:
            # all zipcodes between 40000 and 41000 in zipcodes one
            result = connection.execute(text("SELECT Zipcode FROM zipcodes_one WHERE Zipcode >= 40000 AND Zipcode <= 41000"))
            input("All zipcodes between 40000 and 41000:")
            for row in result:
                print(row)

        engine = get_connection2()
        with engine.connect() as connection:
            # all zipcodes between 40000 and 41000 in zipcodes two
            result = connection.execute(text("SELECT Zipcode FROM zipcodes_two WHERE Zipcode >= 40000 AND Zipcode <= 41000"))
            for row in result:
                print(row)

        engine = get_connection1()
        with engine.connect() as connection:
            # the total wages in Pennsylvania in zipcodes one
            result = connection.execute(text("SELECT TotalWages FROM zipcodes_one WHERE State='PA'"))
            input("Total wages from Pennsylvania:")
            for row in result:
                print(row)

        engine = get_connection2()
        with engine.connect() as connection:
            # the total wages in Pennsylvania in zipcodes two
            result = connection.execute(text("SELECT TotalWages FROM zipcodes_two WHERE State='PA'"))
            for row in result:
                print(row)

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

from sqlalchemy import create_engine

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
        print(
            f"Connection to {host}, database: {database1}, for user {user} created successfully.")
        engine = get_connection2()
        print(
            f"Connection to {host}, database: {database2}, for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

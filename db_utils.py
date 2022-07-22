
import pymysql.cursors

def get_mysql_connection():


    # Connect to the database
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='db',
                             cursorclass=pymysql.cursors.DictCursor)

    return connection

def insert_predicted_price(price):

    connection = get_mysql_connection()
    print("price", price)
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `house` (`predicted_price`) VALUES (%s)"
            cursor.execute(sql, [price])

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()


import psycopg2

class DatabaseConnection:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname="collectors-app",
                user="postgres",
                password="admin1234",
                host="localhost",
                port="5432"
            )
            print("Connected to the database successfully.")
            self.cursor = self.connection.cursor()
        except Exception as e:
            print("Error connecting to the database: ", e)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
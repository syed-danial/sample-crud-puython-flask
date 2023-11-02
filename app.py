from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def check_connection():
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database="flask_db",
            user="postgres",
            password="adminadmin",
            host="172.23.0.1",
            port="5432"
        )

        # If the connection is successful, return a success message
        message = "Database connection established successfully!"
    except Exception as e:
        # If there's an error, return the error message
        message = f"Error connecting to the database: {str(e)}"

    return message

if __name__ == '__main__':
    app.run(debug=True)

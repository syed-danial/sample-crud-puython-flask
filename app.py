from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def check_connection():
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database="workoutapp",
            user="postgres",
            password="FVynNoS7fAusCiLv",
            host="parserapp-dev.ckzduimfmpdl.us-west-2.rds.amazonaws.com",
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

from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Define your MySQL connection details
db_config = {
    'host': 'localhost',
    'user': 'Admin',
    'password': 'admin@123',
    'database': 'placement_data'
}

@app.route('/')
def index():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Fetch data from the database (modify the SQL queries as needed)
        cursor.execute('SELECT COUNT(*) FROM student_data WHERE placement_status = "Placed"')
        placed_count = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM student_data WHERE placement_status = "Not Placed"')
        not_placed_count = cursor.fetchone()[0]

        conn.close()

        return render_template('admin.html', placed_count=placed_count, not_placed_count=not_placed_count)
    except mysql.connector.Error as err:
        # Handle database connection errors here
        print(f"Error: {err}")
        return "Error connecting to the database"

if __name__ == '__main__':
    app.run(debug=True)

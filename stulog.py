from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    "host": "localhost",       
    "user": "Admin",    
    "password": "admin@123",  
    "database": "college"  
}

# Route to display the registration form
@app.route('/')
def registration_form():
    return render_template('stulog.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into the database
        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        data = (username, password)

        cursor.execute(insert_query, data)
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()

        return "Registration successful!"

if __name__ == '__main__':
    app.run(debug=True)

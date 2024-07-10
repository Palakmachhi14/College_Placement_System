from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Define your MySQL connection details
db_host = 'localhost'
db_name = 'placement_data'
db_user = 'Admin'
db_password = 'admin@123'

def init_db():
    # Connect to MySQL
    conn = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            position VARCHAR(255),
            year INT,
            location VARCHAR(255),
            start_date DATE,
            relocate VARCHAR(255),
            secondary_education VARCHAR(255),
            secondary_percentage FLOAT,
            secondary_year INT,
            higher_education VARCHAR(255),
            higher_percentage FLOAT,
            higher_year INT,
            college_name VARCHAR(255),
            major VARCHAR(255),
            current_year INT,
            cgpa FLOAT,
            graduation_year INT,
            graduation_date DATE,
            resume_path VARCHAR(255),
            cover_letter_path VARCHAR(255),
            reference_name_1 VARCHAR(255),
            reference_contact_1 VARCHAR(255),
            reference_email_1 VARCHAR(255),
            reference_name_2 VARCHAR(255),
            reference_contact_2 VARCHAR(255),
            reference_email_2 VARCHAR(255),
            declaration_signature_path VARCHAR(255),
            declaration_date DATE,
            enrollment_no VARCHAR(255),
            password VARCHAR(255)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('success.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        position = request.form['position']
        year = request.form['year']
        location = request.form['location']
        start_date = request.form['date']
        relocate = request.form['relocate']
        secondary_education = request.form['collegeName']
        secondary_percentage = request.form['percentage']
        secondary_year = request.form['year']
        higher_education = request.form['collegeName']
        higher_percentage = request.form['percentage']
        higher_year = request.form['year']
        college_name = request.form['collegeName']
        major = request.form['major']
        current_year = request.form['curryear']
        cgpa = request.form['cgpa']
        graduation_year = request.form['year']
        graduation_date = request.form['date']
        resume_path = request.files['documents'].filename
        cover_letter_path = request.files['documents'].filename
        reference_name_1 = request.form['name']
        reference_contact_1 = request.form['number']
        reference_email_1 = request.form['email']
        reference_name_2 = request.form['name']
        reference_contact_2 = request.form['number']
        reference_email_2 = request.form['email']
        declaration_signature_path = request.files['photo'].filename
        declaration_date = request.form['date']
        enrollment_no = request.form['username']
        password = request.form['password']

        # Connect to MySQL
        conn = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO student_data (position, year, location, start_date, relocate, secondary_education,
            secondary_percentage, secondary_year, higher_education, higher_percentage, higher_year, college_name,
            major, current_year, cgpa, graduation_year, graduation_date, resume_path, cover_letter_path,
            reference_name_1, reference_contact_1, reference_email_1, reference_name_2, reference_contact_2,
            reference_email_2, declaration_signature_path, declaration_date, enrollment_no, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (position, year, location, start_date, relocate, secondary_education, secondary_percentage, secondary_year,
              higher_education, higher_percentage, higher_year, college_name, major, current_year, cgpa, graduation_year,
              graduation_date, resume_path, cover_letter_path, reference_name_1, reference_contact_1, reference_email_1,
              reference_name_2, reference_contact_2, reference_email_2, declaration_signature_path, declaration_date,
              enrollment_no, password))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

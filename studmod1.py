from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_host = 'localhost'
db_name = 'placement_data'
db_user = 'Admin'
db_password = 'admin@123'

@app.route('/student/<enrollment_no>')
def student_page(enrollment_no):
    conn = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = conn.cursor()

    cursor.execute('SELECT student_name, position, year, location FROM student_data WHERE enrollment_no = %s', (enrollment_no,))
    student_info = cursor.fetchone()

    if student_info:
        student_info = {
            'student_name': student_info[0],
            'enrollment_no': enrollment_no,
            'position': student_info[1],
            'year': student_info[2],
            'location': student_info[3]
        }
        conn.close()
        return render_template('student_page.html', **student_info)
    else:
        return "Student not found", 404

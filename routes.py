from flask import Blueprint, render_template, flash, request, redirect, url_for, jsonify
import sqlite3
import csv

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html') # can also pass show_nav_bar = True, as an arg and it will work

@routes.route('/query')
def query():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses")

    # Step 1: Create a table with proper column names
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            title TEXT,
            description TEXT,
            url TEXT
        )
    ''')


    # Step 3: Correct CSV reading and inserting
    csv_file = 'ualberta_courses.csv'
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip the header row

        for row in reader:
            print(row)  
            cursor.execute("INSERT INTO courses (title, description, url) VALUES (?, ?, ?)", row)
    print()

    # Step 4: Commit and query the table
    conn.commit()

    re = '''
        SELECT * FROM courses;
    '''
    cursor.execute(re)
    rows = cursor.fetchall()

    results = [{"title": row[0], "description": row[1], "url": row[2]} for row in rows]

    conn.close()

    return jsonify(results)

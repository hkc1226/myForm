from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
conn = mysql.connector.connect(
    host='sql12.freesqldatabase.com',
    user='sql12786802',
    password='bZt3r2tYYu',
    database='sql12786802'
)
cursor = conn.cursor()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']

    cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
    conn.commit()
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Hrishi#1226',
    database='myformdb'
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

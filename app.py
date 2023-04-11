from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="posterportaldb"
)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if 1:
        # valid credentials
        return redirect(url_for("dashboard"))
    else:
        # invalid credentials
        return redirect(url_for("home"))


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    # Retrieve the username, email, and password from the request
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Insert the new user into the database
    cursor = mydb.cursor()
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, password))
    
    # Commit changes and close cursor
    mydb.commit()
    cursor.close()

    return redirect(url_for("home")) 


@app.route('/forgot-password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'GET':
        return render_template('forgotpassword.html')
    return 'hehe'    

if __name__ == '__main__':
    app.run(debug=True)
    
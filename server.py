from flask import Flask, render_template, redirect, request
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('friendsdb')
# now, we may invoke the query_db method
# print("all the users", mysql.query_db("SELECT * FROM users;"))

@app.route("/")
def index():
    all_friends = mysql.query_db("select * from friends")
    return render_template("index.html", friends=all_friends)

@app.route("/add_friend", methods=["POST"])
def add_friend():
    first_name = request.form["fname"]
    last_name = request.form["lname"]
    occupation = request.form["occupation"]
    query = "insert into friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, now(), now());"
    data = {"first_name":first_name,"last_name":last_name,"occupation":occupation}
    mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)